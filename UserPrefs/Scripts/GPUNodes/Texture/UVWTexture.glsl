out color result;
out float R;
out float G;
out float B;
out float A;

#enum OutputLODs 0 1 2 3

#ifdef OutputLODs_1
#define HAS_LOD0
#endif
#ifdef OutputLODs_2
#define HAS_LOD0
#define HAS_LOD1
#endif
#ifdef OutputLODs_3
#define HAS_LOD0
#define HAS_LOD1
#define HAS_LOD2
#endif

#ifdef HAS_LOD0
in float LOD0_Level(value=0, min=0, max=10);
out color LOD0;
out color LOD0_HighPass;
#endif

#ifdef HAS_LOD1
in float LOD1_Level(value=0, min=0, max=10);
out color LOD1;
out color LOD1_HighPass;
#endif

#ifdef HAS_LOD2
in float LOD2_Level(value=0, min=0, max=10);
out color LOD2;
out color LOD2_HighPass;
#endif
#enum Mapping triplanar UV cilindrical spherical
#enum CnlToColor None Red Green Blue
#ifndef CnlToColor_None
in color NewColor;
#endif

in vec3 UVW(knot= ioFragCoord);

in float TriplanarTransition(legacy=Sharp, value=1.0, min=1.0, max=10);
float Sharp = TriplanarTransition;
in float Scale = 5;
in float TexSharpen(value=1.0, min=0.0, max=5.0);



#sampler tex

vec2 xy=UVW.xy*Scale*0.01;
vec2 yz=UVW.yz*Scale*0.01;
vec2 zx=UVW.zx*Scale*0.01;

float wxy = ioNormal.z * ioNormal.z;
float wyz = ioNormal.x * ioNormal.x;
float wzx = ioNormal.y * ioNormal.y;
wxy = pow(wxy, Sharp);
wyz = pow(wyz, Sharp);
wzx = pow(wzx, Sharp);
float sw = wxy + wyz + wzx;
float swm = 1.0 / sw;
wxy *= swm;
wyz *= swm;
wzx *= swm;
sw = 1.0;

#define APPLY_MAPPING(aMAP, aLAMBDA) { vec4 RESULT = Mapping(aMAP, UVW, ioUV.xy, Scale, xy, yz, zx, wxy, wyz, wzx, sw); aLAMBDA; } 
#define APPLY_MAPPING_LOD(aMAP, aLOD, aLAMBDA) { vec4 RESULT = Mapping(aMAP, aLOD, UVW, ioUV.xy, Scale, xy, yz, zx, wxy, wyz, wzx, sw); aLAMBDA; }

#bool IsNormalMap
#if IsNormalMap
in float NormalIntensity(value=1.0, min=0.0, max=5.0);
vec4 BlendSamplesNormal(vec4 mxy, vec4 myz, vec4 mzx, float wxy, float wyz, float wzx, float sw) {
    vec3 nxy = mxy.xyz * 2.0 - 1.0; 
    vec3 nyz = myz.xyz * 2.0 - 1.0; 
    vec3 nzx = mzx.xyz * 2.0 - 1.0; 
    nxy.xy *= NormalIntensity;
    nyz.xy *= NormalIntensity;
    nzx.xy *= NormalIntensity;
    vec3 n = normalize(ioNormal.xyz);
    vec3 blendZ = vec3(n.x + nxy.x * sign(n.z), n.y + nxy.y, n.z);
    vec3 blendX = vec3(n.x, n.y + nyz.x * sign(n.x), n.z + nyz.y);
    vec3 blendY = vec3(n.x + nzx.y, n.y, n.z + nzx.x * sign(n.y));
    
    vec4 res;
    res.xyz = normalize(blendX * wyz + blendY * wzx + blendZ * wxy);
    res.a = (mxy.a * wxy + myz.a * wyz + mzx.a * wzx) / sw;
    return res;
}

