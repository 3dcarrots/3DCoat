in vec3 source;

in vec3 angles;

out vec3 result;

#bool invertX
#bool invertY
#bool invertZ

vec2 rotate(vec2 v, float a) {
	float s = sin(a);
	float c = cos(a);
	mat2 m = mat2(c, s, -s, c);
	return m * v;
}

#if invertX
source.x = -spurce.x;
#endif

#if invertY
source.y = -spurce.y;
#endif

#if invertZ
source.z = -spurce.z;
#endif

source.xy = rotate(source.xy, angles.z);
source.yz = rotate(source.yz, angles.x);
source.xz = rotate(source.xz, angles.y);

result = source;  