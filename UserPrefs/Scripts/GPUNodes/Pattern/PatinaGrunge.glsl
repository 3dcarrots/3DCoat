// ============================================================================
// CONFIGURACIÓN DE NODOS EN 3DCOAT (NGL)
// ============================================================================
in vec2 UVCoord(knot = ioUV); // UV Coord de entrada

// Deslizadores de apariencia y escala en tu orden preferido (Scale_Z y Seed eliminados)
in float Luminance(value = 0.8, min = 0.1, max = 10.0); // Luminance
in float Midtones(value = 1.0, min = 0.1, max = 3.0);   // Midtones (Gamma)
in float Shadows(value = 0.0, min = 0.0, max = 2.0);    // Shadows (Nivel de negro)
in float Scale(value = 1.0, min = 0.1, max = 20.0);     // Scale (Escala global)
in float Size_X(value = 0.1, min = 0.1, max = 10.0);    // Size X
in float Size_Y(value = 0.1, min = 0.1, max = 10.0);    // Size Y
in float DistortIntensity(value = 1.0, min = 0.0, max = 5.0); // Distort Intensity
in float DistortScale(value = 1.0, min = 0.1, max = 10.0); // Distort Scale
in float Contrast(value = 1.0, min = 0.0, max = 5.0);   // Contrast

// ============================================================================
// SALIDAS ÚNICAS (Únicos conectores visibles en el Node Editor)
// ============================================================================
out vec3 Color;       // Salida RGB (Ruido en escala de grises puro)
out vec3 Normal;      // Vector normal en espacio tangente (Para dar relieve físico)
out float NonColor;   // Patrón procedural seleccionado en escala de grises
out float Opacity;    // Máscara de opacidad para el patrón seleccionado

// ============================================================================
// FUNCIONES AUXILIARES DE RUIDO TOTALMENTE PLANAS (Cero bucles)
// ============================================================================

float hash(vec2 p) {
    vec3 p3 = fract(vec3(p.xyx) * 0.1031);
    p3 += dot(p3, p3.yzx + 33.33);
    return fract((p3.x + p3.y) * p3.z);
}

float noise(vec2 p) {
    vec2 i = floor(p);
    vec2 f = fract(p);
    f = f * f * (3.0 - 2.0 * f);
    float a = hash(i);
    float b = hash(i + vec2(1.0, 0.0));
    float c = hash(i + vec2(0.0, 1.0));
    float d = hash(i + vec2(1.0, 1.0));
    return mix(mix(a, b, f.x), mix(c, d, f.x), f.y);
}

// FBM Aplanado de 4 Octavas fijas para calidad completa sin bucles
float fbm_flat(vec2 p) {
    float val = 0.0;
    // Octava 1
    val += 0.5 * noise(p);
    // Octava 2
    val += 0.275 * noise(p * 3.0);
    // Octava 3
    val += 0.15125 * noise(p * 9.0);
    // Octava 4
    val += 0.0831875 * noise(p * 27.0);
    return val;
}

// FBM Aplanado de 2 Octavas para el cálculo de normales ultra-rápido
float fbm_oct2(vec2 p) {
    float val = 0.0;
    val += 0.5 * noise(p);
    val += 0.275 * noise(p * 3.0);
    return val;
}

// Algoritmo de Domain Warping adaptado para controlar distorsión y escala de forma nativa
float warp(vec2 p) {
    vec2 q = vec2(
        fbm_flat(p),
        fbm_flat(p + vec2(5.2, 1.3))
    );
    vec2 r = vec2(
        fbm_flat(p * DistortScale + (4.0 * DistortIntensity) * q + vec2(1.7, 9.2)),
        fbm_flat(p * DistortScale + (4.0 * DistortIntensity) * q + vec2(8.3, 2.8))
    );
    return fbm_flat(p + (10.0 * DistortIntensity) * r);
}

// ============================================================================
// PROCESAMIENTO DE SEÑAL Y COORDENADAS
// ============================================================================

// Calcula las coordenadas con el factor de escala visual de 3DCoat
vec2 getCoords(vec2 uv_val) {
    float fx = (Size_X * 10.0) * Scale;
    float fy = (Size_Y * 10.0) * Scale;
    return vec2(uv_val.x * fx, uv_val.y * fy);
}

// Procesa el contraste, compresión de domo, sombras, medios tonos y ganancia
float processNoiseValue(float rawVal) {
    // 1. Contrast aplicado de forma no destructiva al valor de entrada
    float adjustedRaw = max(0.0, rawVal * Contrast);
    
    // 2. Compresión exponencial de domo suave (evita que los picos se recorten en plano)
    float compressed = 1.0 - exp(-1.2 * adjustedRaw);
    
    // 3. Shadows (frecuencias oscuras / nivel de negro - con clamp de seguridad)
    float s = clamp(Shadows, 0.0, 0.95);
    float shadowed = max(0.0, compressed - s) / (1.0 - s);
    
    // 4. Midtones (frecuencias medias / contraste por Gamma)
    float m = max(0.05, Midtones);
    float gammaApplied = pow(shadowed, 1.0 / m);
    
    // 5. Luminancia aplicando internamente el multiplicador de 1.2
    float internal_luminance = Luminance * 1.2;
    float final_val = clamp(gammaApplied * internal_luminance, 0.0, 1.0);
    
    return final_val;
}

// Evalúa y retorna el valor de ruido final en calidad completa para Color, NonColor y Opacity
float getSample(vec2 uv_coord) {
    vec2 vUv = getCoords(uv_coord);
    vec2 p = vUv * 3.0 - 1.5;
    
    // Generación del patrón principal de pátina
    float n = warp(p);
    float n2 = fbm_flat(p * 1.5 + vec2(n * 0.5));
    float density = n * 0.7 + n2 * 0.3;
    
    // Generación de grano fino estático de forma analítica
    float g = hash(uv_coord * 4096.0) - 0.5;
    float finalNoise = density + g * 0.08;
    
    return processNoiseValue(finalNoise);
}

// Evalúa una versión ultra-rápida y limpia para el cálculo de normales desplazadas (Lag-Free)
float getSampleLight(vec2 uv_coord) {
    vec2 vUv = getCoords(uv_coord);
    vec2 p = vUv * 3.0 - 1.5;
    
    // Evaluamos una octava simple de FBM para calcular la dirección de las normales de forma instantánea
    float n = fbm_oct2(p);
    
    return processNoiseValue(n);
}

// ============================================================================
// EJECUCIÓN PRINCIPAL
// ============================================================================

void main() {
    // --- EVALUACIÓN DE INTENSIDAD PROCEDURAL (Calidad Completa) ---
    float main_intensity = getSample(UVCoord);

    // Muestreo dinámico por diferencias finitas centrales de alta velocidad (Evita retrasos al arrastrar el ratón)
    float h = 0.002; 
    float val_x = getSampleLight(UVCoord + vec2(h, 0.0));
    float val_y = getSampleLight(UVCoord + vec2(0.0, h));

    vec2 final_derivatives = vec2(val_x - main_intensity, val_y - main_intensity) * (1.0 / h);
    vec3 final_normal = normalize(vec3(-final_derivatives.x, -final_derivatives.y, 1.0));

    // --- ASIGNACIÓN DE SALIDAS ESTÁNDAR ÚNICAS ---
    Color = vec3(main_intensity); // Salida en escala de grises limpia libre de tintes marrones
    Normal = final_normal;
    NonColor = main_intensity;
    Opacity = main_intensity;
}