// ============================================================================
// CONFIGURACIÓN DE NODOS EN 3DCOAT (NGL)
// ============================================================================
in vec2 UVCoord(knot = ioUV); // UV Coord de entrada

// Menú desplegable nativo para seleccionar la variación del fluido de ruido
#enum Pattern Base Flame Cloud

// Parámetros con límites estandarizados y escala multiplicada (con deslizador de corriente Flow)
in float Luminance(value = 0.8, min = 0.1, max = 10.0); // Luminance
in float Midtones(value = 1.0, min = 0.1, max = 3.0);   // Midtones (Gamma)
in float Shadows(value = 0.0, min = 0.0, max = 2.0);    // Shadows (Nivel de negro)
in float Scale(value = 1.0, min = 0.1, max = 5.0);     // Scale (Escala global - multiplicada por 0.1)
in float Size_X(value = 1.0, min = 1.0, max = 5.0);    // Size X (multiplicado por 0.1)
in float Size_Y(value = 1.0, min = 1.0, max = 5.0);    // Size Y (multiplicado por 0.1)
in float DistortIntensity(value = 0.0, min = 0.0, max = 5.0); // Distort Intensity
in float DistortScale(value = 1.0, min = 0.1, max = 10.0); // Distort Scale
in float Contrast(value = 1.0, min = 0.0, max = 5.0);   // Contrast
in float Flow(value = 0.0, min = 0.0, max = 10.0);      // Flow (Desplaza y hace rotar la corriente del fluido)

// ============================================================================
// SALIDAS ÚNICAS (Únicos conectores visibles en el Node Editor)
// ============================================================================
out vec3 Color;       // Salida RGB (Ruido en escala de grises puro)
out vec3 Normal;      // Vector normal en espacio tangente (Relieve limpio)
out float NonColor;   // Patrón procedural seleccionado en escala de grises
out float Opacity;    // Máscara de opacidad para el patrón seleccionado

// ============================================================================
// FUNCIONES AUXILIARES DE FLUJO (Optimizado eliminando exponentes dinámicos)
// ============================================================================

vec2 hash( vec2 p )
{
	p = vec2( dot(p,vec2(127.1,311.7)),
			  dot(p,vec2(269.5,183.3)) );

	return -1.0 + 2.0*fract(sin(p)*43758.5453123);
}

// Función auxiliar de distorsión para el espacio de coordenadas
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

// Flow Noise: Rota los gradientes de Perlin con velocidad precalculada para rendimiento óptimo
float flow_noise( vec2 p, float speedMult )
{
    vec2 i = floor( p );
    vec2 f = fract( p );
	
	vec2 u = f*f*(3.0-2.0*f);
    
    // speedMult elimina el costo pesado de pow(2.0, lvl) en la GPU
    float t = speedMult * 0.4 * Flow;
    mat2 R = mat2(cos(t), -sin(t), sin(t), cos(t));
    if (mod(i.x + i.y, 2.0) == 0.0) R = -R;

    return 2.0 * mix( mix( dot( hash( i + vec2(0,0) ), (f - vec2(0,0))*R ), 
                     dot( hash( i + vec2(1,0) ),-(f - vec2(1,0))*R ), u.x),
                mix( dot( hash( i + vec2(0,1) ),-(f - vec2(0,1))*R ), 
                     dot( hash( i + vec2(1,1) ), (f - vec2(1,1))*R ), u.x), u.y);
}

// Procesa el tipo de turbulencia según la selección plana nativa en preprocesador
float Mnoise(in vec2 uv, float speedMult) {
    float n = flow_noise(uv, speedMult);
    
    #ifdef Pattern_Flame
        return -1.0 + 2.0 * (1.0 - abs(n)); // Estilo fuego (Crestas afiladas)
    #endif
    #ifdef Pattern_Cloud
        return -1.0 + 2.0 * (abs(n));       // Estilo nube (Esponjoso acumulativo)
    #endif
    
    return n; // Estilo Base (Turbulencia estándar)
}

// Suma de turbulencia (FBM de 4 octavas aplanadas fijas con velocidades estáticas)
float turb( in vec2 uv )
{ 	
    float f = 0.0;
    mat2 m = mat2( 1.6,  1.2, -1.2,  1.6 );
    
    f  = 0.5000*Mnoise( uv, 2.0 );  uv = m*uv; // Octava 1: velocidad 2^1 = 2.0
	f += 0.2500*Mnoise( uv, 4.0 );  uv = m*uv; // Octava 2: velocidad 2^2 = 4.0
	f += 0.1250*Mnoise( uv, 8.0 );  uv = m*uv; // Octava 3: velocidad 2^3 = 8.0
	f += 0.0625*Mnoise( uv, 16.0 ); uv = m*uv; // Octava 4: velocidad 2^4 = 16.0
	
    return f/.9375; 
}

// ============================================================================
// PROCESAMIENTO DE SEÑAL Y COORDENADAS
// ============================================================================

// Calcula las coordenadas aplicando la atenuación de escala 0.1x a Scale, Size_X y Size_Y
vec2 getCoords(vec2 uv_val) {
    // Escala del deslizador multiplicada por 0.1 y por su base correspondiente
    float internal_scale = (Scale * 0.1) * 5.0;
    float internal_size_x = Size_X * 0.1;
    float internal_size_y = Size_Y * 0.1;
    
    float fx = (internal_size_x * 10.0) * internal_scale * 5.6;
    float fy = (internal_size_y * 10.0) * internal_scale * 5.6;
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

// Evalúa y retorna el valor de ruido final en calidad completa para Color, NonColor y Opacity (Turbulencia de 4 octavas)
float getSample(vec2 uv_coord) {
    vec2 p = getCoords(uv_coord);
    float f = turb(5.0 * p);
    
    float finalVal = f * 0.5 + 0.5;
    
    return processNoiseValue(finalVal);
}

// Evalúa y retorna una versión sumamente ligera de 1 sola octava de flujo para calcular normales (Lag-Free)
float getSampleLight(vec2 uv_coord) {
    vec2 p = getCoords(uv_coord);
    float f = Mnoise(5.0 * p, 2.0); // 1 octava a velocidad base (2.0)
    
    float finalVal = f * 0.5 + 0.5;
    
    return processNoiseValue(finalVal);
}

// ============================================================================
// EJECUCIÓN PRINCIPAL
// ============================================================================

void main() {
    // --- EVALUACIÓN DE INTENSIDAD PROCEDURAL (Calidad Completa) ---
    float main_intensity = getSample(UVCoord);

    // Muestreo dinámico por diferencias finitas centrales para cálculo de normales (Lag-Free)
    float h = 0.002; 
    float val_x = getSampleLight(UVCoord + vec2(h, 0.0));
    float val_y = getSampleLight(UVCoord + vec2(0.0, h));

    vec2 final_derivatives = vec2(val_x - main_intensity, val_y - main_intensity) * (1.0 / h);
    vec3 final_normal = normalize(vec3(-final_derivatives.x, -final_derivatives.y, 1.0));

    // --- ASIGNACIÓN DE SALIDAS ESTÁNDAR ÚNICAS ---
    Color = vec3(main_intensity); // Salida de ruido de flujo en escala de grises puro
    Normal = final_normal;
    NonColor = main_intensity;
    Opacity = main_intensity;
}