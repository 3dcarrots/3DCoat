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
// CONTROLES ADICIONALES (Leídos dinámicamente, Offset y Tiempo removidos)
// ============================================================================
in float Scale(value = 1.0, min = 0.1, max = 10.0); // Multiplicador de escala
in float Worminess(value = 2.0, min = 1.0, max = 10.0); // Factor de onda (6.0 para aspecto gusano/worm)
in float DistortIntensity(value = 0.0, min = 0.0, max = 5.0); // Intensidad de la distorsión
in float DistortScale(value = 2.0, min = 0.1, max = 10.0); // Escala de la deformación
in float Bright(value = 0.0, min = -1.0, max = 1.0); // Offset de luminancia (Baseline)
in float Contrast(value = 1.0, min = 0.0, max = 5.0); // Contraste general

// ============================================================================
// FUNCIONES AUXILIARES
// ============================================================================

// Hash de vectores de dirección de onda con tipado explícito de flotantes
vec2 g( vec2 n ) { 
    return sin(n.x * n.y * vec2(12.0, 17.0) + vec2(1.0, 2.0)); 
}

// Algoritmo de Ruido de Ondas 2D de Iñigo Quílez con factor Worminess dinámico
float noise(vec2 p)
{
    vec2 i = floor(p);
    vec2 f = fract(p);
    f = f * f * (3.0 - 2.0 * f);
    
    // Suma e interpolación trigonométrica de frentes de onda en el espacio
    return mix(mix(sin(Worminess * dot(p, g(i))),
                   sin(Worminess * dot(p, g(i + vec2(1.0, 0.0)))), f.x),
               mix(sin(Worminess * dot(p, g(i + vec2(0.0, 1.0)))),
                   sin(Worminess * dot(p, g(i + vec2(1.0, 1.0)))), f.x), f.y);
}

// Combinación fractal FBM de 3 Octavas usando la lógica de ondas (Wave FBM)
float fbm(vec2 p) {
    mat2 m = mat2( 1.6,  1.2, -1.2,  1.6 );
    float f  = 0.5000 * noise(p); p = m * p;
    f += 0.2500 * noise(p); p = m * p;
    f += 0.1250 * noise(p);
    return f / 0.8750; // Normalización analítica al rango [-1, 1]
}

// Retorna el valor final aplicando compensación de brillo, contraste y Sharpness
float getWaveValue(vec2 P) {
    float rawNoise = fbm(P);
    
    // Remapeamos el rango [-1, 1] al rango estándar [0, 1] para máscaras
    float noiseVal = rawNoise * 0.5 + 0.5;
    
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

// Coordenadas UV directas (Offset removido)
vec2 uv = UVCoord;

// Aplicamos la repetición global multiplicando la frecuencia ingresada por 10.0 (escala real x10)
float globalScale = (Frequency * 10.0) * Scale;
uv *= globalScale;

// --- DOMAIN WARPING (DISTORTION EN RUIDO DE ONDAS) ---
if (DistortIntensity > 0.001) {
    vec2 distort_uv = uv * DistortScale;
    // Utilizamos el ruido base para distorsionar su propio espacio de forma orgánica
    vec2 distort = vec2(fbm(distort_uv), fbm(distort_uv + vec2(31.415, 57.123)));
    uv += (distort - vec2(0.5)) * DistortIntensity;
}

// --- EVALUACIÓN DE VALUE NOISE ---
float main_intensity = getWaveValue(uv);

// Cálculo de normales dinámicas por diferencias finitas centrales de alta fidelidad
float h = 0.002; // Paso de muestreo óptimo
float val_x = getWaveValue(uv + vec2(h, 0.0));
float val_y = getWaveValue(uv + vec2(0.0, h));

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