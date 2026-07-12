// NGL Color Desaturate Node
in color Color(value=vec4(1.0, 1.0, 1.0, 1.0));
in float Amount(value=1.0, min=0.0, max=1.0, AllowCurve=true);
out color Result;

void main() {
    float luma = dot(Color.rgb, vec3(0.299, 0.587, 0.114));
    vec3 grayscale = vec3(luma);
    
    float mixAmount = clamp(Amount, 0.0, 1.0);
    vec3 finalColor = mix(Color.rgb, grayscale, mixAmount);
    
    Result = vec4(finalColor, Color.a);
}
