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
in float Jitter(value = 1.0, min = 0.0, max = 1.0);  // Alineación/caos de los centros de celda
in float DistortIntensity(value = 0.0, min = 0.0, max = 5.0); // Intensidad de la distorsión
in float DistortScale(value = 2.0, min = 0.1, max = 10.0); // Rango de 0.1 a 10
in float Bright(value = 0.0, min = -1.0, max = 1.0); // Offset de luminancia (Baseline)
in float Contrast(value = 1.0, min = 0.0, max = 5.0); // Contraste general

// ============================================================================
// FUNCIONES AUXILIARES
// ============================================================================

// Hash pseudoaleatorio rápido de 2 dimensiones
vec2 hash( vec2 p ) {
    p = vec2( dot(p,vec2(127.1,311.7)), dot(p,vec2(269.5,183.3)) );
    return fract(sin(p) * 43758.5453);
}

// Algoritmo de ruido celular Worley 2D con ventana de búsqueda 3x3 y Jitter dinámico
float cellular2x2(vec2 P, float jitter) {
    vec2 Pi = floor(P);
    vec2 Pf = fract(P);
    
    float min_dist = 1.0;
    
    // Bucle sobre el vecindario de celdas 3x3
    for (int x = -1; x <= 1; x++) {
        for (int y = -1; y <= 1; y++) {
            vec2 neighbor = vec2(float(x), float(y));
            
            // Calculamos el punto pseudoaleatorio base
            vec2 randPoint = hash(Pi + neighbor);
            
            // Aplicamos el jitter de forma simétrica alrededor del centro de la celda (0.5)
            vec2 point = 0.5 + jitter * (randPoint - 0.5);
            
            vec2 diff = neighbor + point - Pf;
            float dist = length(diff); // Distancia Euclidiana
            
            min_dist = min(min_dist, dist);
        }
    }
    return min_dist;
}

// Retorna el valor final de intensidad de celda aplicando contrastes y dureza (Sharpness)
float getCellularValue(vec2 P) {
    float normValue = clamp(cellular2x2(P, Jitter), 0.0, 1.0);
    
    // Aplicamos Bright (Baseline) y Contraste
    float processedNoise = (normValue - 0.5) * Contrast + 0.5 + Bright;
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

// Tomamos las coordenadas de UVCoord directamente (Offset removido)
vec2 uv = UVCoord;

// Aplicamos la repetición global multiplicando la frecuencia ingresada por 10.0 (escala real x10)
float globalScale = (Frequency * 10.0) * Scale;
uv *= globalScale;

// --- DOMAIN WARPING (DISTORTION EN CELULAS) ---
if (DistortIntensity > 0.001) {
    vec2 distort_uv = uv * DistortScale;
    // Usamos el propio ruido celular de celdas para distorsionar su propio espacio de forma orgánica
    float d0 = cellular2x2(distort_uv, Jitter);
    float d1 = cellular2x2(distort_uv + vec2(31.415, 57.123), Jitter);
    // Corrección: Resta explícita de vectores para compatibilidad total de compilación
    uv += (vec2(d0, d1) - vec2(0.5)) * DistortIntensity;
}

// --- EVALUACIÓN DE VALUE NOISE ---
float main_intensity = getCellularValue(uv);

// Cálculo de derivadas numéricas dinámicas usando diferencias finitas centrales de alta fidelidad
float h = 0.002; // Paso de muestreo óptimo
float val_x = getCellularValue(uv + vec2(h, 0.0));
float val_y = getCellularValue(uv + vec2(0.0, h));

vec2 final_derivatives = vec2(val_x - main_intensity, val_y - main_intensity) * (1.0 / h);

// Calculamos el vector normal final en espacio tangente
vec3 final_normal = normalize(vec3(-final_derivatives.x, -final_derivatives.y, 1.0));

// --- INVERSIÓN FINAL (Invert) ---
// Corrección: Uso estricto de #ifdef para evitar errores de preprocesamiento en 3DCoat
#ifdef Invert
    main_intensity = 1.0 - main_intensity;
    final_derivatives = -final_derivatives;
    final_normal = normalize(vec3(-final_derivatives.x, -final_derivatives.y, 1.0));
#endif

// Asignamos las salidas finales respetando el orden exacto de los pines en la interfaz de 3DCoat
Color = vec3(main_intensity);              // Línea 16
Normal = final_normal;                     // Línea 17
NonColor = main_intensity;                 // Línea 18
Opacity = main_intensity;                  // Línea 19