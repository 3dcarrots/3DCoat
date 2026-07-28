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
// CONTROLES ADICIONALES (Leídos dinámicamente)
// ============================================================================
in float Scale(value = 1.0, min = 0.1, max = 10.0); // Rango de 0.1 a 10
in float OffsetX(value = 0.0, min = 0.0, max = 90.0); // Desplazamiento en X (0 a 90)
in float OffsetY(value = 0.0, min = 0.0, max = 90.0); // Desplazamiento en Y (0 a 90)
in float DistortIntensity(value = 0.0, min = 0.0, max = 5.0); // Intensidad de la distorsión
in float DistortScale(value = 2.0, min = 0.1, max = 10.0); // Rango de 0.1 a 10
in float Bright(value = 0.0, min = -1.0, max = 1.0); // Offset de luminancia (Baseline)
in float Contrast(value = 1.0, min = 0.0, max = 5.0); // Contraste general

// ============================================================================
// FUNCIONES AUXILIARES
// ============================================================================

// Ruido de Perlin 2D con derivadas analíticas (Optimizado sin lógica de Tiling periódico)
vec3 Perlin2D_Deriv( vec2 P )
{
    vec2 Pi = floor(P);
    vec4 Pf_Pfmin1 = P.xyxy - vec4( Pi, Pi + 1.0 );

    // Calculamos las tablas de hash analíticas para los vectores de gradiente
    vec4 Pt = vec4( Pi.xy, Pi.xy + 1.0 );
    Pt = Pt - floor(Pt * ( 1.0 / 71.0 )) * 71.0;
    Pt += vec2( 26.0, 161.0 ).xyxy;
    Pt *= Pt;
    Pt = Pt.xzxz * Pt.yyww;
    vec4 hash_x = fract( Pt * ( 1.0 / 951.135664 ) );
    vec4 hash_y = fract( Pt * ( 1.0 / 642.949883 ) );

    // Calculamos el valor de los gradientes resultantes
    vec4 grad_x = hash_x - 0.49999;
    vec4 grad_y = hash_y - 0.49999;
    vec4 norm = inversesqrt( grad_x * grad_x + grad_y * grad_y );
    grad_x *= norm;
    grad_y *= norm;
    vec4 dotval = ( grad_x * Pf_Pfmin1.xzxz + grad_y * Pf_Pfmin1.yyww );

    // Curva de interpolación C2 (Hermite de 5º grado y su derivada empacados en un vec4)
    vec4 blend = Pf_Pfmin1.xyxy * Pf_Pfmin1.xyxy * ( Pf_Pfmin1.xyxy * ( Pf_Pfmin1.xyxy * ( Pf_Pfmin1.xyxy * vec2( 6.0, 0.0 ).xxyy + vec2( -15.0, 30.0 ).xxyy ) + vec2( 10.0, -60.0 ).xxyy ) + vec2( 0.0, 30.0 ).xxyy );

    // Convertimos los datos para un formato paralelo
    vec3 dotval0_grad0 = vec3( dotval.x, grad_x.x, grad_y.x );
    vec3 dotval1_grad1 = vec3( dotval.y, grad_x.y, grad_y.y );
    vec3 dotval2_grad2 = vec3( dotval.z, grad_x.z, grad_y.z );
    vec3 dotval3_grad3 = vec3( dotval.w, grad_x.w, grad_y.w );

    // Evaluamos constantes comunes
    vec3 k0_gk0 = dotval1_grad1 - dotval0_grad0;
    vec3 k1_gk1 = dotval2_grad2 - dotval0_grad0;
    vec3 k2_gk2 = dotval3_grad3 - dotval2_grad2 - k0_gk0;

    // Evaluamos el ruido final y sus derivadas analíticas
    vec3 results = dotval0_grad0 + blend.x * k0_gk0 + blend.y * ( k1_gk1 + blend.x * k2_gk2 );
    results.yz += blend.zw * ( vec2( k0_gk0.x, k1_gk1.x ) + blend.yx * k2_gk2.xx );
    
    // Escalamos el resultado estrictamente al rango de -1.0 a 1.0
    return results * 1.4142135623730950488016887242097;  
}

