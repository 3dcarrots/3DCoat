out color result;
out float R;
out float G;
out float B;
out float A;

#bool OutputLOD0
#if OutputLOD0
in float LOD0_Level(value=0, min=0, max=10);
out color LOD0;
out color LOD0_HighPass;
#endif

#bool OutputLOD1
#if OutputLOD1
in float LOD1_Level(value=0, min=0, max=10);
out color LOD1;
out color LOD1_HighPass;
#endif

#bool OutputLOD2
#if OutputLOD2
in float LOD2_Level(value=0, min=0, max=10);
out color LOD2;
out color LOD2_HighPass;
#endif

in vec3 UVW(knot= ioFragCoord);

in float TriplanarTransition(legacy=Sharp, value=1.0, min=1.0, max=10);
float Sharp = TriplanarTransition;
in float Scale = 5;
in float TexSharpen(value=1.0, min=0.0, max=5.0);



#sampler tex
#bool EnableHighPass
#if EnableHighPass
in float HighPassLod(value=0, min=0, max=10);
#endif

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

#bool IsNormalMap

#if IsNormalMap
#bool InvertNormalX
#bool InvertNormalY
in float NormalIntensity(value=1.0, min=0.0, max=5.0);
vec4 BlendSamplesNormal(vec4 mxy, vec4 myz, vec4 mzx, float wxy, float wyz, float wzx, float sw) {
    vec3 nxy = mxy.xyz * 2.0 - 1.0; 
    vec3 nyz = myz.xyz * 2.0 - 1.0; 
    vec3 nzx = mzx.xyz * 2.0 - 1.0; 
#if InvertNormalX
    nxy.x = -nxy.x;
    nyz.x = -nyz.x;
    nzx.x = -nzx.x;
#endif
#if InvertNormalY
    nxy.y = -nxy.y;
    nyz.y = -nyz.y;
    nzx.y = -nzx.y;
#endif
    nxy.xy *= NormalIntensity;
    nyz.xy *= NormalIntensity;
    nzx.xy *= NormalIntensity;
    vec3 n = normalize(ioNormal.xyz);
    vec3 blendZ = vec3(n.x + nxy.x * sign(n.z), n.y + nxy.y, n.z);
    vec3 blendX = vec3(n.x, n.y + nyz.x * sign(n.x), n.z + nyz.y);
    vec3 blendY = vec3(n.x + nzx.y, n.y, n.z + nzx.x * sign(n.y));
    
    vec4 res;
    res.xyz = normalize(blendX * wyz + blendY * wzx + blendZ * wxy) * 0.5 + 0.5;
    res.a = (mxy.a * wxy + myz.a * wyz + mzx.a * wzx) / sw;
    return res;
}
#define BLEND_SAMPLES(mxy, myz, mzx, wxy, wyz, wzx, sw) mxy = BlendSamplesNormal(mxy, myz, mzx, wxy, wyz, wzx, sw);
#else
#define BLEND_SAMPLES(mxy, myz, mzx, wxy, wyz, wzx, sw) mxy = (mxy*wxy + myz*wyz + mzx*wzx) / sw;
#endif

#define TRI_PLANAR(aMAP, aLAMBDA) {vec4 mxy=textureBiased(aMAP,xy, -TexSharpen); vec4 myz=textureBiased(aMAP,yz, -TexSharpen); vec4 mzx=textureBiased(aMAP,zx, -TexSharpen); BLEND_SAMPLES(mxy, myz, mzx, wxy, wyz, wzx, sw) vec4 RESULT = mxy; aLAMBDA;}
#define TRI_PLANAR_LOD(aMAP, aLOD, aLAMBDA) {vec4 mxy=textureLod(aMAP,xy,aLOD); vec4 myz=textureLod(aMAP,yz,aLOD); vec4 mzx=textureLod(aMAP,zx,aLOD); BLEND_SAMPLES(mxy, myz, mzx, wxy, wyz, wzx, sw) vec4 RESULT = mxy; aLAMBDA;}

#ifdef tex
#if EnableHighPass
    vec4 thp0;
    vec4 thp1;
    TRI_PLANAR(tex, thp0 = RESULT);
    TRI_PLANAR_LOD(tex, HighPassLod, thp1 = RESULT);
    result = thp0 - thp1 + vec4(0.5);
#else
	TRI_PLANAR(tex, result = RESULT);
#endif
    R = result.r;
    G = result.g;
    B = result.b;
    A = result.a;


    #if OutputLOD0
        TRI_PLANAR_LOD(tex, LOD0_Level, LOD0 = RESULT;);
        LOD0_HighPass = result - LOD0 + vec4(0.5);
    #endif

    #if OutputLOD1
        TRI_PLANAR_LOD(tex, LOD1_Level, LOD1 = RESULT;);
        LOD1_HighPass = result - LOD1 + vec4(0.5);
    #endif

    #if OutputLOD2
        TRI_PLANAR_LOD(tex, LOD2_Level, LOD2 = RESULT;);
        LOD2_HighPass = result - LOD2 + vec4(0.5);
    #endif

#else 
	result = vec4(0, 0, 0, 0);
    R = 0;
    G = 0;
    B = 0;
    A = 0;
    #if OutputLOD0
        LOD0 = vec4(0, 0, 0, 0);
        LOD0_HighPass = vec4(0.5, 0.5, 0.5, 0.5);
    #endif
    #if OutputLOD1
        LOD1 = vec4(0, 0, 0, 0);
        LOD1_HighPass = vec4(0.5, 0.5, 0.5, 0.5);
    #endif
    #if OutputLOD2
        LOD2 = vec4(0, 0, 0, 0);
        LOD2_HighPass = vec4(0.5, 0.5, 0.5, 0.5);
    #endif
#endif
         
