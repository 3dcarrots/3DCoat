// ============================================================================
// CONFIGURACIÓN DE NODOS EN 3DCOAT (NGL)
// ============================================================================
in vec2 UVCoord(knot = ioUV); // UV Coord de entrada

// Menú desplegable oficial y exclusivo para las 3 variaciones de este sombreador
#enum Pattern Worms Cells Intestines

// Parámetros con límites estandarizados y valores por defecto calibrados para tu esfera
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
out vec3 Normal;      // Vector normal en espacio tangente (Relieve limpio)
out float NonColor;   // Patrón procedural seleccionado en escala de grises
out float Opacity;    // Máscara de opacidad para el patrón seleccionado

// ============================================================================
// FUNCIONES AUXILIARES DE RUIDO SIMPLEX 2D (Originales de tu archivo)
// ============================================================================

vec2 hash( vec2 p ) 
{
	p = vec2( dot(p,vec2(127.1,311.7)), dot(p,vec2(269.5,183.3)) );
	p = -1.0 + 2.0*fract(sin(p)*43758.5453123);
    return p;
}

vec3 snoise( in vec2 p )
{
    const float K1 = 0.366025404; // (sqrt(3)-1)/2;
    const float K2 = 0.211324865; // (3-sqrt(3))/6;

	vec2  i = floor( p + (p.x+p.y)*K1 );
    vec2  a = p - i + (i.x+i.y)*K2;
    float m = step(a.y,a.x); 
    vec2  o = vec2(m,1.0-m);
    vec2  b = a - o + K2;
	vec2  c = a - 1.0 + 2.0*K2;
    vec3  h = max( 0.5-vec3(dot(a,a), dot(b,b), dot(c,c) ), 0.0 );
	vec3  n = h*h*h*h*vec3( dot(a,hash(i+0.0)), dot(b,hash(i+o)), dot(c,hash(i+1.0)));
    return 1e2*n; 
}

// ============================================================================
// PROCESAMIENTO DE SEÑAL Y COORDENADAS
// ============================================================================

// Calcula las coordenadas aplicando la escala global y la calibración de frecuencia compensada (5.6x)
vec2 getCoords(vec2 uv_val) {
    float fx = (Size_X * 10.0) * Scale * 5.6;
    float fy = (Size_Y * 10.0) * Scale * 5.6;
    vec2 p = vec2(uv_val.x * fx, uv_val.y * fy);

    // Domain Warping / Distorsión espacial
    if (DistortIntensity > 0.001) {
        vec2 distort_p = p * DistortScale;
        vec2 distort = snoise(distort_p).xy;
        p += distort * DistortIntensity;
    }
    return p;
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
    
    // 5. Ganancia de luminancia interna calibrada (Luminance * 3.0) para un contraste óptimo
    float internal_luminance = Luminance * 3.0;
    float final_val = clamp(gammaApplied * internal_luminance, 0.0, 1.0);
    
    return final_val;
}

// Evalúa y retorna el valor de ruido final en calidad completa según la variación seleccionada
float getSample(vec2 uv_coord) {
    vec2 p = getCoords(uv_coord);
    
    vec3 n = snoise(6.0 * p);
    vec3 an = abs(n);
    vec4 s = vec4(
        dot(n, vec3(1.0)),
        dot(an, vec3(1.0)),
        length(n),
        max(max(an.x, an.y), an.z)
    );
    
    // Calibración exacta para que Luminance = 0.8 equivalga a un grosor de línea óptimo (t = 0.625)
    float t = max(0.001, Luminance * 0.78125);
    
    // Inicialización por defecto (Patrón Worms)
    float x = 1.25 * (s.y * t - abs(s.x)) / t;
    
    // Selección plana nativa de 3DCoat
    #ifdef Pattern_Cells
        x = (1.0 - t) + (s.y - s.w / t) * t;
        x *= 1.0 + t;
        x *= x;
    #endif
    #ifdef Pattern_Intestines
        x = 0.75 * s.y;
    #endif
    
    return processNoiseValue(x);
}

// Muestreo simplificado y fluido para el mapa de normales desplazadas (Lag-Free)
float getSampleLight(vec2 uv_coord) {
    vec2 p = getCoords(uv_coord);
    vec3 n = snoise(6.0 * p);
    float x = 0.75 * dot(abs(n), vec3(1.0));
    return processNoiseValue(x);
}

// ============================================================================
// EJECUCIÓN PRINCIPAL
// ============================================================================

void main() {
    // --- EVALUACIÓN DE LAS VARIACIONES COMO VARIABLES LOCALES (Oculta sus pines de salida) ---
    vec2 p = getCoords(UVCoord);
    
    vec3 n = snoise(6.0 * p);
    vec3 an = abs(n);
    vec4 s = vec4(
        dot(n, vec3(1.0)),
        dot(an, vec3(1.0)),
        length(n),
        max(max(an.x, an.y), an.z)
    );
    
    float t = max(0.001, Luminance * 0.78125);

    // Calculamos las opciones locales
    float x_Worms = 1.25 * (s.y * t - abs(s.x)) / t;
    
    float x_Cells = (1.0 - t) + (s.y - s.w / t) * t;
    x_Cells *= 1.0 + t;
    x_Cells *= x_Cells;
    
    float x_Intestines = 0.75 * s.y;

    float l_Worms      = processNoiseValue(x_Worms);
    float l_Cells      = processNoiseValue(x_Cells);
    float l_Intestines = processNoiseValue(x_Intestines);

    // --- SELECCIÓN DE LA INTENSIDAD PRINCIPAL SEGÚN EL ENUM OFICIAL CORREGIDO ---
    float main_intensity = l_Worms; // Valor por defecto

    #ifdef Pattern_Cells
        main_intensity = l_Cells;
    #endif
    #ifdef Pattern_Intestines
        main_intensity = l_Intestines;
    #endif

    // Muestreo dinámico por diferencias finitas centrales para cálculo de relieve
    float h = 0.002; 
    float val_x = getSampleLight(UVCoord + vec2(h, 0.0));
    float val_y = getSampleLight(UVCoord + vec2(0.0, h));

    vec2 final_derivatives = vec2(val_x - main_intensity, val_y - main_intensity) * (1.0 / h);
    vec3 final_normal = normalize(vec3(-final_derivatives.x, -final_derivatives.y, 1.0));

    // --- ASIGNACIÓN DE SALIDAS ESTÁNDAR ÚNICAS ---
    Color = vec3(main_intensity); // Salida de grises estándar calibrada
    Normal = final_normal;
    NonColor = main_intensity;
    Opacity = main_intensity;
}