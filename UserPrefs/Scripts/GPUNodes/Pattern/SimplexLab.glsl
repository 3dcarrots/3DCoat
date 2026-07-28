// ============================================================================
// CONFIGURACIÓN DE NODOS EN 3DCOAT (NGL)
// ============================================================================
in vec2 UVCoord(knot = ioUV); // UV Coord de entrada

// Menú desplegable oficial consolidado libre de patrones duplicados matemáticamente
#enum Pattern Average Quadratic Max Min Harmonic

// Parámetros con límites estandarizados y valores por defecto normalizados según tus especificaciones
in float Luminance(value = 1.0, min = 0.1, max = 2.0); // Luminance (Internamente multiplicada por 1.15)
in float Midtones(value = 1.0, min = 0.1, max = 1.0);   // Midtones (Gamma - Internamente multiplicada por 1.15)
in float Shadows(value = 0.1, min = 0.1, max = 1.0);    // Shadows (Nivel de negro - Internamente multiplicada por 0.15)
in float Scale(value = 1.0, min = 0.1, max = 10.0);     // Scale (Escala global - multiplicada internamente por 0.1)
in float Size_X(value = 1.0, min = 1.0, max = 10.0);    // Size X (multiplicada internamente por 0.1)
in float Size_Y(value = 1.0, min = 0.1, max = 10.0);    // Size Y (multiplicada internamente por 0.1)
in float DistortIntensity(value = 0.0, min = 0.0, max = 5.0); // Distort Intensity
in float DistortScale(value = 1.0, min = 0.1, max = 10.0); // Distort Scale
in float Contrast(value = 1.0, min = 0.0, max = 2.0);   // Contrast (Internamente multiplicada por 0.3)

// ============================================================================
// SALIDAS ÚNICAS (Únicos conectores visibles en el Node Editor)
// ============================================================================
out vec3 Color;       // Salida RGB (Ruido en escala de grises puro)
out vec3 Normal;      // Vector normal en espacio tangente (Relieve limpio)
out float NonColor;   // Patrón procedural seleccionado en escala de grises
out float Opacity;    // Máscara de opacidad para el patrón seleccionado

// ============================================================================
// FUNCIONES AUXILIARES DE RUIDO (Totalmente optimizadas y con tipos estrictos)
// ============================================================================

vec2 hash2(vec2 p) {
    return fract(sin(p * mat2(127.1, 311.7, 269.5, 183.3)) * 43758.5453123);
}

vec2 shash(vec2 p) {
    return 2.0 * hash2(p) - 1.0;
}

vec3 snoise( vec2 p ) {
    float K1 = 0.366025404; // (sqrt(3)-1)/2
    float K2 = 0.211324865; // (3-sqrt(3))/6

	vec2  i = floor( p + (p.x+p.y)*K1 );
    vec2  a = p - i + (i.x+i.y)*K2;
    vec2  o = step( a.yx, a );
    vec2  b = a - o  + K2;
	vec2  c = a - 1.0 + 2.0*K2;
    
    vec3  h = max( 0.5 - vec3( dot(a,a), dot(b,b), dot(c,c) ), 0.0 );
    vec3  n = h*h*h*h * vec3( dot(a, shash(i   )),   
                              dot(b, shash(i+o )),   
                              dot(c, shash(i+1.0)) ); 
    return 70.0 * n;
}

// Función de distorsión para el espacio de coordenadas
float baseNoise(vec2 p) {
    vec2 i = floor(p);
    vec2 f = fract(p);
    f = f * f * (3.0 - 2.0 * f);
    float a = fract(sin(dot(i, vec2(127.1, 311.7))) * 43758.545);
    float b = fract(sin(dot(i + vec2(1.0, 0.0), vec2(127.1, 311.7))) * 43758.545);
    float c = fract(sin(dot(i + vec2(0.0, 1.0), vec2(127.1, 311.7))) * 43758.545);
    float d = fract(sin(dot(i + vec2(1.0, 1.0), vec2(127.1, 311.7))) * 43758.545);
    return mix(mix(a, b, f.x), mix(c, d, f.x), f.y);
}

// ============================================================================
// PROCESAMIENTO DE SEÑAL Y COORDENADAS
// ============================================================================

