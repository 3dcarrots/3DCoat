// ============================================================================
// CONFIGURACIÓN DE NODOS EN 3DCOAT (NGL)
// ============================================================================
in vec2 UVCoord(knot = ioUV); // Coordenadas UV de entrada

// Deslizadores registrados de forma segura
in float Frequency(value = 0.1, min = 0.0, max = 200.0); // Rango unificado de 0 a 200
in float Sharpness(value = 0.0, min = 0.0, max = 1.0); // Control de contraste / Dureza general

// Switches ON/OFF (Checkboxes)
#bool NonSquareExpansion    // True = Compensa deformación en formatos no cuadrados
#bool Invert                // True = Invierte la máscara final y normales

// ============================================================================
// SALIDAS (Conectores del nodo) - Mantenidos estrictamente en líneas 17 a 20
// ============================================================================
out vec3 Color;       // Salida RGB de color (Línea 17)
out vec3 Normal;      // Vector normal en espacio tangente (Línea 18)
out float NonColor;   // Patrón procedural en escala de grises (Línea 19)
out float Opacity;    // Máscara de opacidad para transparencia (Línea 20)

// ============================================================================
// CONTROLES ADICIONALES (Rango de 0 a 200 unificado para precisión de sliders)
// ============================================================================
in float Scale(value = 0.5, min = 0.1, max = 1.0); // Rango de 0 a 1
in float DeformX(value = 0.0, min = 0.0, max = 1.0); // Rango de 0 a 1
in float DeformY(value = 0.0, min = 0.0, max = 1.0); // Rango de 0 a 1
in float OffsetX(value = 0.0, min = 0.0, max = 90.0); // Rango de 0 a 90
in float OffsetY(value = 0.0, min = 0.0, max = 90.0); // Rango de 0 a 90
in float Jitter(value = 0.0, min = 0.0, max = 1.0);  // Deformación de celdas (Clásico de Worley)

// Selectores desplegables de tipo ENUM (Copia la interfaz de SimpleMaterial)
#enum Silhouette Circle Diamond Square Minkowski
in float CellProfile(value = 0.3, min = 0.3, max = 5.0); // Exponente Minkowski (P)
#enum Curvature Cells Concave Borders
#enum ColorMode Faded Contour ColorID

// ============================================================================
// FUNCIONES AUXILIARES
// ============================================================================

// Definimos las opciones de los ENUM como constantes numéricas para compilar de forma segura
#define Circle 0
#define Diamond 1
#define Square 2
#define Minkowski 3

#define Cells 0
#define Concave 1
#define Borders 2

#define Faded 0
#define Contour 1
#define ColorID 2

// Calcula la distancia de un punto basada en la silueta seleccionada en el menú desplegable
float getDistance(vec2 d, float p) {
    if (Silhouette == Circle) {
        return length(d); // Euclidiana
    } else if (Silhouette == Diamond) {
        return abs(d.x) + abs(d.y); // Manhattan (Rombo)
    } else if (Silhouette == Square) {
        return max(abs(d.x), abs(d.y)); // Chebyshev (Cuadrado)
    } else {
        // Minkowski (Seguro contra indeterminaciones matemáticas)
        return pow(pow(max(abs(d.x), 0.0001), p) + pow(max(abs(d.y), 0.0001), p), 1.0 / max(p, 0.001));
    }
}

// Ejecuta la cuadrícula de búsqueda 2x2 Worley calculando F1, F2 e ID de celda
vec4 computeCellular(vec2 P) {
    vec2 Pi = floor(P);
    vec2 Pf = P - Pi;

    // Calculamos las tablas de hash analíticas (Semilla removida para evitar errores)
    vec4 Pt = vec4( Pi.xy, Pi.xy + 1.0 );
    Pt = Pt - floor(Pt * ( 1.0 / 71.0 )) * 71.0;
    Pt += vec2( 26.0, 161.0 ).xyxy;
    Pt *= Pt;
    Pt = Pt.xzxz * Pt.yyww;
    vec4 hash_x = fract( Pt * ( 1.0 / 951.135664 ) );
    vec4 hash_y = fract( Pt * ( 1.0 / 642.949883 ) );

    hash_x = hash_x * 2.0 - 1.0;
    hash_y = hash_y * 2.0 - 1.0;
    
    hash_x = ( ( hash_x * hash_x * hash_x ) - sign( hash_x ) ) * Jitter + vec4( 0.0, 1.0, 0.0, 1.0 );
    hash_y = ( ( hash_y * hash_y * hash_y ) - sign( hash_y ) ) * Jitter + vec4( 0.0, 0.0, 1.0, 1.0 );

    vec2 p0 = vec2(hash_x.x, hash_y.x);
    vec2 p1 = vec2(hash_x.y, hash_y.y);
    vec2 p2 = vec2(hash_x.z, hash_y.z);
    vec2 p3 = vec2(hash_x.w, hash_y.w);

    // Llamada unificada y limpia con 2 parámetros
    float dist0 = getDistance(Pf - p0, CellProfile);
    float dist1 = getDistance(Pf - p1, CellProfile);
    float dist2 = getDistance(Pf - p2, CellProfile);
    float dist3 = getDistance(Pf - p3, CellProfile);

    float F1 = dist0;
    float F2 = dist1;
    float F3 = dist2;
    float F4 = dist3;

    // Ordenamiento analítico de distancias
    if (F1 > F2) { float tmp = F1; F1 = F2; F2 = tmp; }
    if (F3 > F4) { float tmp = F3; F3 = F4; F4 = tmp; }
    if (F1 > F3) { float tmp = F1; F1 = F3; F3 = tmp; }
    if (F2 > F4) { float tmp = F2; F2 = F4; F4 = tmp; }
    if (F2 > F3) { float tmp = F2; F2 = F3; F3 = tmp; }

    vec2 closest_center = p0;
    if (F1 == dist1) closest_center = p1;
    else if (F1 == dist2) closest_center = p2;
    else if (F1 == dist3) closest_center = p3;

    vec2 absolute_cell = Pi + closest_center;
    return vec4(F1, F2, absolute_cell.x, absolute_cell.y);
}

