	vec3 hash(vec3 p) // replace this by something better 
	{ 
		p = vec3(dot(p, vec3(17.1, 31.7, 74.7)), 
			dot(p, vec3(29.5, 13.3, 26.1)), 
			dot(p, vec3(13.5, 21.9, 14.6))); 
 
		return -1.0 + 2.0 * fract(sin(p) * 458.5123); 
	} 
 
	#int Steps 1 0 10 
    #define Grayscale 0
    #define RG 1
    #define RGB 2
    #define RGBA 3
	#enum ChannelCount Grayscale RG RGB RGBA 
	#bool UseStepsCurve 
 
    #if UseStepsCurve 
		in One2DCurve StepsCurve; 
    #endif 
 
	void main( 
		in vec3 Coord(value= (1,1,1,1), knot= ioFragCoord, expression= R=V*K, min= -10.0, max= 10.0),  
		in float Scale(value= 1, min= -10.0, max= 10.0), 
		out vec4 Result(color = (1,0,0,1)) 
		) 
	{ 
       
	#if ChannelCount > 0 
	vec4 result4 = vec4(0.0); 
      float fCNL = 0; 
    for(int iCNL = 0; iCNL <= ChannelCount; iCNL++){ 
        vec3 uvShift = vec3(fCNL*0.125, fCNL*0.364, fCNL*0.287); 
		fCNL++; 
   	#endif 
		float result = 0.0; 
 
        float summ = 0.0; 
        vec3 iScale = vec3(Scale); 
        float fStep = 0; 
 
 
 
        for (int iStep = 0; iStep < Steps; iStep++) { 
            fStep++; 
            float iStep2 = fStep * fStep; 
            #if UseStepsCurve 
				iStep2 *= StepsCurve[iStep*255/Steps]; 
          	#endif 
           
           
            vec3 p = Coord.xyz * iScale*0.1; 
			#if ChannelCount > 0 
            p+= uvShift; 
            #endif 
            iScale *= 0.5; 
            vec3 i = floor(p.xyz * 100.0); 
            vec3 f = fract(p.xyz * 100.0); 
 
            vec3 u = f * f * (3.0 - 2.0 * f); 
 
            result += mix(mix(mix(dot(hash(i + vec3(0.0, 0.0, 0.0)), f - vec3(0.0, 0.0, 0.0)), 
                dot(hash(i + vec3(1.0, 0.0, 0.0)), f - vec3(1.0, 0.0, 0.0)), u.x), 
                mix(dot(hash(i + vec3(0.0, 1.0, 0.0)), f - vec3(0.0, 1.0, 0.0)), 
                    dot(hash(i + vec3(1.0, 1.0, 0.0)), f - vec3(1.0, 1.0, 0.0)), u.x), u.y), 
                mix(mix(dot(hash(i + vec3(0.0, 0.0, 1.0)), f - vec3(0.0, 0.0, 1.0)), 
                    dot(hash(i + vec3(1.0, 0.0, 1.0)), f - vec3(1.0, 0.0, 1.0)), u.x), 
                    mix(dot(hash(i + vec3(0.0, 1.0, 1.0)), f - vec3(0.0, 1.0, 1.0)), 
                        dot(hash(i + vec3(1.0, 1.0, 1.0)), f - vec3(1.0, 1.0, 1.0)), u.x), u.y), u.z)* iStep2; 
            summ += iStep2; 
        } 
		result /= summ; 
    #if ChannelCount > 0 
    	result4[iCNL] = result*0.5+0.5; 
    } 
	Result = result4;       
    #else 
	Result = vec4(result*0.5+0.5); 
    #endif 
} 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
