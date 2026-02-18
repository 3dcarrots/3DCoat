//#int BoughGathering 1
in vec3 fragCoord(knot = ioUV);
in float NoiseSize(value = 1.0);
in float Noise(value = 1.0);
in float CircleSizePower(value = 1.0, min = 1.0, max = 3.0);
in float CenterNoise(min = 0.0, max = 1.0);
in float Hairiness;
in float HairinessSize;   
in float  HairnessSelective(min = 0.0, max = 100.0 );
in float BranchCurvSize;
in float BranchCurv;

out float CircleID;   
out float DistanceToCoreCenter;
out float CirclesMask;
out float DistanceToCenter;
out float HairinessMask;
out vec2 NoisedPolarUV;
out vec3 PolarUVW;

//////////////////////////////////////////////////////////////

	vec3 hash(vec3 p) // replace this by something better
	{
		p = vec3(dot(p, vec3(17.1, 31.7, 74.7)),
			dot(p, vec3(29.5, 13.3, 26.1)),
			dot(p, vec3(13.5, 21.9, 14.6)));

		return -1.0 + 2.0 * fract(sin(p) * 458.5123);
	}

	float WoodNoise( vec3 Coord, float Scale, int Steps	)
	{
      
		float result = 0.0;

        float summ = 0.0;
        vec3 iScale = vec3(Scale);
        float fStep = 0;

        for (int iStep = 0; iStep < Steps; iStep++) {
            fStep++;
            float iStep2 = fStep * fStep;
              
          
            vec3 p = Coord.xyz * iScale;
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
      	return  result;
   }
///////////////////////////////////////////////////////////////

	float PolarCelinder (vec2 UV, float DistanceToZero)
    {
      
      float pr = 3.141592 * DistanceToZero * 2.0;   
      UV.x *= pr;      
     return length(UV+vec2(-pr*0.5, 0.0));    
      
      		
    }

	vec2 CirclesNoise = vec2(WoodNoise( fragCoord*NoiseSize * 0.05 *vec3(1.0, 0.1, 1.0), 1.0, 2), WoodNoise((vec3(333.0)+fragCoord)*NoiseSize*0.05*vec3(1.0, 0.1, 1.0), 1.0, 2))*Noise *0.1;
	vec2 BranchCurvNoise = vec2(WoodNoise( fragCoord*BranchCurvSize*0.001, 1.0, 1), WoodNoise((vec3(333.0)+fragCoord)* BranchCurvSize*0.001, 1.0, 1))*BranchCurv;
	CirclesNoise += BranchCurvNoise;
//////////////////////////////////////////////////////////////
	DistanceToCenter = length(fragCoord.zx);
	CirclesNoise = mix(CirclesNoise * DistanceToCenter, CirclesNoise,  CenterNoise); 
	NoisedPolarUV = vec2(atan(fragCoord.x + CirclesNoise.x, fragCoord.z + CirclesNoise.y), DistanceToCenter  ) * vec2(0.1591549/*0.1591549 = 1.0/(pi*2.0)*/, 1.0) + vec2(0.5, 0.0);   
	PolarUVW = vec3(atan(fragCoord.x + BranchCurvNoise.x, fragCoord.z + BranchCurvNoise.y), fragCoord.y, DistanceToCenter) * vec3(0.1591549/*0.1591549 = 1.0/(pi*2.0)*/, 1.0, 1.0) + vec3(0.5, 0.0, 0.0);     
		   

//////////////////////////////////////////////////////////////////////////
	
	float HairinessNoise =  WoodNoise((vec3(333.0)+fragCoord) * HairinessSize * 10.0 * vec3(1.0, 0.1, 1.0), 1.0, 3);

	HairinessMask = clamp(HairinessNoise*(1 + HairnessSelective), 0.0, 1.0); 

	//DistanceToCenter *= DistanceToCenter;   
	CirclesNoise += HairinessMask*Hairiness * 0.01;      	 
	vec2 WaveUV = fragCoord.zx + CirclesNoise;
	
    DistanceToCoreCenter = length(WaveUV);   
	float wave = pow(DistanceToCoreCenter * 10.0, CircleSizePower);
	
	CircleID = floor(wave);          	
	CirclesMask = wave - CircleID;     
	CircleID *= 0.01;
	DistanceToCoreCenter *= 0.1;
	DistanceToCenter *= 0.1;

                      