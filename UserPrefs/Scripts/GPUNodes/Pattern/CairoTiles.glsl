in vec2 fragCoord(knot = ioUV);//UV coordinates
in float Pattern;// shape of pattern 

out float DistanceToCenter;// distance to center
out vec4 ColorID;// color id
out float DistanceToBorder;//distance to border
out vec3 CellType;// cell type
out vec3 CellSide;// cell side
out vec2 CellIdx; // cell index
out vec2 CellUV;// cell UV coordinates

vec2 RAND(vec2 tileIndex, float fracRandomiser)//function for creation simple noise
{
  return fract(tan(dot(tileIndex+ vec2(1245,2566) ,tileIndex+vec2(7856,2156)+ fracRandomiser) / (tileIndex.y+4523)*(tileIndex+ vec2(2123, 5428))));// somthing random for noise 
}

    vec2 cellIdx = fract(fragCoord*10.0);
    vec2 cellUV = floor(fragCoord*10.0); 
    
    DistanceToCenter = 1.0;
  	DistanceToBorder = 1.0;
      
 
   	float reflectedCoord = mod(cellUV.x+cellUV.y,2.0);
    cellIdx.x = reflectedCoord-cellIdx.x*sign(reflectedCoord-.5);
    
	for(float relativeCellX=0.0; relativeCellX<=1.0; relativeCellX++)
	for(float relativeCellY=0.0; relativeCellY<=1.0; relativeCellY++)
    {
        vec2 relativeBlockIndex = vec2(relativeCellX, relativeCellY);
        
        float sideX = sign(relativeCellX-0.5); 
        float isDiagonal = float(relativeCellX == relativeCellY);
        vec2 sideDiagonal = vec2(sideX*isDiagonal,-sideX*(1.0-isDiagonal));
     
        vec2 sidePose = cellIdx - relativeBlockIndex + Pattern*sideDiagonal;
        relativeBlockIndex += sideDiagonal;
        
        float distanceTmp = dot(sidePose, sidePose);
        
        if( distanceTmp<DistanceToCenter ) 
        {
          	CellType = vec3(1.0, 0.0, 0.0);
          	CellSide = vec3(1.0, 0.0, 0.0);
            DistanceToBorder = DistanceToCenter;
            DistanceToCenter = distanceTmp;
            relativeBlockIndex.x = reflectedCoord-relativeBlockIndex.x*sign(reflectedCoord-0.5);
        	CellIdx = cellUV+relativeBlockIndex;

        }
        else if( distanceTmp<DistanceToBorder )
		{
          	CellSide.xy = vec2(0.0, 1.0); 
            DistanceToBorder = distanceTmp;
		}
     
    }
    
 
    float distanceTmp = dot(cellIdx-0.5,cellIdx-0.5);
    distanceTmp += 0.4; 
    if (distanceTmp < DistanceToCenter)
    {
      	CellType = vec3(0.0, 0.0, 1.0);
      	CellSide.z = 1.0;
        DistanceToBorder = DistanceToCenter;
        DistanceToCenter = distanceTmp;
        CellIdx = cellUV;
      
    }
    else if(distanceTmp < DistanceToBorder )
	{
      	CellSide.z = 0.0;
    	DistanceToBorder = distanceTmp;
	}
    DistanceToBorder = DistanceToBorder-DistanceToCenter;	 
  	ColorID = vec4(RAND(vec2(CellIdx), 1.0), RAND(vec2(CellIdx), 2.0));   
 	CellUV = (fragCoord*10.0)-CellIdx; 
   	
  
   
    
   