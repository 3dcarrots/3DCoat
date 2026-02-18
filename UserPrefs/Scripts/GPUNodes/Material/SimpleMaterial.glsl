
in Material BackGround;

in vec3 UVW(knot = ioFragCoord);
in float Sharp;
in float Scale = 5;

in color Color;
#sampler ColorMap

in float Depth(min = -2, max = 2, default = 0, expression = R=V*K);
#sampler DepthMap
in float DepthOffset(min = -2, max = 2, default = 0, expression = R=V*K);

in float Gloss(min = 0, max = 1, default = 0, expression = R=V*K);
#sampler GlossMap

in float Metall(min = 0, max = 1, default = 0, expression = R=V*K);
#sampler MetallMap



in float Mask(min = 0, max = 1, default = 1);

out Material result;


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

#define TRI_PLANAR(aMAP, aLAMBDA) {vec4 mxy=texture(aMAP,xy); vec4 myz=texture(aMAP,yz); vec4 mzx=texture(aMAP,zx); mxy=(mxy*wxy+myz*wyz+mzx*wzx)/sw; vec4 RESULT = mxy; aLAMBDA;}

#ifdef ColorMap
		if(Color.INV){
			TRI_PLANAR(ColorMap, Color *= vec4(vec3(1.0, 1.0, 1.0)-RESULT.xyz, RESULT.w));
		} else {
			TRI_PLANAR(ColorMap, Color *= RESULT);
		}
#endif

#ifdef DepthMap
		if(Depth.INV){
			TRI_PLANAR(DepthMap, Depth *= 1.0-RESULT.x);
		} else {
			TRI_PLANAR(DepthMap, Depth *= RESULT.x);
		}
#endif
	Depth += DepthOffset-0.5;
	
#ifdef GlossMap
		if(Gloss.INV){
			TRI_PLANAR(GlossMap, Gloss *= 1.0-RESULT.x);
		} else {
			TRI_PLANAR(GlossMap, Gloss *= RESULT.x);
		}
#endif

#ifdef MetallMap
		if(Metall.INV){
			TRI_PLANAR(MetallMap, Metall *= 1.0-RESULT.x);
		} else {
			TRI_PLANAR(MetallMap, Metall *= RESULT.x);
		}
		TRI_PLANAR(MetallMap, Metall *= RESULT.z);
#endif


 result = _init_Material_;

 result.ioGloss =  Gloss.DC(vec4(Gloss)).x;
 result.ioMetalness =  Metall.DC(vec4(Metall)).x; 
 result.ioOpacity = Color.w;
 result.ioAlbedoColor = Color.DC(Color);
 result.ioDisplacement = Depth.DC(vec4(Depth)).x;
 result.ioDiffuseSSS = 0;

#ifdef IN_BackGround
	result = mixMTL(BackGround, result, clamp(Mask, 0, 1));
#endif