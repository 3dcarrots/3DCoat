// NGL Color Brightness/Contrast Node
in color Color(value=vec4(1.0, 1.0, 1.0, 1.0));
in float Brightness(value=0.0, min=-1.0, max=1.0, AllowCurve=true);
in float Contrast(value=1.0, min=0.0, max=5.0, AllowCurve=true);
out color Result;

void main() {
    float brightnessVal = Brightness;
    float contrastVal = Contrast;
    
    vec3 c = Color.rgb + vec3(brightnessVal);
    c = (c - vec3(0.5)) * vec3(contrastVal) + vec3(0.5);
    
    Result = vec4(clamp(c, 0.0, 1.0), Color.a);
}
