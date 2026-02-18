//https://www.shadertoy.com/view/ldl3W8
//https://www.shadertoy.com/view/Xd23Dh
in vec2 fragCoord(knot = ioUV);// input coordinates
in float Noise(min=0.0, max=1.0);// stage of cell deformation
in float Blur(value=0, min=0.0, max=1.0);// blur of cells


out float DistanceToPoint;// distance from current pixel to point
out color ColorID;//color index
out float RelativeCenter;// deformed distance to the point
out float SharpCenter;// relative distance to closest border
out float DistanceToBorder;// distance to closest border
out vec2 CellLocalUV;// local UV coordinates relative to the point

//noise generator
vec3 hash( vec2 p )
{
    vec3 q = vec3( dot(p,vec2(127.1,311.7)), 
				   dot(p,vec2(269.5,183.3)), 
				   dot(p,vec2(419.2,371.9)) );
	 return fract(sin(q)*43758.5453);
}

    vec2 CellIdx = floor(fragCoord*10.0);// cell index
    vec2 CellUV = fract(fragCoord*10.0);// cell local UV coordinates
    
	// select face by point 
	/////////////////////////////////////////////////////////////////////////////////////
	vec2 cellLocalUV;
	vec2 flatIndex = vec2(0.0, 0.0);//initialising variables for  face indexes 
    float distanceToPoint = 8.0;
    for( int y=-1; y<=1; y++ )
    for( int x=-1; x<=1; x++ )
    {
        vec2 relativeIndex = vec2(float(x),float(y));
		vec2 shapeNoise = hash( CellIdx + relativeIndex ).xy*Noise;
		vec2 localUV = relativeIndex + shapeNoise - CellUV; 
        float distToPoint = dot(localUV,localUV);
		
        if( distToPoint<distanceToPoint )
        {
            distanceToPoint = distToPoint;
            cellLocalUV = localUV;
            flatIndex = (CellIdx + relativeIndex);
      
        }
    }

    ////////////////////////////////////////////////////////////////////////////////
	// extract cell info for each pixel
	///////////////////////////////////////////////////////////////////////////////
	float WeightSumm = 0.0;//summ for users blur 
	float MaxBlurWeightSumm = 0.0;// summ for maximal blir of faces
	DistanceToPoint = 100;//distance to point 
	ColorID = color(0.0);// initialising of color like 0.0 for summ of weights
	vec2 MaxBluredIndex = vec2(0.0, 0.0);//initialising variables for blured face indexes 
	
    float distanceToBorder = 8.0;
	for( int y=-2; y<=2; y++ ) 
    for( int x=-2; x<=2; x++ )
    {
        vec2  relativeIndex = vec2( x, y );// index of point relative to cellIdx
		vec3  shapeNoise = hash( CellIdx + relativeIndex )*vec3(Noise, Noise, 1.0);// noise for face shape
      	vec3  colorID = hash( CellIdx + relativeIndex + vec2(123, 321) );// color index
		vec2  vertexPos = relativeIndex- CellUV + shapeNoise.xy;//current vertexes(center) position  of shape
		float weight = pow( 1.0-smoothstep(0.0,1.414,length(vertexPos)), pow(1.0-Blur,5.0)*50.0+1.0 );//weight of influence current cell to current pixel
      	float MaxBlurWeight =  1.0-smoothstep(0.0,1.414,length(vertexPos));
      	MaxBlurWeight *= MaxBlurWeight; 
      	WeightSumm += weight;
      	MaxBluredIndex += (CellIdx + relativeIndex)* MaxBlurWeight;
      	MaxBlurWeightSumm += MaxBlurWeight; 
    	DistanceToPoint = min(DistanceToPoint,length(vertexPos));
      	ColorID += color(colorID, shapeNoise.z)*weight; 
        
       	vec2 localUV = relativeIndex + shapeNoise.xy - CellUV;// temporary  

        if( dot(cellLocalUV-localUV, cellLocalUV-localUV) > 0.00001 ) 
        	distanceToBorder = min( distanceToBorder, dot( 0.5*(cellLocalUV+localUV), normalize(localUV-cellLocalUV) ) );
    }
	ColorID /= WeightSumm ;
  	MaxBluredIndex /= MaxBlurWeightSumm; 
	RelativeCenter = distance(MaxBluredIndex,flatIndex);
  	SharpCenter = max(abs(flatIndex.x-MaxBluredIndex.x),abs(flatIndex.y-MaxBluredIndex.y));
	DistanceToBorder = distanceToBorder;
	CellLocalUV = cellLocalUV*0.5;
     