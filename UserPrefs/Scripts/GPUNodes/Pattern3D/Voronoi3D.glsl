	vec3 hash(vec3 p) // replace this by something better
	{
		p = vec3(dot(p, vec3(171, 317, 747)),
			dot(p, vec3(295, 133, 261)),
			dot(p, vec3(135, 219, 146)));

		return fract(sin(p) * 45458.51423);
	}

	void main(
		in vec3 FragCoord(value= 1, knot= ioFragCoord, expression= R=(V*K), min= -10.0, max= 10.0),
      	in float Scale,
		out float Closest,
		out float SecondClosest,
		out float CellID
	)
	{

		vec3 p = floor(FragCoord*Scale);
		vec3 f = fract(FragCoord*Scale);
		float id = 0.0;
		vec2 res = vec2(100.0);
		for (int k = -1; k <= 1; k++)
			for (int j = -1; j <= 1; j++)
				for (int i = -1; i <= 1; i++)
				{
					vec3 b = vec3(float(i), float(j), float(k));
					vec3 r = vec3(b) - f + hash(p + b);
					float d = dot(r, r);

					if (d < res.x)
					{
						id = dot(p + b, vec3(1.0, 57.0, 113.0));
						res = vec2(d, res.x);
					}
					else if (d < res.y)
					{
						res.y = d;
					}
				}

		Closest = res.x;
		SecondClosest = res.y;
		CellID = abs(id);
	}
	










