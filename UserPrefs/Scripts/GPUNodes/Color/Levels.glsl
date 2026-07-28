// NGL Color Levels Node
in color Color(value=vec4(1.0, 1.0, 1.0, 1.0));
in float InBlack(value=0.0, min=0.0, max=1.0, AllowCurve=true);
in float InWhite(value=1.0, min=0.0, max=1.0, AllowCurve=true);
in float OutBlack(value=0.0, min=0.0, max=1.0, AllowCurve=true);
in float OutWhite(value=1.0, min=0.0, max=1.0, AllowCurve=true);
out color Result;

void main() {
    float inBk = InBlack;
    float inWt = max(inBk + 0.001, InWhite); // Avoid division by zero
    float outBk = OutBlack;
    float outWt = OutWhite;
    
    vec3 c = clamp(Color.rgb, 0.0, 1.0);
    
    // 1. Normalize between InBlack and InWhite
    c = max(vec3(0.0), c - vec3(inBk)) / vec3(inWt - inBk);
    c = clamp(c, 0.0, 1.0);
    
    // 2. Map to OutBlack and OutWhite
    c = c * vec3(outWt - outBk) + vec3(outBk);
    
    Result = vec4(c, Color.a);
}
