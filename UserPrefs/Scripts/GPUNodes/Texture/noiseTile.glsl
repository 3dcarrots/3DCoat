
out color fractTexture;
in vec2 uv;
in float depth;
float iDepth = length(ioFragCoord_DX)*1000.0*depth;

#sampler tex

vec2 iPixelSize = vec2(1,1);
    //Find the pixel level of detail
	float LOD = log(iDepth);
    //Round LOD down
	float LOD_floor = floor(LOD);
    //Compute the fract part for interpolating
	float LOD_fract = LOD - LOD_floor;
	
    //Compute scaled uvs
	vec2 uv1 = uv / exp(LOD_floor - 1.0);
	vec2 uv2 = uv / exp(LOD_floor + 0.0);
	vec2 uv3 = uv / exp(LOD_floor + 1.0);
	
#ifdef tex
    //Sample at 3 scales
	vec4 tex0 = texture(tex, uv1);
	vec4 tex1 = texture(tex, uv2);
	vec4 tex2 = texture(tex, uv3);
    
    //Blend samples together
	fractTexture = (tex1 + mix(tex0, tex2, LOD_fract)) * 0.5;
#else
	fractTexture = vec4(0, 0, 0, 0);
#endif    