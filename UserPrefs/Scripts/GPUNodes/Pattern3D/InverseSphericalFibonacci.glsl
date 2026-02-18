	void main(
		in vec3 Dir(knot = ioNormal, min = -1.0, max = 1.0),
		in float Num(value = 64, min = -1.0, max = 1.0),
		out float Dist,
		out float IOut
	)
	{
		float PI = 3.14159265359;
		float PHI = 1.61803398875;

		float m = 1.0 - 1.0 / Num;

		float phi = min(atan(Dir.y, Dir.x), PI);
		float cosTheta = Dir.z;

		float k = max(2.0, floor(log(Num * PI * sqrt(5.0) * (1.0 - cosTheta * cosTheta)) / log(PHI + 1.0)));
		float Fk = pow(PHI, k) / sqrt(5.0);
		vec2  F = vec2(round(Fk), round(Fk * PHI)); // k, k+1

		vec2 ka = 2.0 * F / Num;
		vec2 kb = 2.0 * PI * (fract((F + 1.0) * PHI) - (PHI - 1.0));

		mat2 iB = mat2(ka.y, -ka.x,
			kb.y, -kb.x) / (ka.y * kb.x - ka.x * kb.y);

		vec2 c = floor(iB * vec2(phi, cosTheta - m));
		float d = 8.0;
		float j = 0.0;
		for (int s = 0; s < 4; s++)
		{
			vec2 uv = vec2(float(s - 2 * (s / 2)), float(s / 2));

			float i = dot(F, uv + c); 

			float phi = 2.0 * PI * fract(i * PHI);
			float cosTheta = m - 2.0 * i / Num;
			float sinTheta = sqrt(1.0 - cosTheta * cosTheta);

			vec3 q = vec3(cos(phi) * sinTheta, sin(phi) * sinTheta, cosTheta);
			float squaredDistance = dot(q - Dir, q - Dir);
			if (squaredDistance < d)
			{
				d = squaredDistance;
				j = i;
			}
		}
		Dist = j;
		IOut = d;
	}


