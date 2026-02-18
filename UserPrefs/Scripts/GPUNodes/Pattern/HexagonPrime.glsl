out float BoxDisplacement;//box displacemenet
out vec4 BoxSides;// box sides
out float BoxUpperSide;// box upper side
out float BoxLeftSide;// box left side
out float BoxRightSide;// box right side
out float DistanceToCenter;// distance from current pixel to center of hexagon
out float DistanceToBorder;// distance from current pixel to closest border
out vec2 HexagonIndex;// hexagon index
out vec4 ColorID;// color ID
out vec2 FaceUV;// local UV coordinates for current hexagon


vec2 RAND(vec2 tileIndex, float fracRandomiser)//function for creation simple noise
{
  return fract(tan(dot(tileIndex+ vec2(1245,2566) ,tileIndex+vec2(7856,2156)+ fracRandomiser) / (tileIndex.y+4523)*(tileIndex+ vec2(2123, 5428))));// somthing random for noise 
}



void mainImage( in vec2 fragCoord(knot = ioUV)  ) 
{
	vec2 skewedUV = vec2( fragCoord.x*1.1547005384/* 2/sqrt(3) */, fragCoord.y + fragCoord.x*0.5773502692/* 1/sqrt(3) */ );// skew of coordinates 
	
	vec2 rhombusIndex = floor(skewedUV);// rhombus index
	vec2 rhombusUV = skewedUV-rhombusIndex;// global UV coordinates for rhombus
  
  
	// diagonal grouping of rhombuses by 3
	float diagonals3 = mod(rhombusIndex.x + rhombusIndex.y, 3.0);

	float boxFrontSides = step(1.0,diagonals3);// grouping front sides rhombus
	float diagonalTriangles = step(2.0,diagonals3);//groping of two diagonal triangles for defineding sides of hexagon
	vec2  Triangulation  = step(rhombusUV.xy,rhombusUV.yx);//groping odd and pair triangles for definding sides of hexagon
	
    float distanceToBorder = dot(Triangulation, 1.0-rhombusUV.yx + boxFrontSides*(rhombusUV.x+rhombusUV.y-1.0) + diagonalTriangles*(rhombusUV.yx-2.0*rhombusUV.xy));// distance to border

		
	vec2 globalShiftedUV = vec2( skewedUV.x + floor(0.5+fragCoord.y/1.5), 4.0*fragCoord.y/3.0 )*0.5 + 0.5;// global shifted UV coordinates
  	vec2 rawFaceUV = fract(globalShiftedUV); // raw coordinates of form
	float distanceToCenter = length(rawFaceUV - 0.5);// distance from current pixel to center		
	
  	HexagonIndex = vec2(rhombusIndex + boxFrontSides - diagonalTriangles*Triangulation);// hexagon index
	 
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
  	FaceUV = fract(fragCoord/vec2(1.75320, 2.0)+vec2(0.5, 0.5)+HexagonIndex.x*vec2(0.5, 1.75320)+ (HexagonIndex.x+HexagonIndex.y)*vec2(0.0, 0.5));	
  	ColorID = vec4 (RAND(HexagonIndex,0.0), RAND(HexagonIndex,1.0) );
  
  	//fragColor = vec4( distanceToCenter); 
}



         