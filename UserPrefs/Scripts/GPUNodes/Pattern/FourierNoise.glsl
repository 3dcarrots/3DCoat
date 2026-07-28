// ============================================================================
// CONFIGURACIÓN DE NODOS EN 3DCOAT (NGL)
// ============================================================================
in vec2 UVCoord(knot = ioUV); // UV Coord de entrada

// Deslizadores de apariencia y escala estandarizados
in float Luminance(value = 0.8, min = 0.1, max = 10.0); // Luminance
in float Midtones(value = 1.0, min = 0.1, max = 3.0);   // Midtones (Gamma)
in float Shadows(value = 0.0, min = 0.0, max = 2.0);    // Shadows (Nivel de negro)
in float Scale(value = 1.0, min = 0.1, max = 20.0);     // Scale (Escala global - Internamente multiplicada por 5)
in float Size_X(value = 0.1, min = 0.1, max = 10.0);    // Size X
in float Size_Y(value = 0.1, min = 0.1, max = 10.0);    // Size Y
in float DistortIntensity(value = 0.0, min = 0.0, max = 5.0); // Distort Intensity (Warp de Fourier)
in float DistortScale(value = 1.0, min = 0.1, max = 10.0); // Distort Scale
in float Contrast(value = 1.0, min = 0.0, max = 5.0);   // Contrast

// ============================================================================
// SALIDAS ÚNICAS (Únicos conectores visibles en el Node Editor)
// ============================================================================
out vec3 Color;       // Salida RGB (Ruido en escala de grises puro)
out vec3 Normal;      // Vector normal en espacio tangente (Relieve limpio)
out float NonColor;   // Patrón procedural seleccionado en escala de grises
out float Opacity;    // Máscara de opacidad para el patrón seleccionado

// ============================================================================
// SISTEMA DE SÍNTESIS ESPECTRAL DE FOURIER (Cero bucles pesados)
// ============================================================================

// Función de ruido base para el Domain Warping del espacio espectral
float hash(vec2 p) {
    vec3 p3 = fract(vec3(p.xyx) * 0.1031);
    p3 += dot(p3, p3.yzx + 33.33);
    return fract((p3.x + p3.y) * p3.z);
}

float baseNoise(vec2 p) {
    vec2 i = floor(p);
    vec2 f = fract(p);
    f = f * f * (3.0 - 2.0 * f);
    float a = hash(i);
    float b = hash(i + vec2(1.0, 0.0));
    float c = hash(i + vec2(0.0, 1.0));
    float d = hash(i + vec2(1.0, 1.0));
    return mix(mix(a, b, f.x), mix(c, d, f.x), f.y);
}

// Síntesis Espectral de Fourier por anillo de frecuencias (12 ondas isotrópicas)
float fourierNoise(vec2 p) {
    float sum = 0.0;
    float totAmp = 0.0;
    
    // Sumamos 12 ondas orientadas de forma equidistante en el círculo unitario espectral
    const int N = 12;
    for (int i = 0; i < N; i++) {
        float angle = float(i) * (3.14159265 / float(N));
        vec2 k = vec2(cos(angle), sin(angle));
        
        // Fase determinista aleatoria para cada dirección de onda
        float phase = fract(sin(float(i) * 45.123) * 43758.545) * 6.28318;
        
        // Modulación sutil de frecuencia para evitar patrones de muaré rígidos
        float freqRand = 1.0 + 0.15 * sin(float(i) * 17.89);
        
        sum += cos(dot(p * freqRand, k) + phase);
        totAmp += 1.0;
    }
    
    return (sum / totAmp) * 0.5 + 0.5; // Normalizado a [0, 1]
}

// Combinación fractal espectral de Fourier de 2 octavas fijas
float fourierFractal(vec2 p) {
    float n1 = fourierNoise(p);
    float n2 = fourierNoise(p * 2.5);
    return n1 * 0.7 + n2 * 0.3;
}

// ============================================================================
// PROCESAMIENTO DE SEÑAL Y COORDENADAS
// ============================================================================

// Calcula las coordenadas espectrales aplicando escala y distorsión de espacio
vec2 getCoords(vec2 uv_val) {
    // Escala interna multiplicada por 5.0 para que el valor de inicio (1.0) equivalga visualmente a 5.0
    float internal_scale = Scale * 5.0;
    
    float fx = (Size_X * 10.0) * internal_scale * 5.6;
    float fy = (Size_Y * 10.0) * internal_scale * 5.6;
    vec2 p = vec2(uv_val.x * fx, uv_val.y * fy);

    // Domain Warping / Distorsión espacial sobre las coordenadas del espectro
    if (DistortIntensity > 0.001) {
        vec2 distort_p = p * DistortScale;
        vec2 distort = vec2(baseNoise(distort_p), baseNoise(distort_p + vec2(13.7, 31.4))) - 0.5;
        p += distort * DistortIntensity;
    }
    return p;
}

// Procesa la señal aplicando Contrast, Shadows, Midtones y Luminance
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

// Evalúa y retorna el valor de ruido de Fourier fractal completo (Color, NonColor, Opacity)
float getSample(vec2 uv_coord) {
    vec2 p = getCoords(uv_coord);
    float n = fourierFractal(p * 2.0);
    return processNoiseValue(n);
}

// Evalúa y retorna el valor de ruido de Fourier simplificado de 1 octava (Normales rápidas)
float getSampleLight(vec2 uv_coord) {
    vec2 p = getCoords(uv_coord);
    float n = fourierNoise(p * 2.0);
    return processNoiseValue(n);
}

// ============================================================================
// EJECUCIÓN PRINCIPAL
// ============================================================================

void main() {
    // --- EVALUACIÓN DE INTENSIDAD PROCEDURAL ---
    float main_intensity = getSample(UVCoord);

    // Muestreo dinámico por diferencias finitas centrales para cálculo de relieve (Lag-Free)
    float h = 0.002; 
    float val_x = getSampleLight(UVCoord + vec2(h, 0.0));
    float val_y = getSampleLight(UVCoord + vec2(0.0, h));

    vec2 final_derivatives = vec2(val_x - main_intensity, val_y - main_intensity) * (1.0 / h);
    vec3 final_normal = normalize(vec3(-final_derivatives.x, -final_derivatives.y, 1.0));

    // --- ASIGNACIÓN DE SALIDAS ESTÁNDAR ÚNICAS ---
    Color = vec3(main_intensity); // Salida en escala de grises libre de color
    Normal = final_normal;
    NonColor = main_intensity;
    Opacity = main_intensity;
}