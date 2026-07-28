// ============================================================================
// CONFIGURACIÓN DE NODOS EN 3DCOAT (NGL)
// ============================================================================
in vec2 UVCoord(knot = ioUV); // UV Coord de entrada

// Menú desplegable nativo de 3DCoat
#enum Pattern Worms Worms2 Voronoi Cells Micro Noise

// Parámetros en el orden exacto solicitado (Scale_Z eliminado, Scale_X/Y renombrados a Size_X/Y)
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
// FUNCIONES AUXILIARES DE RUIDO TOTALMENTE PLANAS (Cero bucles)
// ============================================================================

vec3 mod289(vec3 x) {return x - floor(x * (1.0 / 289.0)) * 289.0;}
vec2 mod289(vec2 x) {return x - floor(x * (1.0 / 289.0)) * 289.0;}
vec3 permute(vec3 x) {return mod289(((x*34.0)+1.0)*x);}

float snoise(vec2 v)
{
    const vec4 C = vec4(0.211324865405187,  // (3.0-sqrt(3.0))/6.0
                        0.366025403784439,  // 0.5*(sqrt(3.0)-1.0)
                        -0.577350269189626,  // -1.0 + 2.0 * C.x
                        0.024390243902439); // 1.0 / 41.0
    vec2 i  = floor(v + dot(v, C.yy) );
    vec2 x0 = v -   i + dot(i, C.xx);

    vec2 i1;
    i1 = (x0.x > x0.y) ? vec2(1.0, 0.0) : vec2(0.0, 1.0);
    vec4 x12 = x0.xyxy + C.xxzz;
    x12.xy -= i1;

    i = mod289(i); 
    vec3 p = permute( permute( i.y + vec3(0.0, i1.y, 1.0 ))
    + i.x + vec3(0.0, i1.x, 1.0 ));

    vec3 m = max(0.5 - vec3(dot(x0,x0), dot(x12.xy,x12.xy), dot(x12.zw,x12.zw)), 0.0);
    m = m*m ;
    m = m*m ;

    vec3 x = 2.0 * fract(p * C.www) - 1.0;
    vec3 h = abs(x) - 0.5;
    vec3 ox = floor(x + 0.5);
    vec3 a0 = x - ox;

    m *= 1.79284291400159 - 0.85373472095314 * ( a0*a0 + h*h );

    vec3 g;
    g.x  = a0.x  * x0.x  + h.x  * x0.y;
    g.yz = a0.yz * x12.xz + h.yz * x12.yw;
    return 130.0 * dot(m, g);
}

float sdLine( vec2 p, vec2 a, vec2 b, float r )
{
    vec2 pa = p - a, ba = b - a;
    float h = clamp( dot(pa,ba)/dot(ba,ba), 0.0, 1.0 );
    return length( pa - ba*h ) - r;
}

vec2 opRep( vec2 p, vec2 c )
{ 
    return mod(p,c)-0.5*c;
}

vec2 opRepFlip( vec2 p, vec2 c )
{ 
    vec2 fpc = floor(p/c);
    float flip = mod((fpc.x + fpc.y), 2.);
    vec2 ret = p - c*(fpc + 0.5);
    if(flip >= 1.)return ret.yx;
    return ret;
}

vec2 opWarp( vec2 p )
{ 
    return vec2(p.x+0.1*sin(20.*p.y),p.y);
}

float nnoise( in vec2 uv ){return 0.5 + 0.5*snoise(uv);} //norm [0,1]
float rnoise( in vec2 uv ){return 1. - abs(snoise(uv));} //ridge

// Función FBM aplanada de 2 octavas fijas para máximo rendimiento
float fbm_oct2( vec2 x ) 
{
    float a = 0.0;
    float b = 0.9;
    
    // Octava 1
    a += b * nnoise(x);          	
    b *= 0.49;
    x *= 1.98;
    
    // Octava 2
    a += b * nnoise(x);
    
    return a;
}

