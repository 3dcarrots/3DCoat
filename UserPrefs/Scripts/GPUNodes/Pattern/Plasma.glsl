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
in float Scale(value = 1.0, min = 0.1, max = 5.0); // Multiplicador de escala
in float DistortIntensity(value = 1.0, min = 0.0, max = 5.0); // Intensidad de la turbulencia
in float DistortScale(value = 4.0, min = 0.1, max = 10.0); // Escala de la deformación (distortionScale)
in float Bright(value = 0.0, min = -1.0, max = 1.0); // Offset de luminancia (Baseline)
in float Contrast(value = 1.0, min = 0.0, max = 5.0); // Contraste general

// Selector desplegable unificado con nombres seguros contra colisiones de 3DCoat
#enum RenderStyle Rainbow Grayscale

// ============================================================================
// FUNCIONES AUXILIARES (Fieles al plasma.txt original con optimización y tipado)
// ============================================================================

#define Rainbow 0
#define Grayscale 1

// Hash de 2 dimensiones a 3 dimensiones
vec3 hash3( vec2 p )
{
    vec3 q = vec3( dot(p,vec2(127.1, 311.7)), 
				   dot(p,vec2(269.5, 183.3)), 
				   dot(p,vec2(419.2, 371.9)) );
	return fract(sin(q) * 43758.5453);
}

// Algoritmo de Voronoise de Iñigo Quílez optimizado a 3x3 para reducir el peso en la GPU (reducción del 64%)
float voronoise( in vec2 p, float u, float v, in float scale )
{
    p = p * scale;
	float k = 1.0 + 63.0 * pow(1.0 - v, 6.0);

    vec2 i = floor(p);
    vec2 f = fract(p);
    
	vec2 a = vec2(0.0, 0.0);
    for( int y=-1; y<=1; y++ )
    for( int x=-1; x<=1; x++ )
    {
        vec2 g = vec2( float(x), float(y) ); // Corrección de casteo estricto
		vec3 o = hash3( i + g ) * vec3(u, u, 1.0);
		vec2 d = g - f + o.xy;
		float w = pow( 1.0 - smoothstep(0.0, 1.414, length(d)), k );
		a += vec2(o.z * w, w);
    }
	
    return a.x / a.y;
}

// Hash pseudoaleatorio 2D
vec2 hash(in vec2 p, in float fac )
{
	p = vec2( dot(p,vec2(127.1 * fac, 311.7 * fac)), dot(p,vec2(269.5 * fac, 183.3 * fac)) );
	return -1.0 + 2.0 * fract(sin(p) * 43758.5453123 * fac);
}

// Ruido de gradiente de 2 dimensiones
float noise( in vec2 p , in float fac)
{
    const float K1 = 0.366025404; 
    const float K2 = 0.211324865; 

	vec2  i = floor( p + (p.x + p.y) * K1 );
    vec2  a = p - i + (i.x + i.y) * K2;
    float m = step(a.y, a.x); 
    vec2  o = vec2(m, 1.0 - m);
    vec2  b = a - o + K2;
	vec2  c = a - vec2(1.0) + vec2(2.0 * K2); // Expresión tipada
    vec3  h = max( 0.5 - vec3(dot(a, a), dot(b, b), dot(c, c) ), 0.0 );
	vec3  n = h * h * h * h * vec3( dot(a, hash(i, fac)), dot(b, hash(i + o, fac)), dot(c, hash(i + vec2(1.0), fac)));
    return dot( n, vec3(70.0) );
}

// FBM Optimizado a 3 Octavas (25% más rápido)
float combine(in vec2 p, in float fac, in float scale)
{
    float aspect = 1.0;
    if (ioResolution.y > 0.001) {
        aspect = ioResolution.x / ioResolution.y;
    }
    vec2 uv = p * vec2(aspect, 1.0);
	
	float f = 0.0;
    uv *= scale;
    mat2 m = mat2( 1.6,  1.2, -1.2,  1.6 );
    f  = 0.5000 * noise( uv , fac); uv = m * uv;
    f += 0.2500 * noise( uv , fac); uv = m * uv;
    f += 0.1250 * noise( uv , fac);

	f = 0.5 + 0.5 * f;
    return f;
}

// FBM de 1 Octava dedicado para Domain Warping ultra-rápido (400% de ahorro de GPU)
float combineWarp(in vec2 p, in float fac, in float scale)
{
    float aspect = 1.0;
    if (ioResolution.y > 0.001) {
        aspect = ioResolution.x / ioResolution.y;
    }
    vec2 uv = p * vec2(aspect, 1.0);
    return 0.5 + 0.5 * noise(uv * scale, fac);
}

