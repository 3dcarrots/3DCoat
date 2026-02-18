#enum Projection UV Top Left Front
#define UV ioUV.xyxy
#define Top ioFragCoord.xzxz
#define Left ioFragCoord.zyzy
#define Front ioFragCoord.xyxy

in float Noise(min=0.0, max=1.0);
in float Blur(min=0.0, max=1.0);
in vec2 fragCoord(knot = Projection);

out float DistanceToPoint;// distance from current pixel to point
out color ColorID;

vec3 hash( vec2 p )
{
    vec3 q = vec3( dot(p,vec2(127.1,311.7)), 
				   dot(p,vec2(269.5,183.3)), 
				   dot(p,vec2(419.2,371.9)) );
	return fract(sin(q)*43758.5453);
}



	float k = 1.0+63.0*pow(1.0-Blur,6.0); 

    vec2 i = floor(fragCoord);
    vec2 f = fract(fragCoord);
    
	float WeightSumm = 0.0;
	DistanceToPoint = 100;
	ColorID = color(0.0); 
    for( int y=-2; y<=2; y++ ) 
    for( int x=-2; x<=2; x++ )
    {
        vec2  g = vec2( x, y );
		vec3  o = hash( i + g )*vec3(Noise, Noise, 1.0);
      	vec3  colorID = hash( i + g + vec2(123, 321) );
		vec2  d = g - f + o.xy;
		float weight = pow( 1.0-smoothstep(0.0,1.414,length(d)), k );//weight of influence current cell to current pixel
		WeightSumm += weight;
    	DistanceToPoint = min(DistanceToPoint,length(d));
      	ColorID += color(colorID, o.z)*weight; 
    }
	ColorID /= WeightSumm;
  
	
  
