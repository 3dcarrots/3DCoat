#bool AllowRotating 
in vec3 fragCoord;
in vec3 Scale;
in vec3 Rotate(value = 0.0, min = 0.0, max = 360.0);
in vec3 Shift;

out vec3 Axis;
out vec2 UVCoord;
out vec3 UVW;
#if AllowRotating 

float GradToRad = 0.01745329;//
mat3 rotationX( in float angle ) {
	return mat3(1.0, 0.0, 0.0, 
                0.0, cos(angle), -sin(angle), 
				0.0, sin(angle), cos(angle));
}

mat3 rotationY( in float angle ) {
	return mat3(cos(angle),	0.0, sin(angle),
                0.0, 1.0, 0.0,
                -sin(angle), 0.0, cos(angle));
}

mat3 rotationZ( in float angle ) {
	return mat3(cos(angle),	-sin(angle), 0.0,	
			 	sin(angle),	cos(angle), 0.0,
				0.0, 0.0, 1.0	);
}

		UVW = (rotationY(Rotate.y * GradToRad) * rotationX(Rotate.x * GradToRad)* rotationZ(Rotate.z * GradToRad)* fragCoord) * Scale + Shift; 
		vec3 Normal = (rotationY(Rotate.y * GradToRad) * rotationX(Rotate.x * GradToRad)* rotationZ(Rotate.z * GradToRad)* ioNormal.xyz);
#else 
		UVW = fragCoord;
		vec3 Normal = ioNormal.xyz;

#endif		
		Axis = vec3(0.0, 0.0, 1.0);  
	 		if (abs(Normal.x) > abs(Normal.y)&& abs(Normal.x) > abs(Normal.z) ) Axis = vec3(1.0, 0.0, 0.0);     
 			if ( abs(Normal.y) > abs(Normal.x)&&abs(Normal.y) > abs(Normal.z)) Axis = vec3(0.0, 1.0, 0.0);  
 
		UVCoord = UVW.xy*Axis.z + UVW.xz*Axis.y+ UVW.yz*Axis.x;
		
  
	
  
   