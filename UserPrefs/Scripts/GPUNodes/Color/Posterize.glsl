// NGL Color Posterize Node
in color Color(value=vec4(1.0, 1.0, 1.0, 1.0));
in float Levels(value=4.0, min=2.0, max=256.0, AllowCurve=true);
out color Result;

void main() {
    float levelsVal = max(2.0, floor(Levels));
    
    vec3 c = clamp(Color.rgb, 0.0, 1.0);
    
    // Map 0-1 to 0-(levels-1), floor it, then map back to 0-1
    float factor = levelsVal - 1.0;
    c = floor(c * factor + vec3(0.5)) / vec3(factor);
    
    Result = vec4(c, Color.a);
}
