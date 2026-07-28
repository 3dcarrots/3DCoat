// Cobwebs in 1 tweet pattern adaptation
// Original Shadertoy by twitter.com/zozuar

void main(
    in vec3 FragCoord(value= 1, knot= ioFragCoord, expression= R=(V*K), min= -10.0, max= 10.0),
    in float Scale(value= 1.0, min= 0.01, max= 100.0, expression= R=(V*K)),
    in vec3 Offset(value= vec3(0.0, expression= R=(V*K))),
    in float Phase(value= 0.0, min= -100.0, max= 100.0, expression= R=(V*K)),
    in float Twist(value= 0.1, min= -2.0, max= 2.0, expression= R=(V*K)),
    in float Thickness(value= 0.1, min= 0.0, max= 1.0, expression= R=(V*K)),
    out float Distance,
    out float Value,
    out vec4 BaseColor
)
{
    vec3 p = FragCoord * Scale + Offset;
    p.z -= Phase; // Similar to iTime in the original
    
    float a = p.z * Twist;
    float c = cos(a);
    float s = sin(a);
    mat2 rot = mat2(c, s, -s, c);
    
    vec3 o = p;
    // Rotate xy plane based on z coordinate
    o.xy = rot * o.xy;
    
    // Core pattern formula
    float val = length(cos(o.xy) + sin(o.yz));
    
    // Distance field: < 0 inside the web, > 0 outside
    Distance = 1.0-(Thickness - val)*2.0;
    Value = val;
    
    // Normalized color formula based on the original tweet
    vec3 col = (sin(o) + vec3(2.0, 5.0, 9.0)) * 0.1;
    BaseColor = vec4(col, 1.0);
}
