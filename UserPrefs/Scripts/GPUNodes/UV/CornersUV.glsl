in vec2 UVCoord;
in float Scale(value =1.0);
in vec2 Size(value = 1.0);

out vec2 CornersUV;
  
  	CornersUV = vec2(1.0) - abs(UVCoord-vec2(0.5, 0.5))*2.0; 
	CornersUV *= Scale*Size; 