#define v2 vec2
#define v3 vec3
#define v4 vec4
#define f32 float

#enum Projection UV Top Left Front
#define UV ioUV.xyxy
#define Top ioFragCoord.xzxz
#define Left ioFragCoord.zyzy
#define Front ioFragCoord.xyxy

v2 Random01(v2 p) {
    f32 x = dot(p, v2(129.32,179.1));
    f32 y = dot(p, v2(102.22,99.1));
    v2 rand = v2(x,y);
    return fract(sin(rand)*156.432);
}

v3 Worley(v2 p) {
    f32 dist = 1.;
    v2 f_p = fract(p);
    v2 i_p = floor(p);

    for(int y = -1; y <= 1; ++y) {
        for(int x = -1; x <= 1; ++x) {
            v2 n = v2(float(x), float(y));
            v2 d = n + Random01(i_p+n) - f_p;
            if(length(d) < dist) dist = length(d);
        }
    }
    
    return v3(dist);
}

void mainImage( out vec4 fragColor, in vec2 fragCoord(knot = Projection) )
{
    // Normalized pixel coordinates (from 0 to 1)
    v2 uv = fragCoord/iResolution.xy;
    uv = uv * 2. - 1.;
    uv.x    *= iResolution.x / iResolution.y;
    
    f32 scale_factor = 5.;
    
    uv.y+=iTime*0.2;
    v3 col = Worley(uv *scale_factor);
    fragColor = v4(col, 1);
}