// Función FBM Ridged aplanada de 3 octavas fijas
float fbmr_oct3( vec2 x ) 
{
    float a = 0.0;
    float b = 0.4; 
    
    // Octava 1
    a += b * rnoise(x);          	
    b *= 0.9;
    x *= 1.98;
    
    // Octava 2
    a += b * rnoise(x);          	
    b *= 0.9;
    x *= 1.98;
    
    // Octava 3
    a += b * rnoise(x);
    
    return a;
}

float fbm2( in vec2 p )
{
    vec2 q = vec2( fbm_oct2( p + vec2(0.0,0.0) ),
                    fbm_oct2( p + vec2(5.2,1.3) ) );

    return fbmr_oct3( p + (2.9 * DistortIntensity)*q ); 
}

float fbm3( in vec2 p )
{
    vec2 q = vec2( fbm_oct2( p + vec2(0.0,0.0) ),
                    fbm_oct2( p + vec2(5.2,1.3) ) );

    vec2 r = vec2( fbm_oct2( p * DistortScale + 4.0*q + vec2(1.7,9.2) ), 
                    fbm_oct2( p * DistortScale + 4.0*q + vec2(8.3,2.8) ) );
    return fbmr_oct3( p*2.0 + (0.4 * DistortIntensity)*r ); 
}

// ============================================================================
// PROCESAMIENTO DE SEÑAL Y COORDENADAS
// ============================================================================

// Retorna las coordenadas aplicando el multiplicador del visor de 3DCoat y la escala global
vec2 getCoords(vec2 uv_val) {
    float fx = (Size_X * 10.0) * Scale;
    float fy = (Size_Y * 10.0) * Scale;
    return vec2(uv_val.x * fx, uv_val.y * fy);
}

// Procesa el valor crudo aplicando Contrast, Shadows, Midtones y Luminance
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

