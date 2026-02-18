
#enum Steps 1 2 3 4 5

float hash(vec3 p)
{	
	vec3 buf = fract(sin(p) * vec3(1223.321, 234.345, 215.321));
	return fract(buf.x*164.32+buf.y*143.22+buf.z*764.82);
}

void main(
	in vec3 FragCoord(knot = ioFragCoord, min = -1.0, max = 1.0),
	in vec3 Scale(value = 1, min = 0.0, max = 10.0),
	out float Result
)
{
		float result = 0.0;
		float summ = 0.0;
		vec3 iScale = Scale.xyz;
#if Steps == 1
			vec3 x = (FragCoord.xyz) * iScale+vec3(123,543,211);
			iScale *= 0.5;
			vec3 i = floor(x.xyz * 100.0);
			vec3 f = fract(x.xyz * 100.0);
			f = f * f * (3.0 - 2.0 * f);

			result += mix(mix(mix(hash(i + vec3(0, 0, 0)),
				hash(i + vec3(1, 0, 0)), f.x),
				mix(hash(i + vec3(0, 1, 0)),
					hash(i + vec3(1, 1, 0)), f.x), f.y),
				mix(mix(hash(i + vec3(0, 0, 1)),
					hash(i + vec3(1, 0, 1)), f.x),
					mix(hash(i + vec3(0, 1, 1)),
						hash(i + vec3(1, 1, 1)), f.x), f.y), f.z);
#else	
		for (float iStep = 1; iStep < Steps+0.5; iStep = iStep + 1.0) {
			float iStep2 = iStep * iStep;
			vec3 x = (FragCoord.xyz) * iScale+vec3(123,543,211);
			iScale *= 0.5;
			vec3 i = floor(x.xyz * 100.0);
			vec3 f = fract(x.xyz * 100.0);
			f = f * f * (3.0 - 2.0 * f);

			result += mix(mix(mix(hash(i + vec3(0, 0, 0)),
				hash(i + vec3(1, 0, 0)), f.x),
				mix(hash(i + vec3(0, 1, 0)),
					hash(i + vec3(1, 1, 0)), f.x), f.y),
				mix(mix(hash(i + vec3(0, 0, 1)),
					hash(i + vec3(1, 0, 1)), f.x),
					mix(hash(i + vec3(0, 1, 1)),
						hash(i + vec3(1, 1, 1)), f.x), f.y), f.z)* iStep2;
			summ += iStep2;
		}
		result /= summ;
#endif		
		Result = result;
}



