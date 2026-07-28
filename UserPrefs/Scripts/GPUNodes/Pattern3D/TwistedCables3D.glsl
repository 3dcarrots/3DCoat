// Twisted Cables 3D Pattern
// Generates twisted ropes, muscle fibers, wires and roots using polar modulo repetition.

float smin(float a, float b, float k) {
    float h = clamp(0.5 + 0.5 * (b - a) / max(k, 0.0001), 0.0, 1.0);
    return mix(b, a, h) - k * h * (1.0 - h);
}

// Polar space folding function (splits space into N radial segments)
void moda(inout vec2 p, float repetitions) {
    float angle = 6.28318530718 / max(repetitions, 1.0);
    float a = atan(p.y, p.x) + angle / 2.0;
    a = mod(a, angle) - angle / 2.0;
    p = vec2(cos(a), sin(a)) * length(p);
}

void main(
    in vec3 FragCoord(value= 1, knot= ioFragCoord, expression= R=(V*K), min= -10.0, max= 10.0),
    in float Scale(value= 1.0, min= 0.01, max= 100.0, expression= R=(V*K)),
    in float Strands(value= 5.0, min= 1.0, max= 20.0, expression= R=(V*K)),
    in float Radius(value= 0.2, min= 0.01, max= 2.0, expression= R=(V*K)),
    in float Spread(value= 0.3, min= 0.0, max= 3.0, expression= R=(V*K)),
    in float Twist(value= 1.0, min= -5.0, max= 5.0, expression= R=(V*K)),
    in float SubStrands(value= 0.0, min= 0.0, max= 12.0, expression= R=(V*K)),
    in float Smoothness(value= 0.1, min= 0.0, max= 1.0, expression= R=(V*K)),
    out float Distance,
    out vec4 BaseColor
)
{
    vec3 p = FragCoord * Scale;
    
    // Core bundle
    vec3 p1 = p;
    
    // Apply macro twist along the Z axis
    if (Twist != 0.0) {
        float c = cos(p1.z * Twist);
        float s = sin(p1.z * Twist);
        // Standard 2D rotation matrix
        p1.xy = mat2(c, -s, s, c) * p1.xy;
    }
    
    // Polar repeat to create N identical strands radially
    moda(p1.xy, floor(max(Strands, 1.0)));
    
    // Spread strands outwards from the center of the bundle
    p1.x -= Spread;
    
    // Distance to the main strands (which are now just simple cylinders at the origin of their folded space)
    float d1 = length(p1.xy) - Radius;
    float dist = d1;
    
    vec3 colMain = vec3(0.15, 0.15, 0.15); // Dark cable/muscle color
    vec3 colSub = vec3(0.6, 0.4, 0.1);    // Copper/bright sub-wire color
    vec3 col = colMain;
    
    // Optional Layer 2: Sub-strands (smaller wires/fibers twisting around the main strands)
    if (SubStrands > 0.0) {
        // Start relative to the center of the current main strand
        vec3 p2 = p1; 
        
        // Twist in the opposite direction, significantly faster, to wrap around the main strand
        float subTwist = Twist * -4.0; 
        float sc = cos(p2.z * subTwist);
        float ss = sin(p2.z * subTwist);
        p2.xy = mat2(sc, -ss, ss, sc) * p2.xy;
        
        // Fold space again radially around the local strand
        moda(p2.xy, floor(max(SubStrands, 1.0)));
        
        // Wrap them around the surface of the main strand
        p2.x -= Radius * 1.05; 
        
        // Sub-strands are much thinner
        float subRadius = Radius * 0.25;
        float d2 = length(p2.xy) - subRadius;
        
        // Smoothly merge the sub-strands with the main strand
        dist = smin(d1, d2, Smoothness);
        
        // Smooth color blending based on which SDF layer is closest
        float blend = clamp(0.5 + 0.5 * (d1 - d2) / max(Smoothness, 0.0001), 0.0, 1.0);
        col = mix(colMain, colSub, blend);
    }
    
    Distance = dist;
    BaseColor = vec4(col, 1.0);
}
