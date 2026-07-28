// NGL Color Balance Node
in color Color(value=vec4(1.0, 1.0, 1.0, 1.0));
in color Balance(value=vec4(1.0, 1.0, 1.0, 1.0));
in float MixAmount(value=1.0, min=0.0, max=1.0, AllowCurve=true);
out color Result;

void main() {
    vec3 bal = Balance.rgb;
    float mixVal = clamp(MixAmount, 0.0, 1.0);
    
    vec3 balancedCol = Color.rgb * bal;
    vec3 finalColor = mix(Color.rgb, balancedCol, mixVal);
    
    Result = vec4(clamp(finalColor, 0.0, 1.0), Color.a);
}
