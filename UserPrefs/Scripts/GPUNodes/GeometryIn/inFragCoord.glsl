
#enum genType float vec2 vec3 vec4

in genType Scale;  	
	
out vec4 fragCoord;

vec4 vScale = vec4(1);

#ifdef genType_float
	vScale = vec4(Scale);
#endif

#ifdef genType_vec2
	vScale = Scale.xyxy;
#endif

#ifdef genType_vec3
	vScale = Scale.xyzx;
#endif

#ifdef genType_vec4
	vScale = Scale;
#endif


fragCoord = ioFragCoord*vScale;   