// ============================================================================
// EJECUCIÓN DIRECTA (Cuerpo principal / "Implicit Main")
// ============================================================================

// Reconstruimos el vector de desplazamiento espacial
vec2 Offset = vec2(OffsetX, OffsetY);

// Desplazamos las coordenadas iniciales de entrada (Corrección: Offset sumado)
vec2 uv = UVCoord + Offset;

// Aplicamos la repetición global multiplicando la frecuencia ingresada por 10.0 (escala real x10)
float globalScale = (Frequency * 10.0) * Scale;
uv *= globalScale;

// --- DOMAIN WARPING (DISTORTION EN PERLIN) ---
if (DistortIntensity > 0.001) {
    vec2 distort_uv = uv * DistortScale;
    // Corrección: Llamadas a Perlin2D_Deriv con exactamente 1 parámetro
    vec3 d0 = Perlin2D_Deriv(distort_uv);
    vec3 d1 = Perlin2D_Deriv(distort_uv + vec2(31.415, 57.123));
    uv += vec2(d0.x, d1.x) * DistortIntensity;
}

// --- EVALUACIÓN DE PERLIN ---
// Corrección: Llamada a Perlin2D_Deriv con exactamente 1 parámetro y paréntesis balanceados
vec3 perlinData = Perlin2D_Deriv(uv);
float rawNoise = perlinData.x;
vec2 dNoise = perlinData.yz;

// Llevamos el rango nativo de Perlin [-1.0, 1.0] al rango estándar de máscaras [0.0, 1.0]
float noiseVal = rawNoise * 0.5 + 0.5;
dNoise *= 0.5;

// --- BASELINE (BRIGHT) Y CONTRASTE ---
float processedNoise = (noiseVal - 0.5) * Contrast + 0.5 + Bright;
float final_intensity = clamp(processedNoise, 0.0, 1.0);

// Ajustamos las derivadas según el contraste (el offset de Bright no altera la pendiente)
dNoise *= Contrast;

// --- CONTROL DE SHARPNESS (DUREZA DEL DEGRADADO) ---
float soft_width = max((1.0 - Sharpness) * 0.5, 0.0001);
float edge0 = max(0.5 - soft_width, 0.0);
float edge1 = min(0.5 + soft_width, 1.0);

float t = clamp((final_intensity - edge0) / (edge1 - edge0), 0.0, 1.0);
float output_intensity = t * t * (3.0 - 2.0 * t);

// --- CÁLCULO DE DERIVADAS AJUSTADAS POR REGLA DE LA CADENA ---

// 1. Escalamos las derivadas por la escala global (Frequency * Scale * 10.0)
vec2 dBase = dNoise * globalScale;

// 2. Factor de Sharpness
float dIdNoise = 0.0;
if (t > 0.0 && t < 1.0) {
    dIdNoise = (6.0 * t * (1.0 - t)) / (edge1 - edge0);
}

// 3. Multiplicamos para obtener las derivadas finales para el cálculo de normales
vec2 final_derivatives = dBase * dIdNoise;

// 4. Calculamos la normal final en espacio tangente
vec3 final_normal = normalize(vec3(-final_derivatives.x, -final_derivatives.y, 1.0));

// --- INVERSIÓN FINAL (Invert) ---
#if Invert
    output_intensity = 1.0 - output_intensity;
    final_derivatives = -final_derivatives;
    final_normal = normalize(vec3(-final_derivatives.x, -final_derivatives.y, 1.0));
#endif

// Asignamos las salidas finales respetando el orden exacto de los pines en la interfaz de 3DCoat
Color = vec3(output_intensity);            // Línea 16
Normal = final_normal;                     // Línea 17
NonColor = output_intensity;               // Línea 18
Opacity = output_intensity;                // Línea 19