// Retorna la intensidad final y opcionalmente el color estable para la celda
float getCellularValue(vec2 P, out vec3 cellColor) {
    vec4 cellData = computeCellular(P);
    float F1 = cellData.x;
    float F2 = cellData.y;
    vec2 absCell = cellData.zw;

    float baseValue = 0.0;
    if (Curvature == Cells) {
        baseValue = F1; // F1
    } else if (Curvature == Concave) {
        baseValue = F2; // F2
    } else {
        baseValue = F2 - F1; // Borders (F2 - F1)
    }

    float normValue = clamp(baseValue, 0.0, 1.0);

    cellColor = fract(sin(vec3(dot(absCell, vec2(127.1, 311.7)),
                               dot(absCell, vec2(269.5, 183.3)),
                               dot(absCell, vec2(419.2, 371.9)))) * 43758.5453);

    float finalVal = 0.0;
    if (ColorMode == Faded) {
        // MODO 0: Degradado suave regulado por Sharpness
        float soft_width = max((1.0 - Sharpness) * 0.5, 0.0001);
        float edge0 = max(0.5 - soft_width, 0.0);
        float edge1 = min(0.5 + soft_width, 1.0);
        float t = clamp((normValue - edge0) / (edge1 - edge0), 0.0, 1.0);
        finalVal = t * t * (3.0 - 2.0 * t);
    } else if (ColorMode == Contour) {
        // MODO 1: Contorno con valores por defecto fijos por eliminación de parámetros
        float border_thick = 0.05;
        float border_soft = 0.01;
        finalVal = smoothstep(border_thick, border_thick + border_soft, normValue);
    } else {
        // MODO 2: Luminancia del color ID de la celda
        finalVal = dot(cellColor, vec3(0.299, 0.587, 0.114));
    }

    return finalVal;
}

// Función ligera de consulta de altura dedicada para derivadas numéricas
float getCellularValueHeight(vec2 P) {
    vec4 cellData = computeCellular(P);
    float F1 = cellData.x;
    float F2 = cellData.y;
    vec2 absCell = cellData.zw;

    float baseValue = 0.0;
    if (Curvature == Cells) {
        baseValue = F1;
    } else if (Curvature == Concave) {
        baseValue = F2;
    } else {
        baseValue = F2 - F1;
    }

    float normValue = clamp(baseValue, 0.0, 1.0);

    float finalVal = 0.0;
    if (ColorMode == Faded) {
        float soft_width = max((1.0 - Sharpness) * 0.5, 0.0001);
        float edge0 = max(0.5 - soft_width, 0.0);
        float edge1 = min(0.5 + soft_width, 1.0);
        float t = clamp((normValue - edge0) / (edge1 - edge0), 0.0, 1.0);
        finalVal = t * t * (3.0 - 2.0 * t);
    } else if (ColorMode == Contour) {
        float border_thick = 0.05;
        float border_soft = 0.01;
        finalVal = smoothstep(border_thick, border_thick + border_soft, normValue);
    } else {
        vec3 cellColor = fract(sin(vec3(dot(absCell, vec2(127.1, 311.7)),
                                   dot(absCell, vec2(269.5, 183.3)),
                                   dot(absCell, vec2(419.2, 371.9)))) * 43758.5453);
        finalVal = dot(cellColor, vec3(0.299, 0.587, 0.114));
    }

    return finalVal;
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

vec3 cellColor = vec3(0.0);
float main_intensity = getCellularValue(uv, cellColor);

// Cálculo de derivadas numéricas por diferencias finitas centrales
float h = 0.002;
float val_x = getCellularValueHeight(uv + vec2(h, 0.0));
float val_y = getCellularValueHeight(uv + vec2(0.0, h));

vec2 final_derivatives = vec2(val_x - main_intensity, val_y - main_intensity) * (1.0 / h);
vec3 final_normal = normalize(vec3(-final_derivatives.x, -final_derivatives.y, 1.0));

#if Invert
    main_intensity = 1.0 - main_intensity;
    final_derivatives = -final_derivatives;
    final_normal = normalize(vec3(-final_derivatives.x, -final_derivatives.y, 1.0));
#endif

// Asignación estática según la opción de ColorMode
if (ColorMode == ColorID) {
    Color = cellColor;
} else {
    Color = vec3(main_intensity);
}

Normal = final_normal;                     // Línea 18
NonColor = main_intensity;                 // Línea 19
Opacity = main_intensity;                  // Línea 20