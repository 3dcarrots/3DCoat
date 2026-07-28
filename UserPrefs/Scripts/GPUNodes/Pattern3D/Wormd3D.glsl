// ============================================================================
// CONFIGURACIÓN DE NODOS EN 3DCOAT (NGL)
// ============================================================================
// Selector de proyección nativa de 3DCoat (Evita que el shader se muestre blanco en voxeles)
#enum Projection UV Top Left Front
#define UV ioUV.xyxy
#define Top ioFragCoord.xzxz
#define Left ioFragCoord.zyzy
#define Front ioFragCoord.xyxy

// Enlace global a la proyección seleccionada
in vec4 fragCoord(knot = Projection);

// Menú desplegable nativo para el tipo de patrón
#enum Pattern Worms Worms2 Voronoi Cells Micro Noise

// Parámetros generales y dimensionales actualizados con tus límites exactos
in float Luminance(value = 0.8, min = 0.1, max = 10.0); // Luminance
in float Midtones(value = 1.0, min = 0.1, max = 3.0);   // Midtones
in float Shadows(value = 0.0, min = 0.0, max = 2.0);    // Shadows
in float Scale(value = 1.0, min = 0.1, max = 20.0);     // Scale
in float Scale_X(value = 0.1, min = 0.1, max = 10.0);   // Scale X
in float Scale_Y(value = 0.1, min = 0.1, max = 10.0);   // Scale Y
in float Scale_Z(value = 0.1, min = 0.1, max = 10.0);   // Scale Z
in float DistortIntensity(value = 0.0, min = 0.0, max = 5.0); // Distort Intensity
in float DistortScale(value = 2.0, min = 0.1, max = 10.0); // Distort Scale
in float Contrast(value = 1.0, min = 0.0, max = 5.0); // Contrast

// ============================================================================
// SALIDAS ÚNICAS (Únicos conectores visibles en el Node Editor)
// ============================================================================
out vec3 Color;       // Salida RGB de color (Muestra el patrón seleccionado)
out vec3 Normal;      // Vector normal en espacio tangente (Calculado para el patrón seleccionado)
out float NonColor;   // Patrón procedural seleccionado en escala de grises
out float Opacity;    // Máscara de opacidad para el patrón seleccionado

// ============================================================================
// FUNCIONES AUXILIARES DE RUIDO
// ============================================================================

/* discontinuous pseudorandom uniformly distributed in [-0.5, +0.5]^3 */
vec3 random3(vec3 c) {
	float j = 4096.0*sin(dot(c,vec3(17.0, 59.4, 15.0)));
	vec3 r;
	r.z = fract(512.0*j);
	j *= .125;
	r.x = fract(512.0*j);
	j *= .125;
	r.y = fract(512.0*j);
	return r-0.5;
}

/* skew constants for 3d simplex functions */
float F3 =  0.3333333;
float G3 =  0.1666667;

/* 3d simplex noise */
vec4 simplex3d(vec3 p) {
	 vec3 s = floor(p + dot(p, vec3(F3)));
	 vec3 x = p - s + dot(s, vec3(G3));
	 
	 vec3 e = step(vec3(0.0), x - x.yzx);
	 vec3 i1 = e*(1.0 - e.zxy);
	 vec3 i2 = 1.0 - e.zxy*(1.0 - e);
	 	
	 vec3 x1 = x - i1 + G3;
	 vec3 x2 = x - i2 + 2.0*G3;
	 vec3 x3 = x - 1.0 + 3.0*G3;
	 
	 vec4 w, d;
	 
	 w.x = dot(x, x);
	 w.y = dot(x1, x1);
	 w.z = dot(x2, x2);
	 w.w = dot(x3, x3);
	 
	 w = max(0.6 - w, 0.0);
	 
	 d.x = dot(random3(s), x);
	 d.y = dot(random3(s + i1), x1);
	 d.z = dot(random3(s + i2), x2);
	 d.w = dot(random3(s + 1.0), x3);
	 
	 w *= w;
	 w *= w;
	 d *= w;
	 
	 return 70.*d;
}

vec4 variations(vec4 n, float luminanceVal) {
    vec4 an = abs(n);
    vec4 s = vec4(
        dot( n, vec4(1.) ),
        dot( an,vec4(1.) ),
        length(n),
        max(max(max(an.x, an.y), an.z), an.w) );
    
    float t = max(0.001, luminanceVal);
    
    return vec4(
		// worms (Canal X)
		max(0., 1.25*( s.y*t-abs(s.x) )/t),
		// cells (Canal Y)
    	pow( (1.+t)*( (1.-t)+(s.y-s.w/t)*t), 2.),
		// micro y noise (Canal Z)
		0.75 * s.y,
		// Canal W (Auxiliar)
    	.5+.5*s.x);
}

/* const matrices for 3d rotation */
mat3 rot1 = mat3(-0.37, 0.36, 0.85,-0.14,-0.93, 0.34,0.92, 0.01,0.4);
mat3 rot2 = mat3(-0.55,-0.39, 0.74, 0.33,-0.91,-0.24,0.77, 0.12,0.63);
mat3 rot3 = mat3(-0.71, 0.52,-0.47,-0.08,-0.72,-0.68,-0.7,-0.45,0.56);

