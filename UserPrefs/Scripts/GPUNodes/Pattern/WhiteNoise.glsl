// ============================================================================
// CONFIGURACIÓN DE NODOS EN 3DCOAT (NGL)
// ============================================================================
in vec2 UVCoord(knot = ioUV); // Coordenadas UV de entrada

// Deslizadores de frecuencia compactados para máxima precisión (0.0 a 10.0)
in float Frequency(value = 1.0, min = 0.0, max = 10.0); // Escala visual de 0 a 10 (internamente x10)
in float Sharpness(value = 0.0, min = 0.0, max = 1.0); // Control de dureza del degradado

#bool Invert                // True = Invierte la máscara final y normales

// ============================================================================
// SALIDAS (Conectores del nodo) - Mantenidos estrictamente en líneas 16 a 19
// ============================================================================
out vec3 Color;       // Salida RGB de color (Línea 16)
out vec3 Normal;      // Vector normal en espacio tangente (Línea 17)
out float NonColor;   // Patrón procedural en escala de grises (Línea 18)
out float Opacity;    // Máscara de opacidad para transparencia (Línea 19)

// ============================================================================
// CONTROLES ADICIONALES (Leídos dinámicamente, Offset y Pixelated ocultos)
// ============================================================================
in float Scale(value = 1.0, min = 0.1, max = 20.0); // Multiplicador de escala
in float DistortIntensity(value = 0.0, min = 0.0, max = 5.0); // Intensidad de la distorsión
in float DistortScale(value = 2.0, min = 0.1, max = 10.0); // Rango de 0.1 a 10
in float Bright(value = 0.0, min = -1.0, max = 1.0); // Offset de luminancia (Baseline)
in float Contrast(value = 1.0, min = 0.0, max = 5.0); // Contraste general

// ============================================================================
// FUNCIONES AUXILIARES
// ============================================================================

// Función de Hash basada en enteros de 32 bits y operaciones binarias a nivel de GPU
float hash21(vec2 p) {
    uvec2 q = uvec2(p * 8192.0);
    q = 1103515245u * ((q >> 1u) ^ q.yx);
    uint n = 1103515245u * (q.x ^ (q.y >> 3u));
    return float(n) * (1.0 / float(0xffffffffu));
}

// Retorna el valor final de intensidad aplicando pixelado forzado (floor) de forma interna constante
float getHashValue(vec2 P) {
    // El redondeo se ejecuta siempre de manera nativa para que responda a Frequency y Scale
    P = floor(P); 

    float rawNoise = hash21(P);
    float noiseVal = rawNoise; // Rango nativo es 0.0 a 1.0
    
    // Aplicamos Bright (Baseline) y Contraste
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

// Tomamos las coordenadas de entrada directamente (Offset removido)
vec2 uv = UVCoord;

// Aplicamos la repetición global multiplicando la frecuencia ingresada por 10.0 (escala real x10)
float globalScale = (Frequency * 10.0) * Scale;
uv *= globalScale;

// --- DOMAIN WARPING (DISTORTION EN GRANO) ---
if (DistortIntensity > 0.001) {
    vec2 distort_uv = uv * DistortScale;
    // Utilizamos el ruido blanco para distorsionar su propio espacio de forma orgánica
    vec2 distort = vec2(hash21(distort_uv), hash21(distort_uv + vec2(31.415, 57.123)));
    uv += (distort - vec2(0.5)) * DistortIntensity;
}

// --- EVALUACIÓN DEL GRANO PROCEDURAL (DIFERENCIAS FINITAS INCORPORAN FLOOR INTERNO) ---
float main_intensity = getHashValue(uv);

// Cálculo de derivadas numéricas dinámicas usando diferencias finitas centrales de alta fidelidad
float h = 0.002; // Paso de muestreo óptimo
float val_x = getHashValue(uv + vec2(h, 0.0));
float val_y = getHashValue(uv + vec2(0.0, h));

vec2 final_derivatives = vec2(val_x - main_intensity, val_y - main_intensity) * (1.0 / h);

// Calculamos el vector normal final en espacio tangente
vec3 final_normal = normalize(vec3(-final_derivatives.x, -final_derivatives.y, 1.0));

// --- INVERSIÓN FINAL (Invert) ---
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