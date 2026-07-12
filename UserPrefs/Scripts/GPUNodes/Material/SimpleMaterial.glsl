#enum ColorMode ReplaceColor ModulateColor 
#enum DepthMode Replace Modulate 
#enum GlossMode Replace Modulate 
#enum MetallMode Replace Modulate 
#enum Mapping triplanar UV cilindrical spherical 
#enum SecondColor None ReflectionColor SheenColor 
#enum ThirdColor None SubSurfaceColor MicroprotrusionsColor 
 
in Material BackGround; 
 
 
 
in color Color; 
in float Normal(default = 1, min = 0, max = 1); 
 
 
in float Depth(min = -2, max = 2, default = 0, expression = R=V*K); 
 
 
in float DepthOffset(min = -2, max = 2, default = 0, expression = R=V*K); 
in float Gloss(min = 0, max = 1, default = 0, expression = R=V*K); 
 
 
in float Metall(min = 0, max = 1, default = 0, expression = R=V*K); 
 
 
 
in float SoftDisplacement(min = 0, max = 1, default = 0); 
 
in float Anisotropy(min = -1, max = 1, default = 0); 
in float Sheen(min = 0, max = 1, default = 0); 
 
#ifdef SecondColor_ReflectionColor 
	in color ReflectionColor(min = 0, max = 1, default = 0.1); 
#endif 
#ifdef SecondColor_SheenColor 
	in color SheenColor(min = 0, max = 1, default = 1);	 
#endif 
 
#ifdef ThirdColor_SubSurfaceColor 
	in float Refraction(min = 0, max = 1, default = 0); 
	in color SubSurfaceColor(min = 0, max = 1, default = 0.0); 
	in float RefractionBlur(min = 0, max = 1, default = 0); 
	in float Chromatic(min = 0, max = 1, default = 0); 
#endif 
#ifdef ThirdColor_MicroprotrusionsColor 
	in float Micro(min = 0, max = 1, default = 0); 
	in color MicroColor(min = 0, max = 1, default = 1); 	 
	in float MicroGloss(min = 0, max = 1, default = 0); 
#else 
	in float ClearCoat(min = 0, max = 1, default = 0); 
	in float CoatGloss(min = 0, max = 1, default = 1); 
#endif 
in float SubSurface(min =-1, max = 1, default = 0); 
 
in float Mask(min = 0, max = 1, default = 1); 
in float Opacity(min = 0, max = 1, default = 1);
 
out Material result; 
 
// Functions for blending modes 
vec3 ReplaceColor(vec3 bg, vec3 fg) { return fg; } 
vec3 ModulateColor(vec3 bg, vec3 fg) { return bg * fg; } 
 
float Replace(float bg, float fg) { return fg; } 
float Modulate(float bg, float fg) { return bg * fg; } 
 
 
 
vec4 ColorM = vec4(1.0); 
float DepthM = 1.0; 
float GlossM = 1.0; 
float MetallM = 1.0; 
 
 
if(Color.INV) ColorM *= vec4(1.0)-(Color.K); 
else ColorM *= (Color.K); 
 
 
if(Depth.INV) DepthM *= 1.0-(Depth.K).x; 
else DepthM *= (Depth.K).x; 
	 
 
if(Gloss.INV) GlossM *= 1.0-(Gloss.K).x; 
else GlossM *= (Gloss.K).x; 
 
 
if(Metall.INV) MetallM *= 1.0-(Metall.K).x; 
else MetallM *= (Metall.K).x; 
 
 
result = _init_Material_; 
 
// 1. Get the final values taking curves (DC) into account 
vec4 finalColor = Color.DC(ColorM)*Color.V; 
float finalDepth = ((Depth.DC(vec4(DepthM))-vec4(0.5))*Depth.V).x; 
float finalGloss = (Gloss.DC(vec4(GlossM))*Gloss.V).x; 
float finalMetall = (Metall.DC(vec4(MetallM))*Metall.V).x; 
float finalMask = Mask; 
 
 
 
finalDepth += DepthOffset; 
 
// 2. If Background is connected, apply the selected blending modes (#enum) 
#ifdef IN_BackGround 
	vec3 bgColor = BackGround.ioAlbedoColor; 
	float bgDepth = BackGround.ioDisplacement; 
	float bgGloss = BackGround.ioGloss; 
	float bgMetall = BackGround.ioMetalness; 
    finalColor.xyz = ColorMode(bgColor, finalColor.xyz); 
    finalDepth = DepthMode(bgDepth, finalDepth); 
    finalGloss = GlossMode(bgGloss, finalGloss); 
    finalMetall = MetallMode(bgMetall, finalMetall); 
#endif 
 
// 3. Write the result 
result.ioAlbedoColor = finalColor; 
result.ioSoftDisplacement = finalDepth * SoftDisplacement + 0.5; 
result.ioDisplacement = finalDepth * (1.0 - SoftDisplacement); 
result.ioGloss = finalGloss; 
result.ioMetalness = finalMetall; 
result.ioAnisotropy = Anisotropy; 
 
#ifdef ThirdColor_MicroprotrusionsColor 
	result.ioMicroprotrusions = Micro; 
 
	result.ioMicroprotrusionsColor = MicroColor; 
	result.ioMicroprotrusionsGloss = MicroGloss; 
#endif 
#ifndef ThirdColor_MicroprotrusionsColor 
	result.ioClearCoat = ClearCoat; 
	result.ioClearCoatGloss = CoatGloss; 
#endif 
 
 
result.ioSheen = Sheen; 
#ifdef SecondColor_ReflectionColor 
result.ioReflectionColor = ReflectionColor; 
#endif 
#ifdef SecondColor_SheenColor 
result.ioSheenColor = SheenColor; 
#endif 
 
result.ioSubSurface = SubSurface; 
#ifdef ThirdColor_SubSurfaceColor 
result.ioSubSurfaceColor = SubSurfaceColor; 
result.ioRefraction = mix(-finalMetall, 1.0, Refraction); 
result.ioRefractionBlur = RefractionBlur; 
float oldChrom = result.ioRefractionChromatic; 
result.ioRefractionChromatic = mix(oldChrom, 1.0, Chromatic); 
#endif 
result.ioOpacity = Opacity;
 
#if OpacityFromAlbedoAlpha 
result.ioOpacity = Color.w; 
#endif 
 
#ifdef IN_Normal 
result[5].xyz = (Normal.V*( Normal.K-vec4(0.5))+vec4(0.5)).xyz; 
#endif 
 
#ifdef IN_BackGround 
    // The mask will be applied when blending the modified result with the original background 
    result = mixMTL(BackGround, result, clamp(finalMask, 0, 1)); 
#else	 
    //result.ioOpacity *= finalMask; 
#endif 
 
 
 
