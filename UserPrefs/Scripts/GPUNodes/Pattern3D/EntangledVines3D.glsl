// Entangled Vines 3D Pattern
// Adapted from Shadertoy "Entangled Vines"

// Standard smooth minimum function
float smin(float a, float b, float k)
{
    float h = clamp(0.5 + 0.5 * (b - a) / max(k, 0.0001), 0.0, 1.0);
    return mix(b, a, h) - k * h * (1.0 - h);
}

void main(
    in vec3 FragCoord(value= 1, knot= ioFragCoord, expression= R=(V*K), min= -10.0, max= 10.0),
    in float Scale(value= 2.0, min= 0.01, max= 100.0, expression= R=(V*K)),
    in float Radius(value= 0.24, min= 0.01, max= 1.0, expression= R=(V*K)),
    in float Warp(value= 1.0, min= 0.0, max= 5.0, expression= R=(V*K)),
    in float Smoothness(value= 0.25, min= 0.01, max= 2.0, expression= R=(V*K)),
    in float Bumps(value= 0.05, min= 0.0, max= 0.5, expression= R=(V*K)),
    out float Distance,
    out vec4 BaseColor
)
{
    vec3 p = FragCoord * Scale;
    
    // Perturbation functions to warp the cylinders, creating the "entangled" organic look.
    // They use sinusoids of cross-axes to make the cylinders wiggle along their length.
    vec2 perturb1 = vec2(sin(p.z * 2.15 + p.x * 2.35), cos(p.z * 1.15 + p.x * 1.25)) * Warp;
    vec2 perturb2 = vec2(cos(p.z * 1.65 + p.y * 1.75), sin(p.z * 1.4 + p.y * 1.6)) * Warp;
    
    // NGL Rule: explicitly cast float to vec2 for vector math
    vec2 modWrap = vec2(2.0);
    vec2 center = vec2(1.0);
    
    // 3 sets of infinite cylinders aligned roughly along Z, X, and Y axes.
    // They are offset from each other (e.g. vec2(0.25, -0.5)) so they don't perfectly intersect.
    vec2 q1 = mod(p.xy + vec2(0.25, -0.5), modWrap) - center + perturb1 * vec2(0.25, 0.5);
    vec2 q2 = mod(p.yz + vec2(0.25,  0.25), modWrap) - center - perturb1 * vec2(0.25, 0.3);
    vec2 q3 = mod(p.xz + vec2(-0.25, -0.5), modWrap) - center - perturb2 * vec2(0.25, 0.4);
    
    // Evaluate the distances to the 3 warped cylinders
    float s1 = length(q1) - Radius;
    float s2 = length(q2) - Radius;
    float s3 = length(q3) - Radius;
    
    // Combine them smoothly (creates organic webbing where they touch)
    float dist = smin(smin(s1, s3, Smoothness), s2, Smoothness);
    
    // Add high-frequency bumps for a bark/vein texture
    // NGL Rule: Explicitly reconstruct the swizzle to a vec3 for clarity and safety
    vec3 bp = sin(p * 8.0 + cos(vec3(p.y, p.z, p.x) * 8.0));
    float bumpVal = bp.x * bp.y * bp.z * Bumps;
    
    Distance = dist - bumpVal;
    
    // Base Color based on which vine is dominant (rough approximation for coloring)
    vec3 col = vec3(0.35, 0.45, 0.25); // Greenish base
    
    if (s1 < s2 && s1 < s3) {
        col = vec3(0.45, 0.55, 0.25);
    } else if (s2 < s1 && s2 < s3) {
        col = vec3(0.55, 0.45, 0.20);
    } else {
        col = vec3(0.35, 0.55, 0.30);
    }
    
    // Add structural shading to color
    col -= bumpVal * 2.0;
    
    BaseColor = vec4(col, 1.0);
}
