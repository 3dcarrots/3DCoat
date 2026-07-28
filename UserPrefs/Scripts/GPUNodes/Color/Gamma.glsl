// NGL Color Gamma Node
in color Color(value=vec4(1.0, 1.0, 1.0, 1.0));
in float Gamma(value=1.0, min=0.1, max=5.0, AllowCurve=true);
out color Result;

void main() {
    float gammaVal = max(0.001, Gamma);
    vec3 c = pow(clamp(Color.rgb, 0.0, 1.0), vec3(1.0 / gammaVal));
    Result = vec4(c, Color.a);
}
