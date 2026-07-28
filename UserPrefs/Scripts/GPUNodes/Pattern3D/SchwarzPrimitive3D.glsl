// Schwarz Primitive (P) 3D Pattern
// Evaluates the Schwarz P Triply Periodic Minimal Surface (TPMS)
// Excellent for creating highly regular, porous architectural, infill, and biological structures.

void main(
    in vec3 FragCoord(value= 1, knot= ioFragCoord, expression= R=(V*K), min= -10.0, max= 10.0),
    in float Scale(value= 3.14159, min= 0.01, max= 100.0, expression= R=(V*K)),
    in float Thickness(value= 0.1, min= 0.0, max= 1.5, expression= R=(V*K)),
    in float IsoValue(value= 0.0, min= -1.5, max= 1.5, expression= R=(V*K)),
    out float Distance,
    out vec4 BaseColor
)
{
    vec3 p = FragCoord * Scale;
    
    // The implicit function for the Schwarz P surface
    float f = cos(p.x) + cos(p.y) + cos(p.z) - IsoValue;
    
    // Analytical gradient of the function (for exact SDF distance estimation)
    // Derivative of cos(x) is -sin(x)
    vec3 g = vec3(-sin(p.x), -sin(p.y), -sin(p.z));
    
    // Normalize the implicit function value by the gradient magnitude to get true distance.
    // We add a tiny value to the gradient length to prevent division by zero at critical points.
    float gradLength = length(g) + 0.01;
    
    // We use abs(f) to create a hollow shell (thickness) instead of a solid half-space.
    // Divide by Scale to ensure the distance matches world space Euclidean units.
    Distance = (abs(f) - Thickness) / gradLength / Scale;
    
    // Structural coloring (darker in the core of the walls, lighter on the surface)
    float structDepth = clamp((abs(f) - Thickness * 0.5) / gradLength, 0.0, 1.0);
    vec3 colDeep = vec3(0.05, 0.15, 0.25);
    vec3 colSurf = vec3(0.8, 0.85, 0.9);
    
    BaseColor = vec4(mix(colSurf, colDeep, structDepth), 1.0);
}
