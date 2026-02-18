

in vec4 Source;

out vec4 Result;

vec2 RAND(vec2 tileIndex, float fracRandomiser)//function for creation simple noise
{
  return fract(tan(dot(tileIndex+ vec2(1245,2566) ,tileIndex+vec2(7856,2156)+ fracRandomiser) / (tileIndex.y+4523)*(tileIndex+ vec2(2123, 5428))));// somthing random for noise 
}

 Result = vec4(RAND(Source.xy, 1.0), RAND(Source.zw, 2.0));      