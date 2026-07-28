// ============================================================================
// ENTRADAS (Configurables en la interfaz de 3DCoat)
// ============================================================================
in vec2 UVCoord(knot = ioUV); // Coordenadas UV del modelo

// Parámetros del ruido Voronoise
in float Scale(value = 24.0, min = 1.0, max = 100.0);   // Tamaño de la textura
in float Jitter(value = 1.0, min = 0.0, max = 1.0);     // Jitter/Deformación de celdas (Parámetro U)
in float Softness(value = 1.0, min = 0.0, max = 1.0);   // Suavizado/Fusión de bordes (Parámetro V)

// ============================================================================
// SALIDAS (Conectores del nodo)
// ============================================================================
out vec3 Color;   // Salida RGB
// out float NonColor;  // Salida en escala de grises

// ============================================================================
// FUNCIONES AUXILIARES
// ============================================================================
vec3 hash3( vec2 p )
{
    vec3 q = vec3( dot(p, vec2(127.1, 311.7)), 
				   dot(p, vec2(269.5, 183.3)), 
				   dot(p, vec2(419.2, 371.9)) );
	return fract(sin(q) * 43758.5453);
}

float voronoise( in vec2 p, float u, float v )
{
	float k = 1.0 + 63.0 * pow(1.0 - v, 6.0);

    vec2 i = floor(p);
    vec2 f = fract(p);
    
	vec2 a = vec2(0.0, 0.0);
    for( int y=-2; y<=2; y++ )
    for( int x=-2; x<=2; x++ )
    {
        // Se realiza casteo explícito de float para compatibilidad estricta
        vec2  g = vec2( float(x), float(y) );
		vec3  o = hash3( i + g ) * vec3(u, u, 1.0);
		vec2  d = g - f + o.xy;
		float w = pow( 1.0 - smoothstep(0.0, 1.414, length(d)), k );
		a += vec2(o.z * w, w);
    }
	
    return a.x / a.y;
}

// ============================================================================
// EJECUCIÓN DIRECTA (Cuerpo principal / "Implicit Main")
// ============================================================================

// Evaluamos la función Voronoise usando las entradas configuradas
float noiseVal = voronoise( UVCoord * Scale, Jitter, Softness );

// Asignamos el resultado a las salidas del nodo
Color = vec3(noiseVal);
// Value = noiseVal;