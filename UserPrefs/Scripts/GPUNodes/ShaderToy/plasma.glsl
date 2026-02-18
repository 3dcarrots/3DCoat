//Source for voronoi code : https://www.shadertoy.com/view/Xd23Dh
//Source for noise code: https://www.shadertoy.com/view/Msf3WH


#enum Projection UV Top Left Front
#define UV ioUV.xyxy
#define Top ioFragCoord.xzxz
#define Left ioFragCoord.zyzy
#define Front ioFragCoord.xyxy


vec3 hash3( vec2 p )
{
    vec3 q = vec3( dot(p,vec2(127.1,311.7)), 
				   dot(p,vec2(269.5,183.3)), 
				   dot(p,vec2(419.2,371.9)) );
	return fract(sin(q)*43758.5453);
}

float voronoise( in vec2 p, float u, float v ,in float scale)
{
    p = p*scale;
	float k = 1.0+63.0*pow(1.0-v,6.0);

    vec2 i = floor(p);
    vec2 f = fract(p);
    
	vec2 a = vec2(0.0,0.0);
    for( int y=-2; y<=2; y++ )
    for( int x=-2; x<=2; x++ )
    {
        vec2  g = vec2( x, y );
		vec3  o = hash3( i + g )*vec3(u,u,1.0);
		vec2  d = g - f + o.xy;
		float w = pow( 1.0-smoothstep(0.0,1.414,length(d)), k );
		a += vec2(o.z*w,w);
    }
	
    return a.x/a.y;
}

vec2 hash(in vec2 p, in float fac ) // replace this by something better
{
	p = vec2( dot(p,vec2(127.1*fac,311.7*fac)), dot(p,vec2(269.5*fac,183.3*fac)) );
	return -1.0 + 2.0*fract(sin(p)*43758.5453123*fac);
}

float noise( in vec2 p , in float fac)
{
    const float K1 = 0.366025404; // (sqrt(3)-1)/2;
    const float K2 = 0.211324865; // (3-sqrt(3))/6;

	vec2  i = floor( p + (p.x+p.y)*K1 );
    vec2  a = p - i + (i.x+i.y)*K2;
    float m = step(a.y,a.x); 
    vec2  o = vec2(m,1.0-m);
    vec2  b = a - o + K2;
	vec2  c = a - 1.0 + 2.0*K2;
    vec3  h = max( 0.5-vec3(dot(a,a), dot(b,b), dot(c,c) ), 0.0 );
	vec3  n = h*h*h*h*vec3( dot(a,hash(i+0.0,fac)), dot(b,hash(i+o,fac)), dot(c,hash(i+1.0,fac)));
    return dot( n, vec3(70.0) );
}
float combine(in vec2 p, in float fac, in float scale)
{
    vec2 uv = p*vec2(iResolution.x/iResolution.y,1.0);
	
    
	float f = 0.0;
    uv *= scale;
    mat2 m = mat2( 1.6,  1.2, -1.2,  1.6 );
    f  = 0.5000*noise( uv , fac); uv = m*uv;
    f += 0.2500*noise( uv , fac); uv = m*uv;
    f += 0.1250*noise( uv , fac); uv = m*uv;
    f += 0.0625*noise( uv , fac); uv = m*uv;

	f = 0.5 + 0.5*f;
	
    //f *= smoothstep( 0.0, 0.005, abs(p.x-0.6) );
    
    return f;
}

void mainImage( out vec4 fragColor, in vec2 fragCoord(knot = Projection) )
{
    vec2 p = fragCoord.xy / iResolution.xy+vec2(iTime*0.005,iTime*0.008);
    
    //mouse position corrected for resolution (0 to 1)
    vec3 mouseCorr = vec3(iMouse.xy/iResolution.xy,0.);
    //z component stores whether the user clicks or not
    if(iMouse.z>0.)
    {
        mouseCorr.z=1.;
    }
    
    //"Random" factors for various functions below
    float fac1 = 1.764;
    float fac2 = 2.1938;
    float fac3 = 5.1394;
    float fac4 = 0.1938;
    float fac5 = 3.1394;
    
    //Global scale of distortion
    float distortionScale = 4.;
    
    //Two different oscillators, for time variations
    float osc = 1.+sin(iTime*0.3)*0.5;
    float osc2 = 0.75+sin(iTime*0.47)*0.25;
    
    //Distortion offset, used in pretty much every function below
    vec2 offset = vec2(combine(p,fac1,distortionScale)-.5,combine(p,fac2,distortionScale)-.5);
    
    //
    float noiseComp1 = combine(p+offset*osc,fac3,6.0);
    float noiseComp2 = combine(p+offset*osc,fac4,7.0);
    float noiseComp3 = combine(p+offset*osc,fac5,8.0);
    float vorComp = voronoise(p+offset*osc,1.,0.,10.0);
    
    //Exponents for color saturation
    float e1 = 0.1+fract(vorComp*fac1)*(1.+cos(iTime*0.0017));
    float e2 = 0.1+fract(vorComp*fac2)*(1.+cos(iTime*0.0017));
    float e3 = 0.1+fract(vorComp*fac3)*(1.+cos(iTime*0.0017));
    
    //RGB components
    float rComp = combine(p+offset*osc2,fac2*(fac4),2.0);
    float gComp = combine(p+offset*osc2,fac2*(fac5),2.0);
    float bComp = combine(p+offset*osc2,fac3*(fac2),2.0);
    
    //Mouse controls saturation in a weird way depending on position
    if(mouseCorr.z>0.)
    {
        e1*=(.5+.5*sin(3.*mouseCorr.x+1.342));
        e2*=(.5+.5*sin(2.*mouseCorr.y+.8304));
        e3*=(.5+.5*sin(5.*mouseCorr.x*mouseCorr.y-.1933));
    }
    
    //each component is getting saturated randomly
    vec3 col = vec3(pow(noiseComp1,e1*rComp),
    pow(noiseComp2,e2*gComp),
    pow(noiseComp3,e3*bComp));
    //vec3 col = vec3(vorComp*noiseComp);
    
    fragColor = vec4(col,1.0);
}