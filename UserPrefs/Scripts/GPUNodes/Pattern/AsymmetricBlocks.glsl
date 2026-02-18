//https://www.shadertoy.com/view/7t3BWf
////www.shadertoy.com/view/Ws3GRs
in vec2 fragCoord(knot = ioUV);
in float Radius(min = 0.0, max = 1.0);
in float Randomise (min = 0.0, max = 2.0);
in float MaskThreshold(value = 0.01, min = 0.00, max = 1.0);
in float Sharpness(value = 100.0, min =1.0, max = 100.0);

out float Blocks;
out vec2 BlockSize;
out vec2 LocalUV;
out float Corners;
out vec4 ColorId;
out float Mask;

vec2 RAND(vec2 tileIndex, float fracRandomiser)//function for creation simple noise
{
  return fract(tan(dot(tileIndex+ vec2(1245,2566) ,tileIndex+vec2(7856,2156)+ fracRandomiser) / (tileIndex.y+4523)*(tileIndex+ vec2(2123, 5428))));// somthing random for noise 
}

uint triple32(uint x)
{
    x ^= x >> 17;
    x *= 0xed5ad4bbU;
    x ^= x >> 11;
    x *= 0xac4c1b51U;
    x ^= x >> 15;
    x *= 0x31848babU;
    x ^= x >> 14;
    return x;
}
float hashint(uint x)
{
    return float(triple32(x)) / float(0xffffffffU);
}
float hash(uvec2 v)
{
  
    return mix(0.5, mix(0.2, 0.8, hashint(v.x + triple32(v.y))), Randomise);
  
}

vec2 BlockSizeBuf;
vec2 LocalUVBuf;
float box( in vec2 p, in vec2 b ) // https://iquilezles.org/articles/distfunctions2d/ by iq
{
    vec2 d = abs(p)-b;
  	BlockSizeBuf = vec2(1.0, 1.0);
    return length(max(d,0.0)) + min(max(d.x,d.y),0.0);
}

float sdRoundedBox( in vec2 p, in vec2 b ) // https://iquilezles.org/articles/distfunctions2d/
{
  	
    vec2 q = abs(p)-b+Radius;
  	BlockSizeBuf = b;
  	LocalUVBuf = p;
    return min(max(q.x,q.y),0.0) + length(max(q,0.0)) - Radius;
}

float box2(vec2 p, vec2 p0, vec2 p1) // min-max box
{
  	
    float result = sdRoundedBox(p-(p1+p0)/2.0, (p1-p0)/2.0);
  	if (result < Blocks)
    {
      BlockSize = BlockSizeBuf;
      LocalUV = (LocalUVBuf/BlockSizeBuf+1.0)*0.5;            
      Blocks = result;
     }
  	return result;
}

void  blocks(in vec2 p)
{
    vec2 q = fract(p); // local coordinates inside tile
    p = floor(p); // global coordinates of tile
    ivec2 tile = ivec2(p);
    bool flip = (tile.x & 1) == (tile.y & 1);
    if(flip) // vertical line goes through
    {
        float x = hash(uvec2(tile)); // x-coordinate of vertical line through this tile
        float xsw = hash(uvec2(tile+ivec2(-1,-1))); // x-coordinate of vertical line through south-west tile
        float xnw = hash(uvec2(tile+ivec2(-1,+1))); // x-coordinate of vertical line through north-west tile
        float xse = hash(uvec2(tile+ivec2(+1,-1))); // x-coordinate of vertical line through south-east tile
        float xne = hash(uvec2(tile+ivec2(+1,+1))); // x-coordinate of vertical line through north-east tile
        float yw = hash(uvec2(tile+ivec2(-1, 0))); // y-coordinate of horizontal line through west tile
        float ye = hash(uvec2(tile+ivec2(+1, 0))); // y-coordinate of horizontal line through east tile
        float ys = hash(uvec2(tile+ivec2( 0,-1))); // y-coordinate of horizontal line through south tile
        float yn = hash(uvec2(tile+ivec2( 0,+1))); // y-coordinate of horizontal line through north tile
		 
        box2(q, vec2(xsw-1.0, ys-1.0), vec2(x, yw)); // south-west
        box2(q, vec2(xnw-1.0, yw), vec2(x, yn+1.0)); // north-west
        box2(q, vec2(x, ys-1.0), vec2(xse+1.0, ye)); // south-east
        box2(q, vec2(x, ye), vec2(xne+1.0, yn+1.0)); // north-east
      }          
    else // horizontal line goes through
    {
        float y = hash(uvec2(tile)); // x-coordinate of horizontal line through this tile
        float ysw = hash(uvec2(tile+ivec2(-1,-1))); // y-coordinate of horizontal line through south-west tile
        float ynw = hash(uvec2(tile+ivec2(-1,+1))); // y-coordinate of horizontal line through north-west tile
        float yse = hash(uvec2(tile+ivec2(+1,-1))); // y-coordinate of horizontal line through south-east tile
        float yne = hash(uvec2(tile+ivec2(+1,+1))); // y-coordinate of horizontal line through north-east tile
        float xw = hash(uvec2(tile+ivec2(-1, 0))); // x-coordinate of vertical line through west tile
        float xe = hash(uvec2(tile+ivec2(+1, 0))); // x-coordinate of vertical line through east tile
        float xs = hash(uvec2(tile+ivec2( 0,-1))); // x-coordinate of vertical line through south tile
        float xn = hash(uvec2(tile+ivec2( 0,+1))); // x-coordinate of vertical line through north tile        
          	
      	box2(q, vec2(xw-1.0, ysw-1.0), vec2(xs, y)); // south-west
        box2(q, vec2(xw-1.0, y), vec2(xn, ynw+1.0)); // north-west
        box2(q, vec2(xs, yse-1.0), vec2(xe+1.0, y)); // south-east
        box2(q, vec2(xn, y), vec2(xe+1.0, yne+1.0)); // north-east
                
    }
}
	
		Blocks = 999;
		blocks(fragCoord*10.0);
		Blocks *= 2.0;
		Corners = clamp(Blocks,0.0, 1.0);   
		Blocks = clamp(-Blocks,0.0, 1.0);
		Mask = (Blocks-MaskThreshold)*Sharpness;
		
		// random color for each  face
  		ColorId = vec4(RAND(BlockSize, 1), RAND(BlockSize, 2));//random color  for each face 
		
		    