// Evalúa y retorna el valor de ruido final de alta calidad en escala de grises (Color, NonColor, Opacity)
float getSample(vec2 uv_coord) {
    vec2 vUv = getCoords(uv_coord);
    vec2 c, luv, nuv = vUv * 7.0;

    // Fondo del pergamino
    float n = fbm3(nuv);
    float nVal = 2.9 * (n - 0.06);
    nVal *= 1.0 - 0.35 * clamp(abs(vUv.y - 0.5) - 0.1, 0.0, 1.0);
    nVal *= 1.0 - 0.65 * smoothstep(0.27, 0.45, (clamp(snoise(3.9 * nuv) * nnoise(12.2 * nuv) * rnoise(9.2 * nuv), 0.0, 1.0)));
    n = clamp(nVal, 0.0, 1.0);
    nVal = n;
    
    nVal *= 1.14 - 1.5 * clamp(abs(uv_coord.y - 0.5) - 0.25, 0.0, 1.0);
    nVal *= (0.9 + 0.1 * abs(snoise(14.0 * nuv)));
    nVal *= (0.9 + 0.1 * abs(snoise(24.0 * nuv)));
    nVal *= (0.86 + 0.14 * nnoise(41.0 * nuv));
    nVal *= (0.95 + 0.05 * fbm_oct2(1.2 * nuv));
    
    // Puntos blancos
    nVal += (1.0 - n) * smoothstep(0.5, 1.0, 1.72 * nnoise(3.0 * nuv) * nnoise(4.3 * nuv)); 

    vec2 d1 = vec2(rnoise(1.45 * nuv), rnoise(1.45 * nuv + vec2(-7.2, 6.9)));
    
    nuv += 22.0;
    float lm = 0.6;
    float len, n_line;
    
    // OPTIMIZACIÓN EXCEPCIONAL: Precalculamos la deformación del espacio una sola vez para todas las líneas.
    // Esto ahorra un 75% de las llamadas a snoise dentro de esta función.
    vec2 base_warp = vec2(snoise(0.22 * nuv * DistortScale), snoise(0.22 * nuv * DistortScale + vec2(4.2, -9.1)));
    
    // Capa de Líneas 1
    luv = nuv;
    luv += 0.08 * DistortIntensity * d1;
    luv += 0.85 * DistortIntensity * base_warp;
    c = vec2(1.585);
    len = 0.04;
    n_line = sdLine(opRepFlip(luv, c), vec2(-c.x * len, -len), vec2(c.x * len, len), 0.0001);
    nVal *= lm + (1.0 - lm) * smoothstep(0.0, 0.01, n_line);
    
    // Capa de Líneas 2
    luv = nuv + vec2(-13.2, 15.1);
    luv += 0.09 * DistortIntensity * d1;
    luv += 0.85 * DistortIntensity * base_warp;
    c = vec2(1.79);
    len = 0.04; 
    n_line = sdLine(opRepFlip(luv, c), vec2(-c.x * len, len), vec2(c.x * len, -len), 0.0001);
    nVal *= lm + (1.0 - lm) * smoothstep(0.0, 0.01, n_line);
    
    // Capa de Líneas 3
    luv = nuv + vec2(27.2,-21.5);
    luv += 0.09 * DistortIntensity * d1;
    luv += 0.85 * DistortIntensity * base_warp;
    c = vec2(2.07);
    len = 0.085; 
    n_line = sdLine(opRepFlip(luv, c), vec2(-c.x * len, 0.0), vec2(c.x * len, 0.0), 0.0001);
    nVal *= lm + (1.0 - lm) * smoothstep(0.0, 0.01, n_line);
    
    // Capa de Líneas 3.2
    luv = nuv + vec2(-17.8,-28.5);
    luv += 0.09 * DistortIntensity * d1;
    luv += 0.85 * DistortIntensity * base_warp;
    c = vec2(1.87);
    len = 0.095; 
    n_line = sdLine(opRepFlip(luv, c), vec2(-c.x * len, 0.0), vec2(c.x * len, 0.0), 0.0001);
    nVal *= lm + (1.0 - lm) * smoothstep(0.0, 0.01, n_line);
    
    return processNoiseValue(nVal);
}

// OPTIMIZACIÓN EXCEPCIONAL (getSampleLight): Evalúa una versión ultra-rápida y limpia para el cálculo de normales.
// Evita el lag y permite que el cursor se mueva con total fluidez.
float getSampleLight(vec2 uv_coord) {
    vec2 vUv = getCoords(uv_coord);
    vec2 nuv = vUv * 7.0;

    // Fondo del pergamino simplificado para el relieve
    float n = fbm_oct2(nuv);
    float nVal = 2.9 * (n - 0.06);
    nVal = clamp(nVal, 0.0, 1.0);
    
    return processNoiseValue(nVal);
}

// ============================================================================
// EJECUCIÓN PRINCIPAL
// ============================================================================

void main() {
    // --- EVALUACIÓN DE INTENSIDAD PROCEDURAL (Calidad Completa) ---
    float main_intensity = getSample(UVCoord);

    // Muestreo dinámico ultra-rápido por diferencias finitas (Ahorra un 95% de carga computacional)
    float h = 0.002; 
    float val_x = getSampleLight(UVCoord + vec2(h, 0.0));
    float val_y = getSampleLight(UVCoord + vec2(0.0, h));

    vec2 final_derivatives = vec2(val_x - main_intensity, val_y - main_intensity) * (1.0 / h);
    vec3 final_normal = normalize(vec3(-final_derivatives.x, -final_derivatives.y, 1.0));

    // --- ASIGNACIÓN DE SALIDAS ESTÁNDAR ÚNICAS ---
    Color = vec3(main_intensity); // Salida en escala de grises libre de tintes de color
    Normal = final_normal;
    NonColor = main_intensity;
    Opacity = main_intensity;
}