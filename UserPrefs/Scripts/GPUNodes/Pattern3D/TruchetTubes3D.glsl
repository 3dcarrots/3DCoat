// 3D Truchet Tubes Pattern
// Adapted from Shadertoy "Twisted Tubes"

void main(
    in vec3 FragCoord(value= 1, knot= ioFragCoord, expression= R=(V*K), min= -10.0, max= 10.0),
    in float Scale(value= 1.0, min= 0.01, max= 100.0, expression= R=(V*K)),
    in float Radius(value= 0.15, min= 0.01, max= 0.5, expression= R=(V*K)),
    in float ShapeMutation(value= 0.0, min= 0.0, max= 0.5, expression= R=(V*K)),
    in float Seed(value= 0.0, min= -100.0, max= 100.0, expression= R=(V*K)),
    out float Distance,
    out float TubeIndex,
    out vec4 BaseColor
)
{
    vec3 p = FragCoord * Scale;
    
    vec3 cell = floor(p);
    vec3 local = fract(p);
    
    // Hash function to get random cell ID
    // NGL Rule: explicitly cast Seed to vec3 to safely add to vector
    float rnd = fract(sin(dot(cell + vec3(41.0), vec3(7.63, 157.31, 113.97) + vec3(Seed))) * 43758.5453);
    
    // Randomly rotate the block to create the labyrinth
    if (rnd > 0.75) {
        // NGL Rule: explicitly cast float to vec3 for subtraction
        local = vec3(1.0) - local;
    } else if (rnd > 0.5) {
        local = local.yzx;
    } else if (rnd > 0.25) {
        local = local.zxy;
    }
    
    // Mutation vector for squarish tube shapes
    vec2 mut = vec2(ShapeMutation);
    
    // Evaluate the 3 torus tubes connecting the faces of the cubic cell
    vec2 q1 = vec2(length(local.xy) - 0.5, local.z - 0.5);
    float d1 = length(abs(q1) + mut);
    
    vec3 p2 = local.yzx - vec3(1.0, 1.0, 0.0);
    vec2 q2 = vec2(length(p2.xy) - 0.5, p2.z - 0.5);
    float d2 = length(abs(q2) + mut);
    
    vec3 p3 = local.zxy - vec3(0.0, 1.0, 0.0);
    vec2 q3 = vec2(length(p3.xy) - 0.5, p3.z - 0.5);
    float d3 = length(abs(q3) + mut);
    
    float minDist = min(d1, min(d2, d3));
    
    // Final distance to the tube surface
    Distance = minDist - Radius;
    
    // Identify which tube we are closest to for coloring
    float idx = 0.0;
    if (minDist == d1) idx = 1.0;
    else if (minDist == d2) idx = 2.0;
    else idx = 3.0;
    
    TubeIndex = idx;
    
    // Colorize tubes (red, green, blue) based on their internal index
    vec3 col1 = vec3(0.9, 0.4, 0.4);
    vec3 col2 = vec3(0.4, 0.9, 0.4);
    vec3 col3 = vec3(0.4, 0.4, 0.9);
    
    vec3 finalColor = vec3(1.0);
    if (idx == 1.0) finalColor = col1;
    else if (idx == 2.0) finalColor = col2;
    else finalColor = col3;
    
    BaseColor = vec4(finalColor, 1.0);
}
