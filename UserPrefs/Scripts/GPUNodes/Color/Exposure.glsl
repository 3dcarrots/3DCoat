// NGL Color Exposure Node
in color Color(value=vec4(1.0, 1.0, 1.0, 1.0));
in float Exposure(value=0.0, min=-5.0, max=5.0, AllowCurve=true);
out color Result;

void main() {
    float expVal = Exposure;
    
    // Exposure = Color * 2^Exposure
    vec3 c = Color.rgb * exp2(expVal);
    
    Result = vec4(clamp(c, 0.0, 1.0), Color.a);
}
