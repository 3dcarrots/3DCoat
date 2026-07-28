// Organic Sponge 3D Pattern (Fractal Gyroid)
// Adapted from the organic wall pattern in Shadertoy "Lava Tubes"

// Commutative smooth minimum function
float smin(float a, float b, float k){
   float f = max(0.0, 1.0 - abs(b - a) / max(k, 0.0001));
   return min(a, b) - k * 0.25 * f * f;
}

void main(
    in vec3 FragCoord(value= 1, knot= ioFragCoord, expression= R=(V*K), min= -10.0, max= 10.0),
    in float Scale(value= 1.0, min= 0.01, max= 100.0, expression= R=(V*K)),
    in float IsoValue(value= 0.75, min= -5.0, max= 5.0, expression= R=(V*K)),
    in float DetailScale(value= 1.0, min= 0.0, max= 5.0, expression= R=(V*K)),
    out float Distance,
    out vec4 BaseColor
)
{
    vec3 p = FragCoord * Scale;
    
    // Scale up coordinates to match the mathematical period roughly
    vec3 q = p * 3.14159265;
    
    // Layer 1: Base low-frequency chaotic gyroid
    // By using different divisors for cos and sin (2.0 vs 2.5), 
    // we break the perfect symmetry of a normal gyroid and create an organic, non-repeating structure.
    float cav1 = dot(cos(q / 2.0), sin(vec3(q.y, q.z, q.x) / 2.5));
    
    // Layer 2: Medium-frequency chaotic gyroid
    float cav2 = dot(cos(q / 6.5), sin(vec3(q.y, q.z, q.x) / 4.5));
    
    // Combine layers smoothly using smin
    float cav = smin(cav1, cav2 / 2.0, 2.0);
    
    // Layer 3: High-frequency perturbation (adds small bumps and ridges)
    // NGL Rule: Explicit cast float to vec3 for multiplication
    float n = 0.0;
    if (DetailScale > 0.0) {
        n = dot(sin(q / 3.0 + cos(vec3(q.y, q.z, q.x) / 6.0)), vec3(0.166)) * DetailScale;
    }
    
    // Final SDF distance calculation
    // -cav creates the hollow/solid inversion, IsoValue controls porosity
    Distance = -cav - IsoValue + n;
    
    // Simple coloring based on depth
    vec3 colDeep = vec3(0.15, 0.05, 0.02); // Dark lava/crevice color
    vec3 colSurface = vec3(0.8, 0.7, 0.6); // Light pumice/rock color
    
    // Map the internal structure to a 0-1 mix factor based on distance
    float mixFactor = clamp((Distance + 1.0) * 0.5, 0.0, 1.0);
    BaseColor = vec4(mix(colDeep, colSurface, mixFactor), 1.0);
}
