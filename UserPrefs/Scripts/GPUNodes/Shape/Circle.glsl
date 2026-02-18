in vec2 UVCoord;
in float Sharpness(min =1.0, max = 100.0);
in float Radius(min = 0.0, max = 1.0);

out float DistanceToCenter;
out float Mask;

		DistanceToCenter = distance(vec2(0.5), UVCoord);
		Mask = (DistanceToCenter-Radius)*Sharpness;