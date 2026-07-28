// Smooth Lattice 3D Pattern
// Includes cubic and tetrahedral/octahedral diagonal cross-bracing (Triangle Grid)
// Adapted from Shadertoy "3D square grid with nodes" by Vinicius Graciano Santos

// Smooth minimum function (by iq)
float smin(float a, float b, float k)
{
    float h = clamp(0.5 + 0.5 * (b - a) / max(k, 0.0001), 0.0, 1.0);
    return mix(b, a, h) - k * h * (1.0 - h);
}

void main(
    in vec3 FragCoord(value= 1, knot= ioFragCoord, expression= R=(V*K), min= -10.0, max= 10.0),
    in float Scale(value= 1.0, min= 0.01, max= 100.0, expression= R=(V*K)),
    in float RepeatSize(value= 10.0, min= 0.1, max= 100.0, expression= R=(V*K)),
    in float NodeRadius(value= 2.25, min= 0.0, max= 10.0, expression= R=(V*K)),
    in float LinkRadius(value= 1.0, min= 0.0, max= 10.0, expression= R=(V*K)),
    in float DiagonalRadius(value= 0.0, min= 0.0, max= 10.0, expression= R=(V*K)),
    in float Smoothness(value= 0.5, min= 0.0, max= 5.0, expression= R=(V*K)),
    out float Distance,
    out vec4 BaseColor
)
{
    vec3 p = FragCoord * Scale;
    
    // Repeat space to create the lattice grid
    // NGL Rule: explicitly cast float to vec3 for modulo and subtraction
    p = mod(p, vec3(RepeatSize)) - vec3(RepeatSize * 0.5);
    
    // Distance to the node sphere at the center of the cell
    float dist = length(p) - NodeRadius;
    
    // Distance to the three cylindrical links along the X, Y, and Z axes (Cubic frame)
    if (LinkRadius > 0.0) {
        float dLinkX = length(p.yz);
        float dLinkY = length(p.xz);
        float dLinkZ = length(p.xy);
        float dCubic = min(dLinkX, min(dLinkY, dLinkZ)) - LinkRadius;
        dist = smin(dist, dCubic, Smoothness);
    }
    
    // Distance to the face diagonals (Octet-truss / Triangle grid cross-bracing)
    if (DiagonalRadius > 0.0) {
        float dDiag1 = sqrt(p.z*p.z + 0.5*(p.x - p.y)*(p.x - p.y));
        float dDiag2 = sqrt(p.z*p.z + 0.5*(p.x + p.y)*(p.x + p.y));
        float dDiag3 = sqrt(p.y*p.y + 0.5*(p.x - p.z)*(p.x - p.z));
        float dDiag4 = sqrt(p.y*p.y + 0.5*(p.x + p.z)*(p.x + p.z));
        float dDiag5 = sqrt(p.x*p.x + 0.5*(p.y - p.z)*(p.y - p.z));
        float dDiag6 = sqrt(p.x*p.x + 0.5*(p.y + p.z)*(p.y + p.z));
        
        float dCross = min(min(min(dDiag1, dDiag2), min(dDiag3, dDiag4)), min(dDiag5, dDiag6)) - DiagonalRadius;
        dist = smin(dist, dCross, Smoothness);
    }
    
    Distance = dist;
    
    // Simple coloring based on distance from the node center
    vec3 colorSphere = vec3(0.3, 0.5, 0.7);
    vec3 colorLinks = vec3(0.7, 0.6, 0.4);
    
    // Calculate a factor from 0.0 to 1.0 based on how close we are to the center vs the links
    float mixFactor = clamp(length(p) / max(NodeRadius, 0.001), 0.0, 1.0);
    
    vec3 col = mix(colorSphere, colorLinks, mixFactor);
    BaseColor = vec4(col, 1.0);
}
