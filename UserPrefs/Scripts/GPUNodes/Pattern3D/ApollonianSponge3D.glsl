// Apollonian Sponge 3D Fractal Pattern
// Creates infinite architectural and intricate lattice structures using spherical inversion.
// Based on Kali-set and Kleinian group fractal formulas.

void main(
    in vec3 FragCoord(value= 1, knot= ioFragCoord, expression= R=(V*K), min= -10.0, max= 10.0),
    in float Scale(value= 1.0, expression= R=(V*K), min= 0.01, max= 100.0),
    in float InversionScale(value= 1.5, expression= R=(V*K), min= 0.1, max= 3.0),
    in float ModSize(value= 2.0, expression= R=(V*K), min= 0.1, max= 10.0),
    in float Thickness(value= 0.01, expression= R=(V*K), min= 0.0, max= 0.5),
    in float Iterations(value= 7.0, expression= R=(V*K), min= 1.0, max= 15.0),
    out float Distance,
    out float IterationCount,
    out vec4 BaseColor
)
{
    // NGL inputs are passed as vec4 internally, so we must swizzle them to their intended types.
    vec3 p = FragCoord * Scale;
    
    // Scale tracking variable for exact distance estimation
    float s = 1.0;
    
    // NGL explicit casts for modulo arithmetic
    vec3 modWrap = vec3(ModSize);
    vec3 modOffset = vec3(ModSize * 0.5);
    
    float n = 0.0;
    
    // Iterated Function System (KIFS) Loop
    for (int i = 0; i < 15; i++) {
        if (float(i) >= Iterations) break;
        
        // Fold space: creates the infinite repeating lattice grid
        p = mod(p - modOffset, modWrap) - modOffset;
        
        // Spherical inversion: the core of Apollonian/Kali fractals
        // We clamp the dot product to avoid division by zero explosions
        float d2 = max(dot(p, p), 0.00001);
        float k = InversionScale / d2;
        
        // Apply the mathematical inversion scale to the point and the scale tracker
        p *= k;
        s *= k;
        
        n += 1.0;
    }
    
    // Distance estimator for KIFS fractals:
    Distance = (length(p) / s) - Thickness;
    
    // Output iteration count
    IterationCount = n;
    
    // Colorizing based on structural depth
    float structVal = clamp(length(p) * 0.1, 0.0, 1.0);
    
    vec3 darkCol = vec3(0.05, 0.1, 0.15);
    vec3 lightCol = vec3(0.8, 0.85, 0.9);
    
    BaseColor = vec4(mix(darkCol, lightCol, structVal), 1.0);
}
