#int NUM_CELLS	16	
#int TileSizeX 1
#int TileSizeY 1
#define TILES vec2(TileSizeY, TileSizeX) 

in float ScaleX;
in vec2 fragCoord(knot = ioUV);
 
out vec2 PolarUV;
out vec2 LocalUV;
out vec2 FacePos;
out vec2 PointShift;
out vec4 DistanceToPoint;


float Cells(in vec2 p, in float numCells)
{
  	float TileSize = max(TileSizeY,TileSizeX);
	p *= numCells * TileSize;
	float d = 1.0e10;
	for (int xo = -1; xo <= 1; xo++)
	{
		for (int yo = -1; yo <= 1; yo++)
		{
          	 
			vec2 tp = floor(p) + vec2(xo, yo);
            vec2 HashTp = mod(tp, numCells / TILES * TileSize);
            float Hash = 523.0*sin(dot(HashTp, vec2(53.3158, 43.6143)));
          	vec2 Hash2 = vec2(fract(15.32354 * Hash), fract(17.25865 * Hash));
          	      
          
			tp = p - tp - Hash2;
          	vec2 tpScaleX = tp;
          	tpScaleX.x *= ScaleX;
          	float newDist = length(tpScaleX);     
			
            if (newDist < d)
            {
             	d =  newDist;
              	PointShift = Hash2; 
              	FacePos = - tp + p; 
              	LocalUV = tp;
              	PolarUV = vec2(atan(tp.x, tp.y), d) * vec2(0.1591549/*0.1591549 = 1.0/(pi*2.0)*/, 1.0) + vec2(0.5, 0.0);
            }	
		}
	}
	return sqrt(d);

}

	
	vec2 uv = fract(fragCoord.xy/ max(TileSizeY,TileSizeX));
	float c = Cells(uv, NUM_CELLS);
	vec3 col = vec3(c*.83, c, min(c*1.3, 1.0));
	DistanceToPoint = vec4(col, 1.0);

 