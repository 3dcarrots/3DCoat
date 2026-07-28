// ============================================================================
// CONFIGURACIÓN DE NODOS EN 3DCOAT (NGL)
// ============================================================================
in vec2 UVCoord(knot = ioUV); // Coordenadas UV de entrada

// Deslizadores registrados de forma segura
in float Frequency(value = 0.1, min = 0.0, max = 200.0); // Ajustado a valor inicial 0.1
in float Sharpness(value = 0.0, min = 0.0, max = 1.0); // Control de dureza del degradado

// Switches ON/OFF (Checkboxes)
#bool NonSquareExpansion    // True = Compensa deformación en formatos no cuadrados
#bool Invert                // True = Invierte la máscara final y normales
#bool Absolute              // True = Usa valores absolutos (Ridge / Billow Noise)
#bool EnableTiling          // True = Activa la repetición en mosaico (pnoise)

// ============================================================================
// SALIDAS (Conectores del nodo) - Mantenidos estrictamente en líneas 17 a 20
// ============================================================================
out vec3 Color;       // Salida RGB de color (Línea 17)
out float NonColor;   // Patrón procedural en escala de grises (Línea 18)
out vec3 Normal;      // Vector normal en espacio tangente (Línea 19)
out float Opacity;    // Máscara de opacidad para transparencia (Línea 20)

// ============================================================================
// CONTROLES ADICIONALES (Separados para evitar bugs de la interfaz vectorial)
// ============================================================================
in float Scale(value = 1.0, min = 0.0, max = 200.0); // Rango de 0 a 200
in float DeformX(value = 1.0, min = 0.0, max = 200.0); // Deformación en X (0 a 200)
in float DeformY(value = 1.0, min = 0.0, max = 200.0); // Deformación en Y (0 a 200)
in float OffsetX(value = 0.0, min = 0.0, max = 200.0); // Desplazamiento en X (0 a 200)
in float OffsetY(value = 0.0, min = 0.0, max = 200.0); // Desplazamiento en Y (0 a 200)
in float DistortIntensity(value = 0.0, min = 0.0, max = 5.0); // Intensidad de la distorsión
in float DistortScale(value = 2.0, min = 0.0, max = 20.0); // Rango de 0 a 20
in float Bright(value = 0.0, min = -1.0, max = 1.0); // Offset de luminancia (Baseline)
in float Contrast(value = 1.0, min = 0.0, max = 5.0); // Contraste general

// ============================================================================
// FUNCIONES AUXILIARES
// ============================================================================
vec3 SimplexPerlin2D_Deriv( vec2 P )
{
    const float SKEWFACTOR = 0.36602540378443864676372317075294;
    const float UNSKEWFACTOR = 0.21132486540518711774542560974902;
    const float SIMPLEX_TRI_HEIGHT = 0.70710678118654752440084436210485;
    const vec3 SIMPLEX_POINTS = vec3( 1.0-UNSKEWFACTOR, -UNSKEWFACTOR, 1.0-2.0*UNSKEWFACTOR );

    P *= SIMPLEX_TRI_HEIGHT;    
    vec2 Pi = floor( P + dot( P, vec2( SKEWFACTOR ) ) );

    vec4 Pt = vec4( Pi.xy, Pi.xy + 1.0 );
    Pt = Pt - floor(Pt * ( 1.0 / 71.0 )) * 71.0;
    Pt += vec2( 26.0, 161.0 ).xyxy;
    Pt *= Pt;
    Pt = Pt.xzxz * Pt.yyww;
    vec4 hash_x = fract( Pt * ( 1.0 / 951.135664 ) );
    vec4 hash_y = fract( Pt * ( 1.0 / 642.949883 ) );

    vec2 v0 = Pi - dot( Pi, vec2( UNSKEWFACTOR ) ) - P;
    vec4 v1pos_v1hash = (v0.x < v0.y) ? vec4(SIMPLEX_POINTS.xy, hash_x.y, hash_y.y) : vec4(SIMPLEX_POINTS.yx, hash_x.z, hash_y.z);
    vec4 v12 = vec4( v1pos_v1hash.xy, SIMPLEX_POINTS.zz ) + v0.xyxy;

    vec3 grad_x = vec3( hash_x.x, v1pos_v1hash.z, hash_x.w ) - 0.49999;
    vec3 grad_y = vec3( hash_y.x, v1pos_v1hash.w, hash_y.w ) - 0.49999;
    vec3 norm = inversesqrt( grad_x * grad_x + grad_y * grad_y );
    grad_x *= norm;
    grad_y *= norm;
    vec3 grad_results = grad_x * vec3( v0.x, v12.xz ) + grad_y * vec3( v0.y, v12.yw );

    vec3 m = vec3( v0.x, v12.xz ) * vec3( v0.x, v12.xz ) + vec3( v0.y, v12.yw ) * vec3( v0.y, v12.yw );
    m = max(0.5 - m, 0.0);
    vec3 m2 = m*m;
    vec3 m4 = m2*m2;

    vec3 temp = 8.0 * m2 * m * grad_results;
    float xderiv = dot( temp, vec3( v0.x, v12.xz ) ) - dot( m4, grad_x );
    float yderiv = dot( temp, vec3( v0.y, v12.yw ) ) - dot( m4, grad_y );

    const float FINAL_NORMALIZATION = 99.204334582718712976990005025589;
    return vec3( dot( m4, grad_results ), xderiv, yderiv ) * FINAL_NORMALIZATION;
}

