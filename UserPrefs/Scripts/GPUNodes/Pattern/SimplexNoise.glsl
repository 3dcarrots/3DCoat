// ============================================================================
// CONFIGURACIÓN DE NODOS EN 3DCOAT (NGL)
// ============================================================================
in vec2 UVCoord(knot = ioUV); // Coordenadas UV de entrada

// Deslizadores de frecuencia compactados para máxima precisión (0.0 a 10.0)
in float Frequency(value = 1.0, min = 0.0, max = 10.0); // Escala visual de 0 a 10 (internamente x10)
in float Sharpness(value = 0.0, min = 0.0, max = 1.0); // Control de dureza del degradado

// #bool Invert                // True = Invierte la máscara final y normales

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
in float Scale(value = 1.0, min = 0.1, max = 10.0); // Multiplicador de escala
in float DistortIntensity(value = 0.0, min = 0.0, max = 5.0); // Intensidad de la distorsión
in float DistortScale(value = 2.0, min = 0.1, max = 10.0); // Rango de 0.1 a 10
in float Bright(value = 0.0, min = -1.0, max = 1.0); // Offset de luminancia (Baseline)
in float Contrast(value = 1.0, min = 0.0, max = 5.0); // Contraste general

// ============================================================================
// FUNCIONES AUXILIARES
// ============================================================================

// Sobrecargas y matemáticas base del Ruido Simplex 3D con tipado estricto para evitar fallas
vec3 mod289(vec3 x) { return x - floor(x * (1.0 / 289.0)) * 289.0; }
vec4 mod289(vec4 x) { return x - floor(x * (1.0 / 289.0)) * 289.0; }

vec4 permute(vec4 x) { 
    return mod289(((x * 34.0) + vec4(1.0)) * x); 
}

vec4 taylorInvSqrt(vec4 r) { 
    return vec4(1.79284291400159) - vec4(0.85373472095314) * r; 
}

float snoise(vec3 v) {
  const vec2  C = vec2(1.0/6.0, 1.0/3.0) ;
  const vec4  D = vec4(0.0, 0.5, 1.0, 2.0);

  // Primer esquina
  vec3 i  = floor(v + vec3(dot(v, C.yyy)) );
  vec3 x0 =   v - i + vec3(dot(i, C.xxx)) ;

  // Otras esquinas
  vec3 g = step(x0.yzx, x0.xyz);
  vec3 l = vec3(1.0) - g;
  vec3 i1 = min( g.xyz, l.zxy );
  vec3 i2 = max( g.xyz, l.zxy );

  vec3 x1 = x0 - i1 + C.xxx;
  vec3 x2 = x0 - i2 + C.yyy; 
  vec3 x3 = x0 - D.yyy;      

  // Permutaciones
  i = mod289(i);
  vec4 p = permute( permute( permute(
             i.z + vec4(0.0, i1.z, i2.z, 1.0 ))
           + i.y + vec4(0.0, i1.y, i2.y, 1.0 ))
           + i.x + vec4(0.0, i1.x, i2.x, 1.0 ));

  float n_ = 0.142857142857; 
  vec3  ns = n_ * D.wyz - D.xzx;

  vec4 j = p - vec4(49.0) * floor(p * vec4(ns.z * ns.z));  

  vec4 x_ = floor(j * vec4(ns.z));
  vec4 y_ = floor(j - vec4(7.0) * x_ );    

  vec4 x = x_ * vec4(ns.x) + vec4(ns.yyyy);
  vec4 y = y_ * vec4(ns.x) + vec4(ns.yyyy);
  vec4 h = vec4(1.0) - abs(x) - abs(y);

  vec4 b0 = vec4( x.xy, y.xy );
  vec4 b1 = vec4( x.zw, y.zw );

  vec4 s0 = floor(b0)*vec4(2.0) + vec4(1.0);
  vec4 s1 = floor(b1)*vec4(2.0) + vec4(1.0);
  vec4 sh = -step(h, vec4(0.0));

  vec4 a0 = b0.xzyw + s0.xzyw*sh.xxyy ;
  vec4 a1 = b1.xzyw + s1.xzyw*sh.zzww ;

  vec3 p0 = vec3(a0.xy,h.x);
  vec3 p1 = vec3(a0.zw,h.y);
  vec3 p2 = vec3(a1.xy,h.z);
  vec3 p3 = vec3(a1.zw,h.w);

  // Normalización
  vec4 norm = taylorInvSqrt(vec4(dot(p0,p0), dot(p1,p1), dot(p2, p2), dot(p3,p3)));
  p0 *= norm.x;
  p1 *= norm.y;
  p2 *= norm.z;
  p3 *= norm.w;

  // Mezcla de valores
  vec4 m = max(vec4(0.6) - vec4(dot(x0,x0), dot(x1,x1), dot(x2,x2), dot(x3,x3)), vec4(0.0));
  m = m * m;
  return 42.0 * dot( m*m, vec4( dot(x0,p0), dot(x1,p1),
                                dot(x2,p2), dot(x3,p3) ) );
}

// Retorna el valor final aplicando compensación de brillo, contraste, Sharpness y Z estático
float getSimplexValue(vec2 P) {
    // Evaluamos estáticamente el volumen en Z = 0.0 para eliminar la animación
    float rawNoise = snoise(vec3(P, 0.0));
    
    // Remapeamos el rango [-1, 1] al rango estándar [0, 1] para máscaras
    float noiseVal = rawNoise * 0.5 + 0.5;
    
    // Aplicamos Bright (Baseline) y Contraste
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

// Coordenadas UV de entrada directas
vec2 uv = UVCoord;

// Aplicamos la repetición global multiplicando la frecuencia ingresada por 10.0 (escala real x10)
float globalScale = (Frequency * 10.0) * Scale;
uv *= globalScale;

// --- DOMAIN WARPING (DISTORTION EN SIMPLEX ESTÁTICO) ---
if (DistortIntensity > 0.001) {
    vec2 distort_uv = uv * DistortScale;
    // Evaluamos la distorsión de forma estática en Z = 0.0
    vec2 distort = vec2(
        snoise(vec3(distort_uv, 0.0)), 
        snoise(vec3(distort_uv + vec2(31.415, 57.123), 0.0))
    );
    // Corrección estricta de sustracción vectorial
    uv += (distort - vec2(0.5)) * DistortIntensity;
}

// --- EVALUACIÓN DEL RUIDO ---
float main_intensity = getSimplexValue(uv);

// Cálculo de derivadas numéricas dinámicas usando diferencias finitas centrales de alta fidelidad
float h = 0.002; // Paso de muestreo óptimo
float val_x = getSimplexValue(uv + vec2(h, 0.0));
float val_y = getSimplexValue(uv + vec2(0.0, h));

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