/* directional artifacts can be reduced by rotating each octave */
vec4 simplex3d_fractal(vec3 m, float luminanceVal) {
    return   0.5333333*variations( simplex3d(m*rot1), luminanceVal )
			+0.2666667*variations( simplex3d(2.0*m*rot2), luminanceVal )
			+0.1333333*variations( simplex3d(4.0*m*rot3), luminanceVal )
			+0.0666667*variations( simplex3d(8.0*m), luminanceVal );
}

// ============================================================================
// PROCESAMIENTO DE SEÑAL Y COORDENADAS
// ============================================================================

// Calcula las coordenadas 3D dinámicamente según la proyección elegida (UV o espacial)
vec3 getCoords() {
    vec3 coord = fragCoord.xyz;
    
    float fx = (Scale_X * 10.0) * Scale;
    float fy = (Scale_Y * 10.0) * Scale;
    float fz = (Scale_Z * 10.0) * Scale;
    
    vec3 p3 = vec3(coord.x * fx, coord.y * fy, coord.z * fz);
    
    // Domain Warping / Distorsión espacial
    if (DistortIntensity > 0.001) {
        vec3 distort_uv = p3 * DistortScale;
        vec3 distort = simplex3d(distort_uv).xyz;
        p3 += distort * DistortIntensity;
    }
    return p3;
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

// Evalúa y retorna el valor de ruido para el patrón seleccionado (para derivadas de normales)
float getSample(vec2 uv_val) {
    vec3 p3 = getCoords();
    
    // Calibración exacta para que Luminance = 0.8 coincida con el umbral original de 0.45
    float t_var = max(0.001, Luminance * 0.56);
    vec4 s1 = variations(simplex3d(p3 * 16.0), t_var);
    
    float result = processNoiseValue(s1.x); // Default Worms
    
    #ifdef Pattern_Worms2
        vec4 s2 = simplex3d_fractal(p3 * 8.0 + 8.0, t_var);
        result = processNoiseValue(s2.x);
    #endif
    #ifdef Pattern_Voronoi
        result = processNoiseValue(s1.y);
    #endif
    #ifdef Pattern_Cells
        vec4 s2 = simplex3d_fractal(p3 * 8.0 + 8.0, t_var);
        result = processNoiseValue(s2.y);
    #endif
    #ifdef Pattern_Micro
        result = processNoiseValue(s1.z);
    #endif
    #ifdef Pattern_Noise
        vec4 s2 = simplex3d_fractal(p3 * 8.0 + 8.0, t_var);
        result = processNoiseValue(s2.z);
    #endif
    
    return result;
}

// ============================================================================
// EJECUCIÓN PRINCIPAL
// ============================================================================

void main() {
    // --- EVALUACIÓN DE LAS VARIACIONES INDIVIDUALES ---
    vec3 p3 = getCoords();
    
    // El valor por defecto de Luminance (0.8) equivale al umbral original de Shadertoy (0.45)
    float t_var = max(0.001, Luminance * 0.56);
    vec4 s1 = variations(simplex3d(p3 * 16.0), t_var);
    vec4 s2 = simplex3d_fractal(p3 * 8.0 + 8.0, t_var);

    float l_Worms   = processNoiseValue(s1.x);
    float l_Worms2  = processNoiseValue(s2.x);
    float l_Voronoi = processNoiseValue(s1.y);
    float l_Cells   = processNoiseValue(s2.y);
    float l_Micro   = processNoiseValue(s1.z);
    float l_Noise   = processNoiseValue(s2.z);

    // --- SELECCIÓN DE LA INTENSIDAD PRINCIPAL (Lógica plana ultracompatible con 3DCoat) ---
    float main_intensity = l_Worms; // Valor por defecto

    #ifdef Pattern_Worms2
        main_intensity = l_Worms2;
    #endif
    #ifdef Pattern_Voronoi
        main_intensity = l_Voronoi;
    #endif
    #ifdef Pattern_Cells
        main_intensity = l_Cells;
    #endif
    #ifdef Pattern_Micro
        main_intensity = l_Micro;
    #endif
    #ifdef Pattern_Noise
        main_intensity = l_Noise;
    #endif

    // Muestreo dinámico en el espacio tridimensional de la proyección para el cálculo de normales
    float h = 0.002; // Paso de muestreo óptimo
    float val_x = getSample(UVCoord + vec2(h, 0.0));
    float val_y = getSample(UVCoord + vec2(0.0, h));

    vec2 final_derivatives = vec2(val_x - main_intensity, val_y - main_intensity) * (1.0 / h);
    vec3 final_normal = normalize(vec3(-final_derivatives.x, -final_derivatives.y, 1.0));

    // --- ASIGNACIÓN DE SALIDAS ESTÁNDAR ÚNICAS ---
    Color = vec3(main_intensity);
    Normal = final_normal;
    NonColor = main_intensity;
    Opacity = main_intensity;
}