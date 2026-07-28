// ============================================================================
// CONFIGURACIÓN DE NODOS EN 3DCOAT (NGL)
// ============================================================================
in vec2 UVCoord(knot = ioUV); // Coordenadas UV de entrada

// Deslizadores de frecuencia compactados para máxima precisión (0.0 a 10.0)
in float Frequency(value = 1.0, min = 0.0, max = 10.0); // Escala visual de 0 a 10 (internamente x10)
in float Sharpness(value = 0.0, min = 0.0, max = 1.0); // Control de dureza del degradado

// Switches ON/OFF (Checkboxes)
#bool Invert                // True = Invierte la máscara final y normales

// ============================================================================
// SALIDAS (Conectores del nodo) - Mantenidos estrictamente en líneas 16 a 19
// ============================================================================
out vec3 Color;       // Salida RGB de color (Línea 16)
out vec3 Normal;      // Vector normal en espacio tangente (Línea 17)
out float NonColor;   // Patrón procedural en escala de grises (Línea 18)
out float Opacity;    // Máscara de opacidad para transparencia (Línea 19)

// ============================================================================
// CONTROLES ADICIONALES (Leídos dinámicamente, Offset removido)
// ============================================================================
in float Scale(value = 1.0, min = 0.1, max = 10.0); // Multiplicador de escala
in float DistortIntensity(value = 0.0, min = 0.0, max = 5.0); // Intensidad de la distorsión
in float DistortScale(value = 2.0, min = 0.1, max = 10.0); // Rango de 0.1 a 10
in float Bright(value = 0.0, min = -1.0, max = 1.0); // Offset de luminancia (Baseline)
in float Contrast(value = 1.0, min = 0.0, max = 5.0); // Contraste general

// ============================================================================
// FUNCIONES AUXILIARES
// ============================================================================

// Constantes de transformación de hash estáticas
const mat2 myt = mat2(.12121212, .13131313, -.13131313, .12121212);
const vec2 mys = vec2(1e4, 1e6);

// Hash pseudoaleatorio rápido de 2 dimensiones
vec2 rhash(vec2 uv) {
  uv *= myt;
  uv *= mys;
  return fract(fract(uv / mys) * uv);
}

// Algoritmo de Voronoi Suavizado 2D (Smooth Voronoi)
float voronoi2d(in vec2 point) {
  vec2 p = floor(point);
  vec2 f = fract(point);
  float res = 0.0;
  
  // Bucle sobre el vecindario de celdas 3x3
  for (int j = -1; j <= 1; j++) {
    for (int i = -1; i <= 1; i++) {
      // Corrección de casteo estricto de tipos para GPUs AMD/NVIDIA
      vec2 b = vec2(float(i), float(j));
      vec2 r = b - f + rhash(p + b);
      // Acumulación exponencial para suavizar la distancia mínima
      res += 1. / pow(dot(r, r), 8.);
    }
  }
  return pow(1. / res, 0.0625); // Exponente normalizado (1 / 16)
}

// Retorna el valor final de intensidad aplicando contrastes y dureza (Sharpness)
float getVoronoiValue(vec2 P) {
    float rawNoise = voronoi2d(P);
    float noiseVal = clamp(rawNoise, 0.0, 1.0); // Rango nativo es de 0.0 a 1.0
    
    // Aplicamos Bright y Contraste
    float processedNoise = (noiseVal - 0.5) * Contrast + 0.5 + Bright;
    float final_intensity = clamp(processedNoise, 0.0, 1.0);

    // Aplicamos el control de Sharpness (Dureza del degradado)
    float soft_width = max((1.0 - Sharpness) * 0.5, 0.0001);
    float edge0 = max(0.5 - soft_width, 0.0);
    float edge1 = min(0.5 + soft_width, 1.0);

    float t = clamp((final_intensity - edge0) / (edge1 - edge0), 0.0, 1.0);
    return t * t * (3.0 - 2.0 * t);
}

// ============================================================================
// EJECUCIÓN DIRECTA (Cuerpo principal / "Implicit Main")
// ============================================================================

// Coordenadas UV de entrada directas (Offset removido)
vec2 uv = UVCoord;

// Aplicamos la repetición global multiplicando la frecuencia ingresada por 10.0 (escala real x10)
float globalScale = (Frequency * 10.0) * Scale;
uv *= globalScale;

// --- DOMAIN WARPING (DISTORTION EN VORONOI LISO) ---
if (DistortIntensity > 0.001) {
    vec2 distort_uv = uv * DistortScale;
    // Utilizamos el propio ruido Voronoi para distorsionar su espacio de forma orgánica
    vec2 distort = vec2(voronoi2d(distort_uv), voronoi2d(distort_uv + vec2(31.415, 57.123)));
    uv += (distort - 0.5) * DistortIntensity;
}

// --- EVALUACIÓN DE VALUE NOISE ---
float main_intensity = getVoronoiValue(uv);

// Cálculo de derivadas numéricas dinámicas usando diferencias finitas centrales de alta fidelidad
float h = 0.002; // Paso de muestreo óptimo
float val_x = getVoronoiValue(uv + vec2(h, 0.0));
float val_y = getVoronoiValue(uv + vec2(0.0, h));

vec2 final_derivatives = vec2(val_x - main_intensity, val_y - main_intensity) * (1.0 / h);

// Calculamos el vector normal final en espacio tangente
vec3 final_normal = normalize(vec3(-final_derivatives.x, -final_derivatives.y, 1.0));

// --- INVERSIÓN FINAL (Invert) ---
#if Invert
    main_intensity = 1.0 - main_intensity;
    final_derivatives = -final_derivatives;
    final_normal = normalize(vec3(-final_derivatives.x, -final_derivatives.y, 1.0));
#endif

// Asignamos las salidas finales respetando el orden exacto de los pines en la interfaz de 3DCoat
Color = vec3(main_intensity);              // Línea 16
Normal = final_normal;                     // Línea 17
NonColor = main_intensity;                 // Línea 18
Opacity = main_intensity;                  // Línea 19