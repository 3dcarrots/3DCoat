
out color result;

in vec3 UVW(knot= ioFragCoord);

in float Sharp;
in float Scale = 5;
#sampler tex

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

#ifdef tex
	vec4 mxy=texture(tex,xy);
	vec4 myz=texture(tex,yz);
	vec4 mzx=texture(tex,zx);
	mxy=(mxy*wxy+myz*wyz+mzx*wzx)/sw;
	result = mxy;
#else 
	result = vec4(0, 0, 0, 0);
#endif
         