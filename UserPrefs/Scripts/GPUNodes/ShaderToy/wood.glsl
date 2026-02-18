#define animation false
#enum Projection UV Top Left Front
#define UV ioUV.xyxy
#define Top ioFragCoord.xzxz
#define Left ioFragCoord.zyzy
#define Front ioFragCoord.xyxy

mat2 m = mat2( .1, .1, -.7, .5 );

float noise( in vec2 f ){
  f *= m;
  return ( cos( f.x + .18975 ) * sin( f.y + .494516 ) + .1615246 );
}

mat2 rot( float d ){
float s = sin(d), c = cos(d);
return mat2(c, s, -s, c);
}

float fbm( in vec2 x, in float H )
{    
    float t = 0.0;
    for( int i=0; i<10; i++ )
    {
        float f = pow( 2.0, float(i) );
        float a = pow( f, -H );
        t += a*noise(f*x);
    }
    return t;
}


void mainImage( out vec4 fragColor, in vec2 fragCoord(knot = Projection) )
{
    // Normalized pixel coordinates (from 0 to 1)
    vec2 uv =  fragCoord;
    
    float p = fbm( vec2( fbm( uv - ( animation ? iTime : 0.3 ), 1. ) ), .1 );

    uv += p;

    // Time varying pixel color
    vec3 col = vec3( .154, .116, .08 ) * uv.yxx;


    // Output to screen
    fragColor = vec4(col,1.0);
}