// Calcula las coordenadas aplicando la atenuación de escala 0.1x de forma interna y compensada
vec2 getCoords(vec2 uv_val) {
    float internal_scale = Scale * 0.1;
    float internal_size_x = Size_X * 0.1;
    float internal_size_y = Size_Y * 0.1;

    // Multiplicamos por 10.0 de forma interna para compensar la atenuación de 0.1x y mantener la proporción idónea
    float fx = (internal_size_x * 10.0) * (internal_scale * 10.0) * 5.6;
    float fy = (internal_size_y * 10.0) * (internal_scale * 10.0) * 5.6;
    vec2 p = vec2(uv_val.x * fx, uv_val.y * fy);

    // Domain Warping / Distorsión espacial
    if (DistortIntensity > 0.001) {
        vec2 distort_p = p * DistortScale;
        vec2 distort = vec2(baseNoise(distort_p), baseNoise(distort_p + vec2(13.7, 31.4))) - 0.5;
        p += distort * DistortIntensity;
    }
    return p;
}

// Procesa el contraste, compresión de domo, sombras, medios tonos y ganancia
float processNoiseValue(float rawVal) {
    // 1. Contrast calibrado de forma no destructiva (Contrast visual * 0.3)
    float internal_contrast = Contrast * 0.3;
    float adjustedRaw = max(0.0, rawVal * internal_contrast);
    
    // 2. Compresión exponencial de domo suave (evita que los picos se recorten en plano)
    float compressed = 1.0 - exp(-1.2 * adjustedRaw);
    
    // 3. Shadows calibrado con clamp de seguridad (Shadows visual * 0.15)
    float internal_shadows = Shadows * 0.15;
    float s = clamp(internal_shadows, 0.0, 0.95);
    float shadowed = max(0.0, compressed - s) / (1.0 - s);
    
    // 4. Midtones calibrado (Midtones visual * 1.15)
    float internal_midtones = Midtones * 1.15;
    float m = max(0.05, internal_midtones);
    float gammaApplied = pow(shadowed, 1.0 / m);
    
    // 5. Luminancia calibrada a su valor de escala dinámico (Luminance visual * 1.15)
    float internal_luminance = Luminance * 1.15;
    float final_val = clamp(gammaApplied * internal_luminance, 0.0, 1.0);
    
    return final_val;
}

// Evalúa y retorna el valor de ruido final de alta calidad en escala de grises
float getSample(vec2 uv_coord) {
    vec2 p = getCoords(uv_coord);
    
    // Fijado abs() de forma global para un comportamiento de ruido absoluto detallado
    vec3 n = abs(snoise(2.0 * p));
    vec3 s = n;
    
    // Algoritmo de ordenamiento nativo de componentes de Inigo Quilez
    s = (s.y <= min(s.x, s.z)) ? s.yxz : ((s.z < min(s.x, s.y)) ? s.zxy : s);
    s = (s.z < s.y) ? s.xzy : s;
    
    float val = 0.0;
    
    // Selección por preprocesador plano compatible con 3DCoat
    #ifdef Pattern_Average
        val = n.x + n.y + n.z; // Ruido simplex clásico (Promedio estándar)
    #endif
    #ifdef Pattern_Quadratic
        val = length(n); // Suma cuadrática
    #endif
    #ifdef Pattern_Max
        val = s.z + 0.1; // Componente máxima
    #endif
    #ifdef Pattern_Min
        val = s.x; // Componente mínima
    #endif
    #ifdef Pattern_Harmonic
        float v = n.x * n.y * n.z;
        val = 8.0 * sign(v) * pow(abs(v), 1.0 / 3.0); // Promedio armónico
    #endif
    
    return processNoiseValue(val);
}

// Muestreo dinámico ultra-rápido para el relieve de normales desplazadas (Lag-Free)
float getSampleLight(vec2 uv_coord) {
    vec2 p = getCoords(uv_coord);
    vec3 n = abs(snoise(2.0 * p));
    
    float val = (n.x + n.y + n.z) * 0.5;
    
    return processNoiseValue(val);
}

// ============================================================================
// EJECUCIÓN PRINCIPAL
// ============================================================================

void main() {
    // --- EVALUACIÓN DE INTENSIDAD PROCEDURAL (Calidad Completa) ---
    float main_intensity = getSample(UVCoord);

    // Muestreo dinámico por diferencias finitas centrales para cálculo de relieve (Lag-Free)
    float h = 0.002; 
    float val_x = getSampleLight(UVCoord + vec2(h, 0.0));
    float val_y = getSampleLight(UVCoord + vec2(0.0, h));

    vec2 final_derivatives = vec2(val_x - main_intensity, val_y - main_intensity) * (1.0 / h);
    vec3 final_normal = normalize(vec3(-final_derivatives.x, -final_derivatives.y, 1.0));

    // --- ASIGNACIÓN DE SALIDAS ESTÁNDAR ÚNICAS ---
    Color = vec3(main_intensity); // Salida RGB en escala de grises limpia y libre de color
    Normal = final_normal;
    NonColor = main_intensity;
    Opacity = main_intensity;
}