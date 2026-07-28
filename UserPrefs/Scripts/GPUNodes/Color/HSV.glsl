// NGL Color HSV Node
in color Color(value=vec4(1.0, 1.0, 1.0, 1.0));
in float Hue(value=0.0, min=-1.0, max=1.0, AllowCurve=true);
in float Saturation(value=1.0, min=0.0, max=5.0, AllowCurve=true);
in float Value(value=1.0, min=0.0, max=5.0, AllowCurve=true);
out color Result;

vec3 rgb2hsv(vec3 c) {
    vec4 K = vec4(0.0, -1.0 / 3.0, 2.0 / 3.0, -1.0);
    vec4 p = mix(vec4(c.bg, K.wz), vec4(c.gb, K.xy), step(c.b, c.g));
    vec4 q = mix(vec4(p.xyw, c.r), vec4(c.r, p.yzx), step(p.x, c.r));

    float d = q.x - min(q.w, q.y);
    float e = 1.0e-10;
    return vec3(abs(q.z + (q.w - q.y) / (6.0 * d + e)), d / (q.x + e), q.x);
}

vec3 hsv2rgb(vec3 c) {
    vec4 K = vec4(1.0, 2.0 / 3.0, 1.0 / 3.0, 3.0);
    vec3 p = abs(fract(c.xxx + K.xyz) * 6.0 - K.www);
    return c.z * mix(K.xxx, clamp(p - K.xxx, 0.0, 1.0), c.y);
}

void main() {
    float hueShift = Hue;
    float satMult = Saturation;
    float valMult = Value;
    
    vec3 hsv = rgb2hsv(clamp(Color.rgb, 0.0, 1.0));
    
    hsv.x = fract(hsv.x + hueShift);
    hsv.y = clamp(hsv.y * satMult, 0.0, 1.0);
    hsv.z = clamp(hsv.z * valMult, 0.0, 1.0);
    
    vec3 finalColor = hsv2rgb(hsv);
    Result = vec4(finalColor, Color.a);
}