vec3 ConvertNormalMapGeneric(vec4 texColor, vec2 texCoord) {
    vec3 tsNormal = texColor.xyz * 2.0 - 1.0;
    tsNormal.xy *= NormalIntensity;
    tsNormal = normalize(tsNormal);
    vec3 N = normalize(ioNormal.xyz);
    vec3 T = normalize(ioTangent.xyz - N * dot(ioTangent.xyz, N));
    vec3 B = normalize(ioBiTangent.xyz - (N * dot(ioBiTangent.xyz, N) + T * dot(ioBiTangent.xyz, T)));
    return normalize(N * tsNormal.z - T * tsNormal.x - B * tsNormal.y);
}
#else
vec4 BlendSamplesNormal(vec4 mxy, vec4 myz, vec4 mzx, float wxy, float wyz, float wzx, float sw) {
    vec4 res = (mxy*wxy + myz*wyz + mzx*wzx) / sw;
    return res;
}
#endif

vec4 triplanar(sampler2D aMAP, vec3 p_UVW, vec2 p_ioUV, float p_Scale, vec2 xy, vec2 yz, vec2 zx, float wxy, float wyz, float wzx, float sw) {
    vec4 mxy=textureBiased(aMAP,xy, -TexSharpen); vec4 myz=textureBiased(aMAP,yz, -TexSharpen); vec4 mzx=textureBiased(aMAP,zx, -TexSharpen);
    return BlendSamplesNormal(mxy, myz, mzx, wxy, wyz, wzx, sw);
}
vec4 triplanar(sampler2D aMAP, float aLOD, vec3 p_UVW, vec2 p_ioUV, float p_Scale, vec2 xy, vec2 yz, vec2 zx, float wxy, float wyz, float wzx, float sw) {
    vec4 mxy=textureLod(aMAP,xy,aLOD); vec4 myz=textureLod(aMAP,yz,aLOD); vec4 mzx=textureLod(aMAP,zx,aLOD);
    return BlendSamplesNormal(mxy, myz, mzx, wxy, wyz, wzx, sw);
}
vec4 UV(sampler2D aMAP, vec3 p_UVW, vec2 p_ioUV, float p_Scale, vec2 xy, vec2 yz, vec2 zx, float wxy, float wyz, float wzx, float sw) {
    vec4 col = textureBiased(aMAP, p_ioUV * p_Scale, -TexSharpen);
#if IsNormalMap
    col.xyz = ConvertNormalMapGeneric(col, p_ioUV * p_Scale);
#endif
    return col;
}
vec4 UV(sampler2D aMAP, float aLOD, vec3 p_UVW, vec2 p_ioUV, float p_Scale, vec2 xy, vec2 yz, vec2 zx, float wxy, float wyz, float wzx, float sw) {
    vec4 col = textureLod(aMAP, p_ioUV * p_Scale, aLOD);
#if IsNormalMap
    col.xyz = ConvertNormalMapGeneric(col, p_ioUV * p_Scale);
#endif
    return col;
}
vec4 cilindrical(sampler2D aMAP, vec3 p_UVW, vec2 p_ioUV, float p_Scale, vec2 xy, vec2 yz, vec2 zx, float wxy, float wyz, float wzx, float sw) {
    vec2 cyl = vec2(atan(p_UVW.x, p_UVW.z) / 6.2831853, p_UVW.y * 0.01) * p_Scale;
    vec4 col = textureBiased(aMAP, cyl, -TexSharpen);
#if IsNormalMap
    col.xyz = ConvertNormalMapGeneric(col, cyl);
#endif
    return col;
}
vec4 cilindrical(sampler2D aMAP, float aLOD, vec3 p_UVW, vec2 p_ioUV, float p_Scale, vec2 xy, vec2 yz, vec2 zx, float wxy, float wyz, float wzx, float sw) {
    vec2 cyl = vec2(atan(p_UVW.x, p_UVW.z) / 6.2831853, p_UVW.y * 0.01) * p_Scale;
    vec4 col = textureLod(aMAP, cyl, aLOD);
#if IsNormalMap
    col.xyz = ConvertNormalMapGeneric(col, cyl);
#endif
    return col;
}
vec4 spherical(sampler2D aMAP, vec3 p_UVW, vec2 p_ioUV, float p_Scale, vec2 xy, vec2 yz, vec2 zx, float wxy, float wyz, float wzx, float sw) {
    vec3 nUVW = normalize(p_UVW);
    vec2 sph = vec2(atan(nUVW.x, nUVW.z) / 6.2831853, asin(clamp(nUVW.y, -1.0, 1.0)) / 3.14159265) * p_Scale;
    vec4 col = textureBiased(aMAP, sph, -TexSharpen);
#if IsNormalMap
    col.xyz = ConvertNormalMapGeneric(col, sph);
#endif
    return col;
}
vec4 spherical(sampler2D aMAP, float aLOD, vec3 p_UVW, vec2 p_ioUV, float p_Scale, vec2 xy, vec2 yz, vec2 zx, float wxy, float wyz, float wzx, float sw) {
    vec3 nUVW = normalize(p_UVW);
    vec2 sph = vec2(atan(nUVW.x, nUVW.z) / 6.2831853, asin(clamp(nUVW.y, -1.0, 1.0)) / 3.14159265) * p_Scale;
    vec4 col = textureLod(aMAP, sph, aLOD);
#if IsNormalMap
    col.xyz = ConvertNormalMapGeneric(col, sph);
#endif
    return col;
}