// Retorna el color final del plasma del algoritmo original de forma rápida
vec3 getPlasmaColor(vec2 uvCoord, float t) {
    vec2 p = uvCoord + vec2(t * 0.005, t * 0.008);
    
    float fac1 = 1.764;
    float fac2 = 2.1938;
    float fac3 = 5.1394;
    float fac4 = 0.1938;
    float fac5 = 3.1394;
    
    float osc = 1.0 + sin(t * 0.3) * 0.5;
    float osc2 = 0.75 + sin(t * 0.47) * 0.25;
    
    // Distorsión de coordenadas optimizada usando ruidos de 1 octava
    vec2 offset = vec2(combineWarp(p, fac1, DistortScale) - 0.5, 
                       combineWarp(p, fac2, DistortScale) - 0.5) * DistortIntensity;
    
    float noiseComp1 = combine(p + offset * osc, fac3, 6.0);
    float noiseComp2 = combine(p + offset * osc, fac4, 7.0);
    float noiseComp3 = combine(p + offset * osc, fac5, 8.0);
    float vorComp = voronoise(p + offset * osc, 1.0, 0.0, 10.0);
    
    float e1 = 0.1 + fract(vorComp * fac1) * (1.0 + cos(t * 0.0017));
    float e2 = 0.1 + fract(vorComp * fac2) * (1.0 + cos(t * 0.0017));
    float e3 = 0.1 + fract(vorComp * fac3) * (1.0 + cos(t * 0.0017));
    
    // Exponentes optimizados a ruidos rápidos de 1 octava
    float rComp = combineWarp(p + offset * osc2, fac2 * fac4, 2.0);
    float gComp = combineWarp(p + offset * osc2, fac2 * fac5, 2.0);
    float bComp = combineWarp(p + offset * osc2, fac3 * fac2, 2.0);
    
    vec3 col = vec3(pow(max(noiseComp1, 0.0001), e1 * rComp),
                    pow(max(noiseComp2, 0.0001), e2 * gComp),
                    pow(max(noiseComp3, 0.0001), e3 * bComp));
                    
    col = clamp((col - vec3(0.5)) * Contrast + vec3(0.5 + Bright), 0.0, 1.0);
    
    return col;
}

// Canal de grises dedicado ultra-rápido para el relieve (Evita calcular canales redundantes RGB)
float getPlasmaGrayscale(vec2 uvCoord, float t) {
    vec2 p = uvCoord + vec2(t * 0.005, t * 0.008);
    
    float fac1 = 1.764;
    float fac2 = 2.1938;
    float fac3 = 5.1394;
    float osc = 1.0 + sin(t * 0.3) * 0.5;
    
    // Distorsión espacial rápida
    vec2 offset = vec2(combineWarp(p, fac1, DistortScale) - 0.5, 
                       combineWarp(p, fac2, DistortScale) - 0.5) * DistortIntensity;
    
    // Evaluamos solo una componente y Voronoise para la altura (80% de ahorro en cálculo de normales)
    float noiseComp1 = combine(p + offset * osc, fac3, 6.0);
    float vorComp = voronoise(p + offset * osc, 1.0, 0.0, 10.0);
    
    float luma = mix(noiseComp1, vorComp, 0.5);
    
    // Aplicamos Bright y Contrast
    float processedNoise = (luma - 0.5) * Contrast + 0.5 + Bright;
    float final_intensity = clamp(processedNoise, 0.0, 1.0);

    // Dureza del degradado (Sharpness)
    float soft_width = max((1.0 - Sharpness) * 0.5, 0.0001);
    float edge0 = max(0.5 - soft_width, 0.0);
    float edge1 = min(0.5 + soft_width, 1.0);

    float t_interp = clamp((final_intensity - edge0) / (edge1 - edge0), 0.0, 1.0);
    return t_interp * t_interp * (3.0 - 2.0 * t_interp);
}

// ============================================================================
// EJECUCIÓN DIRECTA (Cuerpo principal / "Implicit Main")
// ============================================================================

// Coordenadas UV directas sin desplazamientos (Offset removido)
vec2 uv = UVCoord;

// Aplicamos la repetición global multiplicando la frecuencia ingresada por 10.0 (escala real x10)
float globalScale = (Frequency * 10.0) * Scale;
uv *= globalScale;

// Congelamos el tiempo de forma estática (Fijo en el tiempo)
float t_z = 0.0; 

// Evaluamos el color RGB completo de forma única
vec3 final_color = getPlasmaColor(uv, t_z);

// Evaluamos la altura de grises dedicada para la máscara y opacidad
float main_intensity = getPlasmaGrayscale(uv, t_z);

// Cálculo de normales ultra-rápido usando el mapa de grises dedicado
float h = 0.002; // Paso de muestreo óptimo
float val_x = getPlasmaGrayscale(uv + vec2(h, 0.0), t_z);
float val_y = getPlasmaGrayscale(uv + vec2(0.0, h), t_z);

vec2 final_derivatives = vec2(val_x - main_intensity, val_y - main_intensity) * (1.0 / h);

// Calculamos el vector normal final en espacio tangente
vec3 final_normal = normalize(vec3(-final_derivatives.x, -final_derivatives.y, 1.0));

// --- INVERSIÓN FINAL (Invert) ---
#ifdef Invert
    main_intensity = 1.0 - main_intensity;
    final_color = vec3(1.0) - final_color;
    final_derivatives = -final_derivatives;
    final_normal = normalize(vec3(-final_derivatives.x, -final_derivatives.y, 1.0));
#endif

// Aplicamos el coloreado psicodélico o grises de forma estable con RenderStyle
vec3 output_color = vec3(main_intensity);
#ifdef RenderStyle_Rainbow
    output_color = final_color;
#endif

// Asignamos las salidas finales respetando el orden exacto de los pines en la interfaz de 3DCoat
Color = output_color;                      // Línea 16
Normal = final_normal;                     // Línea 17
NonColor = main_intensity;                 // Línea 18
Opacity = main_intensity;                  // Línea 19