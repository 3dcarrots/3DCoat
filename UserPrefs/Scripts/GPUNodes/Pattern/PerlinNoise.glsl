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

// Sobrecargas de modulación seguras y tipificadas vectorialmente para evitar cuelgues
vec4 permute(vec4 x) {
    return mod(((x * 34.0) + vec4(1.0)) * x, vec4(289.0));
}

vec2 fade(vec2 t) {
    return t * t * t * (t * (t * 6.0 - vec2(15.0)) + vec2(10.0));
}

// Algoritmo de Ruido de Perlin Clásico 2D (cnoise) de Stefan Gustavson (Con tipado estricto)
float cnoise(vec2 P) {
    vec4 Pi = floor(P.xyxy) + vec4(0.0, 0.0, 1.0, 1.0);
    vec4 Pf = fract(P.xyxy) - vec4(0.0, 0.0, 1.0, 1.0);
    Pi = mod(Pi, vec4(289.0)); // Tipificación estricta de modulo en GPU
    vec4 ix = Pi.xzxz;
    vec4 iy = Pi.yyww;
    vec4 fx = Pf.xzxz;
    vec4 fy = Pf.yyww;
    
    vec4 i = permute(permute(ix) + iy);
    
    vec4 gx = 2.0 * fract(i * 0.0243902439) - vec4(1.0); // 1/41 = 0.02439...
    vec4 gy = abs(gx) - vec4(0.5);
    vec4 tx = floor(gx + vec4(0.5));
    gx = gx - tx;
    
    vec2 g00 = vec2(gx.x, gy.x);
    vec2 g10 = vec2(gx.y, gy.y);
    vec2 g01 = vec2(gx.z, gy.z);
    vec2 g11 = vec2(gx.w, gy.w);
    
    vec4 norm = vec4(1.79284291400159) - vec4(0.85373472095314) * vec4(
        dot(g00, g00), dot(g10, g10), dot(g01, g01), dot(g11, g11)
    );
    g00 *= norm.x;
    g10 *= norm.y;
    g01 *= norm.z;
    g11 *= norm.w;
    
    float n00 = dot(g00, vec2(fx.x, fy.x));
    float n10 = dot(g10, vec2(fx.y, fy.y));
    float n01 = dot(g01, vec2(fx.z, fy.z));
    float n11 = dot(g11, vec2(fx.w, fy.w));
    
    vec2 fade_xy = fade(Pf.xy);
    vec2 n_x = mix(vec2(n00, n01), vec2(n10, n11), fade_xy.x);
    float n_xy = mix(n_x.x, n_x.y, fade_xy.y);
    return 2.3 * n_xy;
}

// Retorna el valor final aplicando compensación de brillo, contraste y Sharpness
float getPerlinValue(vec2 P) {
    float rawNoise = cnoise(P);
    
    // Remapeamos el rango [-1, 1] al rango estándar [0, 1] para máscaras
    float noiseVal = rawNoise * 0.5 + 0.5;
    
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

// Coordenadas UV de entrada directas (Offset removido)
vec2 uv = UVCoord;

// Aplicamos la repetición global multiplicando la frecuencia ingresada por 10.0 (escala real x10)
float globalScale = (Frequency * 10.0) * Scale;
uv *= globalScale;

// --- DOMAIN WARPING (DISTORTION EN PERLIN) ---
if (DistortIntensity > 0.001) {
    vec2 distort_uv = uv * DistortScale;
    // Utilizamos el ruido clásico para distorsionar su propio espacio de forma orgánica
    vec2 distort = vec2(cnoise(distort_uv), cnoise(distort_uv + vec2(31.415, 57.123)));
    // Corrección: Resta explícita de vectores para compatibilidad total
    uv += (distort - vec2(0.5)) * DistortIntensity;
}

// --- EVALUACIÓN DE VALUE NOISE ---
float main_intensity = getPerlinValue(uv);

// Cálculo de derivadas numéricas dinámicas usando diferencias finitas centrales de alta fidelidad
float h = 0.002; // Paso de muestreo óptimo
float val_x = getPerlinValue(uv + vec2(h, 0.0));
float val_y = getPerlinValue(uv + vec2(0.0, h));

vec2 final_derivatives = vec2(val_x - main_intensity, val_y - main_intensity) * (1.0 / h);

// Calculamos el vector normal final en espacio tangente
vec3 final_normal = normalize(vec3(-final_derivatives.x, -final_derivatives.y, 1.0));

// --- INVERSIÓN FINAL (Invert) ---
// Corrección: Uso estricto de #ifdef para evitar cuelgues del preprocesador
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