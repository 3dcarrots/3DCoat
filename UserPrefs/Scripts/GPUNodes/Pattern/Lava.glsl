// ============================================================================
// CONFIGURACIÓN DE NODOS EN 3DCOAT (NGL)
// ============================================================================
in vec2 UVCoord(knot = ioUV); // Coordenadas UV de entrada

// Deslizadores de frecuencia compactados para máxima precisión (0.0 a 10.0)
in float Frequency(value = 1.0, min = 0.0, max = 10.0); // Escala visual de 0 a 10 (internamente x10)
in float Sharpness(value = 0.0, min = 0.0, max = 1.0); // Control de dureza del degradado

// #bool Invert                // True = Invierte la máscara final, color y normales

// ============================================================================
// SALIDAS (Conectores del nodo) - Mantenidos estrictamente en líneas 16 a 19
// ============================================================================
out vec3 Color;       // Salida RGB de color (Línea 16)
out vec3 Normal;      // Vector normal en espacio tangente (Línea 17)
out float NonColor;   // Patrón procedural en escala de grises (Línea 18)
out float Opacity;    // Máscara de opacidad para transparencia (Línea 19)

// ============================================================================
// CONTROLES ADICIONALES (Leídos dinámicamente, Offset, Time y Speed removidos)
// ============================================================================
in float Scale(value = 1.0, min = 0.1, max = 10.0); // Multiplicador de escala
in float DistortIntensity(value = 0.0, min = 0.0, max = 5.0); // Intensidad de la turbulencia
in float DistortScale(value = 2.0, min = 0.1, max = 10.0); // Escala de la distorsión
in float Bright(value = 0.0, min = -1.0, max = 1.0); // Offset de luminancia (Baseline)
in float Contrast(value = 1.0, min = 0.0, max = 5.0); // Contraste general

// Selectores de color nativos (reemplazan etiquetas X,Y,Z por R,G,B con paleta circular)
in color LineColor(value = vec4(1.0, 0.3, 0.0, 1.0)); // Color de la lava (Naranja por defecto)
in color BgColor(value = vec4(0.05, 0.05, 0.05, 1.0)); // Color del fondo (Negro volcánico)

// ============================================================================
// FUNCIONES AUXILIARES
// ============================================================================

// Matriz de rotación 2D segura
mat2 rotate2D(float r) {
    return mat2(cos(r), sin(r), -sin(r), cos(r));
}

// Hash rápido de 2 dimensiones para distorsión espacial
float hash(vec2 p) {
    return fract(sin(dot(p, vec2(127.1, 311.7))) * 43758.5453);
}

// Ruido de Valor 2D base para el Domain Warping
float noise(vec2 p) {
    vec2 i = floor(p);
    vec2 f = fract(p);
    vec2 u = f * f * (3.0 - 2.0 * f);
    return mix(mix(hash(i + vec2(0.0, 0.0)), 
                   hash(i + vec2(1.0, 0.0)), u.x),
               mix(hash(i + vec2(0.0, 1.0)), 
                   hash(i + vec2(1.0, 1.0)), u.x), u.y);
}

// Retorna el valor final de intensidad de forma estática
float getLavaNoise(vec2 uvCoord) {
    vec2 n = vec2(0.0);
    vec2 q = vec2(0.0);
    vec2 p = uvCoord;
    
    float t = 0.0; // Tiempo congelado para textura fija
    float S = 12.0;
    float a = 0.0;
    mat2 m = rotate2D(5.0);

    // Bucle de realimentación trigonométrica de 20 pasadas
    for (float j = 0.0; j < 20.0; j += 1.0) {
        p *= rotate2D(5.0);
        n *= m;
        q = p * S + vec2(t + j) + n; 
        a += sin(q.x) / S;
        n -= cos(q);
        S *= 1.2;
    }
    
    // Normalizamos el acumulador de zozuar al rango de máscaras [0, 1]
    float normValue = clamp(a * 2.0 + 0.5, 0.0, 1.0);
    
    // Aplicamos Bright (Baseline) y Contraste
    float processedNoise = (normValue - 0.5) * Contrast + 0.5 + Bright;
    float final_intensity = clamp(processedNoise, 0.0, 1.0);

    // Aplicamos el control de Sharpness (Dureza del degradado)
    float soft_width = max((1.0 - Sharpness) * 0.5, 0.0001);
    float edge0 = max(0.5 - soft_width, 0.0);
    float edge1 = min(0.5 + soft_width, 1.0);

    float factor = clamp((final_intensity - edge0) / (edge1 - edge0), 0.0, 1.0);
    return factor * factor * (3.0 - 2.0 * factor);
}

// ============================================================================
// EJECUCIÓN DIRECTA (Cuerpo principal / "Implicit Main")
// ============================================================================

// Coordenadas UV directas sin desplazamientos (Offset removido)
vec2 uv = UVCoord;

// Aplicamos la repetición global multiplicando la frecuencia ingresada por 10.0 (escala real x10)
float globalScale = (Frequency * 10.0) * Scale;
uv *= globalScale;

// --- DOMAIN WARPING (DISTORTION EN LAVA) ---
if (DistortIntensity > 0.001) {
    vec2 distort_uv = uv * DistortScale;
    vec2 distort = vec2(noise(distort_uv), noise(distort_uv + vec2(31.415, 57.123)));
    uv += (distort - vec2(0.5)) * DistortIntensity;
}

// --- EVALUACIÓN DEL RUIDO GEOMÉTRICO ---
float main_intensity = getLavaNoise(uv);

// Cálculo de normales dinámicas por diferencias finitas centrales de alta fidelidad
float h = 0.002; // Paso de muestreo óptimo
float val_x = getLavaNoise(uv + vec2(h, 0.0));
float val_y = getLavaNoise(uv + vec2(0.0, h));

vec2 final_derivatives = vec2(val_x - main_intensity, val_y - main_intensity) * (1.0 / h);

// Calculamos el vector normal final en espacio tangente
vec3 final_normal = normalize(vec3(-final_derivatives.x, -final_derivatives.y, 1.0));

// --- INVERSIÓN FINAL (Invert) ---
#ifdef Invert
    main_intensity = 1.0 - main_intensity;
    final_derivatives = -final_derivatives;
    final_normal = normalize(vec3(-final_derivatives.x, -final_derivatives.y, 1.0));
#endif

// Mezcla de color final (.rgb de los selectores seguros)
vec3 final_color = mix(BgColor.rgb, LineColor.rgb, vec3(main_intensity));

// Asignamos las salidas finales respetando el orden exacto de los pines en la interfaz de 3DCoat
Color = final_color;                       // Línea 16
Normal = final_normal;                     // Línea 17
NonColor = main_intensity;                 // Línea 18
Opacity = main_intensity;                  // Línea 19