// ============================================================================
// EJECUCIÓN DIRECTA (Cuerpo principal / "Implicit Main")
// ============================================================================
vec2 Deform = vec2(DeformX, DeformY);
vec2 Offset = vec2(OffsetX, OffsetY);

vec2 uv = UVCoord;

#if NonSquareExpansion
    if (ioResolution.y > 0.001) {
        uv.x *= ioResolution.x / ioResolution.y;
    }
#endif

vec2 safeSize = max(Deform, vec2(0.001));
uv = (uv / safeSize) + Offset;

float globalScale = Frequency * Scale;
uv *= globalScale;

// --- DOMAIN WARPING (DISTORTION EN SIMPLEX) ---
if (DistortIntensity > 0.001) {
    vec2 distort_uv = uv * DistortScale;
    vec3 d0 = SimplexPerlin2D_Deriv(distort_uv);
    vec3 d1 = SimplexPerlin2D_Deriv(distort_uv + vec2(31.415, 57.123));
    uv += vec2(d0.x, d1.x) * DistortIntensity;
}

#if EnableTiling
    float period = max(floor(globalScale), 1.0);
    uv = mod(uv, period);
#endif

// --- EVALUACIÓN DE SIMPLEX ---
vec3 simplexData = SimplexPerlin2D_Deriv(uv);
float rawNoise = simplexData.x;
vec2 dNoise = simplexData.yz;

#if Absolute
    float signVal = sign(rawNoise);
    rawNoise = abs(rawNoise);
    dNoise *= signVal;
#endif

float noiseVal = rawNoise * 0.5 + 0.5;
dNoise *= 0.5;

// --- BRIGHT Y CONTRASTE ---
float processedNoise = (noiseVal - 0.5) * Contrast + 0.5 + Bright;
float final_intensity = clamp(processedNoise, 0.0, 1.0);
dNoise *= Contrast;

// --- CONTROL DE SHARPNESS ---
float soft_width = max((1.0 - Sharpness) * 0.5, 0.0001);
float edge0 = max(0.5 - soft_width, 0.0);
float edge1 = min(0.5 + soft_width, 1.0);

float t = clamp((final_intensity - edge0) / (edge1 - edge0), 0.0, 1.0);
float output_intensity = t * t * (3.0 - 2.0 * t);

// --- CÁLCULO DE DERIVADAS AJUSTADAS POR REGLA DE LA CADENA ---
vec2 dBase = (dNoise * globalScale) / safeSize;

float dIdNoise = 0.0;
if (t > 0.0 && t < 1.0) {
    dIdNoise = (6.0 * t * (1.0 - t)) / (edge1 - edge0);
}

vec2 final_derivatives = dBase * dIdNoise;
vec3 final_normal = normalize(vec3(-final_derivatives.x, -final_derivatives.y, 1.0));

#if Invert
    output_intensity = 1.0 - output_intensity;
    final_derivatives = -final_derivatives;
    final_normal = normalize(vec3(-final_derivatives.x, -final_derivatives.y, 1.0));
#endif

Color = vec3(output_intensity);            // Línea 17
NonColor = output_intensity;               // Línea 18
Normal = final_normal;                     // Línea 19
Opacity = output_intensity;                // Línea 20