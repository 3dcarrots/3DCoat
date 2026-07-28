// Cell-Faces Truchet 3D Pattern
// Adapted from Shadertoy "cell-faces truchet" by FabriceNeyret2

void main(
    in vec3 FragCoord(value= 1, knot= ioFragCoord, expression= R=(V*K), min= -10.0, max= 10.0),
    in float Scale(value= 1.0, min= 0.01, max= 100.0, expression= R=(V*K)),
    in float Thickness(value= 0.05, min= 0.0, max= 0.5, expression= R=(V*K)),
    in float Seed(value= 0.0, min= -100.0, max= 100.0, expression= R=(V*K)),
    out float Distance,
    out float FaceIndex,
    out float Checkered,
    out vec4 BaseColor
)
{
    vec3 q = FragCoord * Scale;
    vec3 I = ceil(q);
    
    // Convert to cell local space [-0.5, 0.5]
    // NGL Rule: explicitly cast float to vec3 for subtraction
    q = fract(q) - vec3(0.5); 
    vec3 a = abs(q);
    
    int c = 0;
    
    // Find closest cell face and swizzle so that X is always the normal to that face
    if (a.y > max(a.x, a.z)) {
        q = vec3(q.y, q.z, q.x);
        I = vec3(I.y, I.z, I.x);
        c = 1;
    } else if (a.z > max(a.x, a.y)) {
        q = vec3(q.z, q.x, q.y);
        I = vec3(I.z, I.x, I.y);
        c = 2;
    }
    
    // Determine which side of the face we are on
    if (q.x > 0.0) {
        I.x += 1.0;
    }
    
    // Make q.x relative to the face itself (distance to face)
    q.x -= 0.5 * sign(q.x);
    
    // Checkered pattern on the faces
    float s = mod(I.y + I.z, 2.0) - 0.5;
    
    // Random Truchet swap (hash function)
    float rand = fract(10000.0 * sin(dot(I, vec3(12.9898, 78.233, 45.164)) + Seed));
    if (rand > 0.5) {
        q.y = -q.y;
    }
    
    // Map to a single quadrant for the torus arcs
    if (q.y + q.z < 0.0) {
        q.y = -q.y;
        q.z = -q.z;
    }
    
    float t = 1000.0;
    
    // Draw Truchet curve (torus arc) on checkered faces
    if (s > 0.0) {
        // NGL Rule: explicitly cast float to vec2 for subtraction
        t = length(vec2(q.x, length(q.yz - vec2(0.5)) - 0.5)) - Thickness;
    }
    
    // Draw connection spheres at the corners
    a = abs(q);
    if (a.y > a.z) {
        a = vec3(a.x, a.z, a.y);
    }
    a.z -= 0.5;
    
    float sphereRadius = Thickness * 1.2;
    t = min(t, length(a) - sphereRadius);
    
    Distance = t;
    FaceIndex = float(c);
    Checkered = s > 0.0 ? 1.0 : 0.0;
    
    // Colorize based on face orientation and checkered state
    vec3 col = vec3(1.0);
    if (c == 0) col = vec3(0.9, 0.4, 0.4);
    else if (c == 1) col = vec3(0.4, 0.9, 0.4);
    else col = vec3(0.4, 0.4, 0.9);
    
    col *= (s > 0.0 ? 1.0 : 0.6);
    
    BaseColor = vec4(col, 1.0);
}
