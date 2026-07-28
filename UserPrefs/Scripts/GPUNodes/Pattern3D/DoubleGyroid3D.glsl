// Double Intertwined Gyroids 3D Pattern

// Helper function to evaluate the gyroid implicit surface equation
float evaluateGyroid(vec3 p) {
    // Math formula: cos(x)*sin(y) + cos(y)*sin(z) + cos(z)*sin(x)
    vec3 c = cos(p);
    vec3 s = sin(vec3(p.z, p.x, p.y));
    return dot(c, s);
}

void main(
    in vec3 FragCoord(value= 1, knot= ioFragCoord, expression= R=(V*K), min= -10.0, max= 10.0),
    in float Scale(value= 1.0, min= 0.01, max= 100.0, expression= R=(V*K)),
    in float Phase(value= 0.0, min= -10.0, max= 10.0, expression= R=(V*K)),
    in float IsoValue(value= 1.0, min= -2.0, max= 2.0, expression= R=(V*K)),
    in float Thickness(value= 0.0, min= -1.0, max= 1.0, expression= R=(V*K)),
    out float Distance,
    out float GyroidIndex,
    out vec4 BaseColor
)
{
    // Apply scaling and phase shift (animation)
    // NGL Rule: explicitly cast float to vec3 for addition
    vec3 pos = FragCoord * Scale + vec3(Phase);
    
    // Evaluate the first gyroid surface
    float gyroid1 = evaluateGyroid(pos) + IsoValue;
    
    // Evaluate the second gyroid surface
    // Shifting by PI along the Z axis creates an inverted, non-intersecting interlocking mesh
    vec3 shiftOffset = vec3(0.0, 0.0, 3.14159265359);
    float gyroid2 = evaluateGyroid(pos - shiftOffset) + IsoValue;
    
    // Combine the two surfaces using minimum distance
    float minDist;
    float closestIndex;
    
    if (gyroid1 < gyroid2) {
        minDist = gyroid1;
        closestIndex = 1.0;
    } else {
        minDist = gyroid2;
        closestIndex = 2.0;
    }
    
    // Final SDF distance with user-defined thickness adjustment
    Distance = minDist - Thickness;
    GyroidIndex = closestIndex;
    
    // Assign colors based on which gyroid surface we are closest to
    vec3 color1 = vec3(0.25, 0.45, 0.85); // Blueish
    vec3 color2 = vec3(0.85, 0.35, 0.25); // Reddish
    
    vec3 finalColor = (closestIndex == 1.0) ? color1 : color2;
    
    // Add some textural variation (spots) on the surface to break up the solid color
    float spots = cos(pos.x * 12.0) + cos(pos.y * 12.0) + cos(pos.z * 12.0);
    finalColor *= (spots > 1.5) ? 1.0 : 0.7;
    
    BaseColor = vec4(finalColor, 1.0);
}
