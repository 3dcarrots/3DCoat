out float BoxDisplacement;
out vec4 BoxSides;
out float BoxUpperSide;
out float BoxLeftSide;
out float BoxRightSide;
out float DistanceToCenter;
out float DistanceToBorder;
out vec2 HexagonIndex;
out vec4 ColorID;


vec2 RAND(vec2 tileIndex, float fracRandomiser)//function for creation simple noise
{
  return fract(tan(dot(tileIndex+ vec2(1245,2566) ,tileIndex+vec2(7856,2156)+ fracRandomiser) / (tileIndex.y+4523)*(tileIndex+ vec2(2123, 5428))));// somthing random for noise 
}



void mainImage( in vec2 fragCoord  ) 
{
	vec2 skewedUV = vec2( fragCoord.x*1.1547005384/* 2/sqrt(3) */, fragCoord.y + fragCoord.x*0.5773502692/* 1/sqrt(3) */ );
	
	vec2 rhombusIndex = floor(skewedUV);
	vec2 rhombusUV = skewedUV-rhombusIndex;
  
  
	// diagonal grouping of rhombuses by 3
	float diagonals3 = mod(rhombusIndex.x + rhombusIndex.y, 3.0);

	float boxFrontSides = step(1.0,diagonals3);
	float diagonalTriangles = step(2.0,diagonals3);
	vec2  Triangulation  = step(rhombusUV.xy,rhombusUV.yx);
	
    float distanceToBorder = dot(Triangulation, 1.0-rhombusUV.yx + boxFrontSides*(rhombusUV.x+rhombusUV.y-1.0) + diagonalTriangles*(rhombusUV.yx-2.0*rhombusUV.xy));

		
	vec2 globalShiftedUV = vec2( skewedUV.x + floor(0.5+fragCoord.y/1.5), 4.0*fragCoord.y/3.0 )*0.5 + 0.5;
  	vec2 rawFaceUV = fract(globalShiftedUV); 
	float distanceToCenter = length(rawFaceUV - 0.5);		
	
  	HexagonIndex = vec2(rhombusIndex + boxFrontSides - diagonalTriangles*Triangulation);
	 
  	BoxRightSide = 1- max(diagonalTriangles, 1-boxFrontSides);
  	BoxLeftSide = diagonalTriangles+Triangulation.x;
  	BoxLeftSide -= max(0, BoxLeftSide-1)*2.0;
  	BoxLeftSide = 1-max(BoxLeftSide, BoxRightSide);
  	BoxUpperSide =1-BoxLeftSide-BoxRightSide;
   	DistanceToBorder = distanceToBorder;
	DistanceToCenter = distanceToCenter;
  	BoxSides = vec4(BoxUpperSide, BoxLeftSide, BoxRightSide,1);
  	BoxDisplacement = (1-fract(fragCoord.y+fract(HexagonIndex.x*0.5)))*BoxUpperSide;
  	BoxDisplacement += fract((rhombusUV.x+rhombusUV.y)*0.5)*BoxRightSide; 
  	BoxDisplacement += fract((rhombusUV.yx-2.0*rhombusUV.xy).x*0.5)*BoxLeftSide*(1-diagonalTriangles);
  	BoxDisplacement += fract((rhombusUV.yx-2.0*rhombusUV.xy).x*0.5+0.5)*BoxLeftSide*diagonalTriangles; 
  	ColorID = vec4 (RAND(HexagonIndex,0.0), RAND(HexagonIndex,1.0) );
  	//fragColor = vec4( distanceToCenter); 
}



        