// https://www.shadertoy.com/view/ttsyRB

// Fork of "3d simplex noise" by nikat. https://shadertoy.com/view/XsX3zB
// 2020-06-17 16:05:37

/* https://www.shadertoy.com/view/XsX3zB
 *
 * The MIT License
 * Copyright  2013 Nikita Miropolskiy
 * 
 * ( license has been changed from CCA-NC-SA 3.0 to MIT
 *
 *   but thanks for attributing your source code when deriving from this sample 
 *   with a following link: https://www.shadertoy.com/view/XsX3zB )
 *
 * ~
 * ~ if you're looking for procedural noise implementation examples you might 
 * ~ also want to look at the following shaders:
 * ~ 
 * ~ Noise Lab shader by candycat: https://www.shadertoy.com/view/4sc3z2
 * ~
 * ~ Noise shaders by iq:
 * ~     Value    Noise 2D, Derivatives: https://www.shadertoy.com/view/4dXBRH
 * ~     Gradient Noise 2D, Derivatives: https://www.shadertoy.com/view/XdXBRH
 * ~     Value    Noise 3D, Derivatives: https://www.shadertoy.com/view/XsXfRH
 * ~     Gradient Noise 3D, Derivatives: https://www.shadertoy.com/view/4dffRH
 * ~     Value    Noise 2D             : https://www.shadertoy.com/view/lsf3WH
 * ~     Value    Noise 3D             : https://www.shadertoy.com/view/4sfGzS
 * ~     Gradient Noise 2D             : https://www.shadertoy.com/view/XdXGW8
 * ~     Gradient Noise 3D             : https://www.shadertoy.com/view/Xsl3Dl
 * ~     Simplex  Noise 2D             : https://www.shadertoy.com/view/Msf3WH
 * ~     Voronoise: https://www.shadertoy.com/view/Xd23Dh
 * ~ 
 *
 */

#enum Projection UV Top Left Front
#define UV ioUV.xyxy
#define Top ioFragCoord.xzxz
#define Left ioFragCoord.zyzy
#define Front ioFragCoord.xyxy

/* discontinuous pseudorandom uniformly distributed in [-0.5, +0.5]^3 */
vec3 random3(vec3 c) {
	float j = 4096.0*sin(dot(c,vec3(17.0, 59.4, 15.0)));
	vec3 r;
	r.z = fract(512.0*j);
	j *= .125;
	r.x = fract(512.0*j);
	j *= .125;
	r.y = fract(512.0*j);
	return r-0.5;
    //return normalize(r-0.5)*.5;
}

/* skew constants for 3d simplex functions */
 float F3 =  0.3333333;
 float G3 =  0.1666667;

/* 3d simplex noise */
vec4 simplex3d(vec3 p) {
	 /* 1. find current tetrahedron T and it's four vertices */
	 /* s, s+i1, s+i2, s+1.0 - absolute skewed (integer) coordinates of T vertices */
	 /* x, x1, x2, x3 - unskewed coordinates of p relative to each of T vertices*/
	 
	 /* calculate s and x */
	 vec3 s = floor(p + dot(p, vec3(F3)));
	 vec3 x = p - s + dot(s, vec3(G3));
	 
	 /* calculate i1 and i2 */
	 vec3 e = step(vec3(0.0), x - x.yzx);
	 vec3 i1 = e*(1.0 - e.zxy);
	 vec3 i2 = 1.0 - e.zxy*(1.0 - e);
	 	
	 /* x1, x2, x3 */
	 vec3 x1 = x - i1 + G3;
	 vec3 x2 = x - i2 + 2.0*G3;
	 vec3 x3 = x - 1.0 + 3.0*G3;
	 
	 /* 2. find four surflets and store them in d */
	 vec4 w, d;
	 
	 /* calculate surflet weights */
	 w.x = dot(x, x);
	 w.y = dot(x1, x1);
	 w.z = dot(x2, x2);
	 w.w = dot(x3, x3);
	 
	 /* w fades from 0.6 at the center of the surflet to 0.0 at the margin */
	 w = max(0.6 - w, 0.0);
	 
	 /* calculate surflet components */
	 d.x = dot(random3(s), x);
	 d.y = dot(random3(s + i1), x1);
	 d.z = dot(random3(s + i2), x2);
	 d.w = dot(random3(s + 1.0), x3);
	 
	 /* multiply d by w^4 */
	 w *= w;
	 w *= w;
	 d *= w;
	 
	 /* 3. return the four surflets */
	 //return dot(d, vec4(52.0));
    return 70.*d;
}

vec4 variations(vec4 n) {
    vec4 an = abs(n);
    vec4 s = vec4(
        dot( n, vec4(1.) ),
        dot( an,vec4(1.) ),
        length(n),
        max(max(max(an.x, an.y), an.z), an.w) );
    
    float t =.45;
    if(iMouse.xy!=vec2(0))
    t = iMouse.x/iResolution.x;
    
    return vec4(
		// worms
		max(0., 1.25*( s.y*t-abs(s.x) )/t),
		// cells
    	pow( (1.+t)*( (1.-t)+(s.y-s.w/t)*t), 2.), //step( .7, (1.+t)*( (1.-t)+(s.y-s.w/t)*t) ),
		.75*s.y,
    	.5+.5*s.x);
}

/* const matrices for 3d rotation */
 mat3 rot1 = mat3(-0.37, 0.36, 0.85,-0.14,-0.93, 0.34,0.92, 0.01,0.4);
 mat3 rot2 = mat3(-0.55,-0.39, 0.74, 0.33,-0.91,-0.24,0.77, 0.12,0.63);
 mat3 rot3 = mat3(-0.71, 0.52,-0.47,-0.08,-0.72,-0.68,-0.7,-0.45,0.56);

/* directional artifacts can be reduced by rotating each octave */
vec4 simplex3d_fractal(vec3 m) {
    return   0.5333333*variations( simplex3d(m*rot1) 	 )
			+0.2666667*variations( simplex3d(2.0*m*rot2) )
			+0.1333333*variations( simplex3d(4.0*m*rot3) )
			+0.0666667*variations( simplex3d(8.0*m) 	 );
}

void mainImage(out float Worms, out float Worms2,  out float Voronoi,  out float Cells,  out float Micro,  out float Noise,  in vec3 fragCoord(knot = Projection) )
{
	vec3 p3 = fragCoord;
	
    vec4 s1, s2;
	
    
	s1 = variations(simplex3d(p3*16.0) );
	s2 = simplex3d_fractal(p3*8.0+8.0);
	
	Worms = s1.x;
	Worms2 = s2.x;
    Voronoi = s1.y;
    Cells = s2.y;
	Micro = s1.z;
	Noise = s2.z;
        
}  