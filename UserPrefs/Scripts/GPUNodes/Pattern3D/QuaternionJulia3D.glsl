// Quaternion Julia 3D Fractal Pattern
// Evaluates the 4D Julia set (sliced in 3D) for alien, organic-tech fractal structures.

void main(
    in vec3 FragCoord(value= 1, knot= ioFragCoord, expression= R=(V*K), min= -10.0, max= 10.0),
    in float Scale(value= 1.0, min= 0.01, max= 100.0, expression= R=(V*K)),
    in float CX(value= -0.323, min= -2.0, max= 2.0, expression= R=(V*K)),
    in float CY(value= 0.85, min= -2.0, max= 2.0, expression= R=(V*K)),
    in float CZ(value= 0.0, min= -2.0, max= 2.0, expression= R=(V*K)),
    in float CW(value= 0.0, min= -2.0, max= 2.0, expression= R=(V*K)),
    in float Iterations(value= 10.0, min= 1.0, max= 20.0, expression= R=(V*K)),
    out float Distance,
    out float IterationCount,
    out vec4 BaseColor
)
{
    vec3 p = FragCoord * Scale;
    
    // Initial 4D quaternion (w=0 for 3D slice)
    vec4 q = vec4(p, 0.0);
    
    // Julia set constant C
    vec4 c = vec4(CX, CY, CZ, CW);
    
    // Distance estimator variables
    float a = 1.0;
    float b = dot(q, q);
    float n = 1.0;
    
    // Iterate the fractal equation Q = Q^2 + C
    for (int i = 0; i < 20; i++) {
        if (float(i) >= Iterations) break;
        
        a *= b;
        
        // Quaternion squaring math:
        // Real part: x^2 - y^2 - z^2 - w^2 = 2x^2 - dot(q,q)
        // Imag part: 2 * x * (y, z, w)
        q = vec4(2.0 * q.x * q.x - b, 2.0 * q.x * q.yzw) + c;
        
        b = dot(q, q);
        
        // Escape condition (radius 2, squared is 4)
        if (b > 4.0) break;
        n += 1.0;
    }
    
    // Standard distance estimator for Julia/Mandelbrot sets: 0.25 * ln(r^2) * r / dr 
    // We use exp2(-n) to mathematically correct the derivative scale (2^n)
    float dist = 0.25 * sqrt(b / a) * exp2(-n) * log(b);
    
    // Tiny offset to make the fractal surface slightly solid instead of infinitely thin
    Distance = dist - 0.005; 
    
    // Output the iteration count so users can use it as a custom mask!
    IterationCount = n;
    
    // Colorizing based on how many iterations it took to escape (fractal depth)
    float iterNorm = clamp(n / Iterations, 0.0, 1.0);
    
    vec3 coreColor = vec3(0.9, 0.6, 0.1); // Glowing core (high iterations)
    vec3 edgeColor = vec3(0.1, 0.2, 0.4); // Deep fractal shell (low iterations)
    
    BaseColor = vec4(mix(coreColor, edgeColor, iterNorm), 1.0);
}
