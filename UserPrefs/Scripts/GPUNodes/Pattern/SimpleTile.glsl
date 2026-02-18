
in vec2 Size = 1;// size of the tile
in vec2 Border = 1;//size of the tile border
in vec2 BorderMaskContrast = 1; // contrast of the border
in float RowShift = 0;// rowshift of the tiles
in float RowShiftVariation = 0;// rowshift for each tile
in float WidthVariation(value = 0, min =0.0, max = 1.0);
in float Scale = 1;// scale of the tiles
in float Skew = 0;// skew
in float SkewVariation(value = 0, min =0.0, max = 1.0);

//************************//

out vec2 TileUV;//uv coordinates of the tile
out vec2 UV;// uv coordinates
out vec2 TileIndex;//numeration of rows and columns
out float FaceHeight;//face hieght for face displacement &  normal map 
out float BorderMask;//mask for separate border from face of the tile
out float BorderHeight;// height for displacement & normal map
out vec4 ColorId;//random color  for each face
out vec2 EdgeDir;

vec2 RAND(vec2 tileIndex, float fracRandomiser)//function for creation simple noise
{
  return fract(tan(dot(tileIndex+ vec2(1245,2566) ,tileIndex+vec2(7856,2156)+ fracRandomiser) / (tileIndex.y+4523)*(tileIndex+ vec2(2123, 5428))));// somthing random for noise 
}

void mainImage(  in vec2 fragCoord(knot = ioUV) )// main function
{
	vec2 uv = fragCoord*Size*Scale;// scale uv coordinates for one unit per tile
  	
  	// row skew
  	float rowIndex = floor(uv.y+0.5);//create variable with rows & columns numbers
  	float rowRand =  fract(sin(dot(vec2(rowIndex, 421) , vec2(65.6513, 21.6542))) * 8854.7562)-0.5;// random function for rowSkew
  	float tileV = mix(uv.y - floor(uv.y+0.5), (uv.y - floor(uv.y+0.5))*rowRand, SkewVariation);//
  	uv.x += Skew*tileV;
  	
  	// tile index
   	vec2 tileIndex = floor(uv+vec2(0.5));//create variable with rows & columns numbers
  
  	// tile width variation	
  	rowRand =  fract(sin(dot(vec2(tileIndex.y, 564) , vec2(78.6564, 12.798))) * 9874.2545);// random function for rowWidth
  	uv.x *= 1+rowRand*WidthVariation;
  	Size.x *= 1+rowRand*WidthVariation;
  	
  	// row shift variation
   	rowRand =  fract(sin(dot(vec2(tileIndex.y, 566) , vec2(65.5467, 54.435))) * 6572.5421);// 
  	uv.x += tileIndex.y*RowShift+(rowRand*RowShiftVariation) ;// rowShift of the tiles (shifting the tiles in rowShift walue)
   	
  	// rows and columns
  	vec2 tileIndex2 = abs(trunc(uv));// dividing the tile half parts from each side
  	vec2 tileUV = abs(uv)-tileIndex2;//uv coordinates for each tile from 0 to 1
    vec2 cells = abs(tileUV - vec2(0.5, 0.5));//cells distance to row center and column
  	
  	// pyramids
  	float pyramid = min(cells.x, cells.y);// producing pyramid of the tile
   	
  	// height map
  	vec2 rowHeight = cells-Border*Size*0.01;// row height
  	float height = (min(rowHeight.x, rowHeight.y));//map of heights (result)
  	BorderHeight = clamp(max(-rowHeight.x/Size.x/Border.x*100, -rowHeight.y/Size.y/Border.y*100),0, 1);//height for borders 
  	
  	// edge mask
  	vec2 edgeDir = clamp(rowHeight*BorderMaskContrast/Size*100, 0, 1);//red for horizontal border & green for vertical border
  	float edgeMask = min(edgeDir.x, edgeDir.y);//mask for split  border and face
 	
  	// random color for each  face
  	ColorId = vec4(RAND(tileIndex, 1), RAND(tileIndex, 2));//random color  for each face 
  	
  	// outputs 
  	TileUV = uv - floor(uv+vec2(0.5));//uv coordinates for each tile from 0 to 1
  	UV = uv;//global uv (diferent for each tile
  	TileIndex = tileIndex; //create variable with rows & columns numbers
  	FaceHeight = height;//map of heights (result)
  	BorderMask = edgeMask;//mask for split  border and face
  	EdgeDir = edgeDir;
}           