#ifdef tex
	APPLY_MAPPING(tex, result = RESULT);

    float colorizer = 0;
    vec3 uncolored = vec3(0);
#ifdef CnlToColor_Red
    uncolored = vec3(min(result.r, max(result.g, result.b)), result.g, result.b);
    colorizer = result.r - uncolored.r;
#endif
#ifdef CnlToColor_Green
    uncolored = vec3(result.r, min(result.g, max(result.r, result.b)), result.b);
    colorizer = result.g - uncolored.g;
#endif
#ifdef CnlToColor_Blue
    uncolored = vec3(result.r, result.g, min(result.b, max(result.r, result.g)));
    colorizer = result.b - uncolored.b;
#endif
#ifndef CnlToColor_None
    result.xyz = uncolored + NewColor.xyz * colorizer;
#endif

    R = result.r;
    G = result.g;
    B = result.b;
    A = result.a;


    #ifdef HAS_LOD0
        APPLY_MAPPING_LOD(tex, LOD0_Level, LOD0 = RESULT;);
        LOD0_HighPass = result - LOD0 + vec4(0.5);
    #endif

    #ifdef HAS_LOD1
        APPLY_MAPPING_LOD(tex, LOD1_Level, LOD1 = RESULT;);
        LOD1_HighPass = result - LOD1 + vec4(0.5);
    #endif

    #ifdef HAS_LOD2
        APPLY_MAPPING_LOD(tex, LOD2_Level, LOD2 = RESULT;);
        LOD2_HighPass = result - LOD2 + vec4(0.5);
    #endif

#else 
	result = vec4(0, 0, 0, 0);
    R = 0;
    G = 0;
    B = 0;
    A = 0;
    #ifdef HAS_LOD0
        LOD0 = vec4(0, 0, 0, 0);
        LOD0_HighPass = vec4(0.5, 0.5, 0.5, 0.5);
    #endif
    #ifdef HAS_LOD1
        LOD1 = vec4(0, 0, 0, 0);
        LOD1_HighPass = vec4(0.5, 0.5, 0.5, 0.5);
    #endif
    #ifdef HAS_LOD2
        LOD2 = vec4(0, 0, 0, 0);
        LOD2_HighPass = vec4(0.5, 0.5, 0.5, 0.5);
    #endif
#endif
         
