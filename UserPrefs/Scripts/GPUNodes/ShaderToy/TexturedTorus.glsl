// surface phasor noise , Sylvain Lefebvre
// see https://hal.archives-ouvertes.fr/hal-02118508 for details
//
// The MIT License
// Copyright � 2019 Sylvain Lefebvre
// Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

int   MaxInt = 2147483647; // 2^31 - 1

#define M_PI   3.1415926535897932385

#enum Projection UV Top Left Front
#define UV ioUV.xyxy
#define Top ioFragCoord.xzxz
#define Left ioFragCoord.zyzy
#define Front ioFragCoord.xyxy

float  _a            = 6.0;   // noise bandwidth
float  _F_0          = 7.0;  // main frequency
float  _F_w          = 0.0;   // frequency random spread
float  _omega_0      = 0.0;   // main orientation
float  _omega_w      = 0.3;   // orientation spread
int    Seed          = 42;    // random seed

int ImpPerKernel  = 32; // impulses per kernel, higher is better but slower

vec3 Vup = vec3(0.0,0.0,1.0);

//-----------------------------------------------------------------------------

int hash_linear(ivec4 ijkl)
{
  return (ijkl.x + (ijkl.y << 10) + (ijkl.z << 20));
}

//-----------------------------------------------------------------------------

int hash(ivec2 ij)
{
  return hash_linear( ij.xyxy );
}

int hash3(ivec3 ijk)
{
  return hash_linear( ijk.xyzx );
}

 int MaxHash = MaxInt;

//-----------------------------------------------------------------------------

float drand(int r, out int _r)
{
  _r = r * 3039177861;
  return float(_r & MaxInt) / float(MaxInt);
}

//-----------------------------------------------------------------------------

 float truncate = 0.01;

float kernelRadius(float ka)
{
  return (sqrt( - log( truncate ) / M_PI ) / float(ka));
}

// -----------------------------------------------------

float gaussian(vec2 uv, float a)
{
  // gaussian
  float lsq = dot(uv, uv);
  return exp(-M_PI * (a*a) * lsq);
}

//-----------------------------------------------------------------------------
 
vec2 sampleCellSrf(
  ivec3 ijk, vec3 uvw,
  vec3  wu, vec3 wv, vec3  wn, // surface frame (u,v, normal)
  float f0, float o0, float ow, float a, float kr)
{  

  // init random number generator 
  int   h = 1 + hash3(ijk);
  int rnd = Seed + h;
  
  vec2 phasor  = vec2(0.0);
    
  vec3  cellsz = vec3(2.0*kr);
  
  int   N = ImpPerKernel;
  for (int nIter = 0; nIter < N; nIter++) {
    // generate a 3D sample in the virtual grid    
    float rx  = drand(rnd, rnd);
    float ry  = drand(rnd, rnd);
    float rz  = drand(rnd, rnd);
    vec3 ctr3 = vec3(rx, ry, rz);

    // project it to the surface
    vec3   v           = (uvw - ctr3) * cellsz;  
    vec2   x_minus_x_i = vec2(dot(v, wu), dot(v, wv));
    vec2   k           = vec2(0.0,0.0);
    vec3  wctr         = (vec3(ijk) + ctr3);
    vec2  plane_uv     = vec2(dot(wctr, wu), dot(wctr, wv)) * cellsz.xy;
    float o0 = _omega_0;
    // randomize orientation
    float o   = o0;
    float o_r = drand(rnd, rnd);
    float o1  = o0 - ow;
    float o2  = o0 + ow;
    o         = o1 + o_r * (o2 - o1);
    // randomize freq
    float f;
    float f_r = drand(rnd, rnd);
    float f1  = f0 - _F_w;
    float f2  = f0 + _F_w;
    f         = f1 + f_r * (f2 - f1);
    // if within kernel radius (kernel might contribute to the result)
    if (dot(v, v) < kr*kr*2.0) {
      vec2  u_i   = vec2(cos(o), sin(o));
      float phase = 2.0 * M_PI * f * dot(u_i,x_minus_x_i);
      // compute weight, takes into acount distnace between
      // 3d sample and surface (samples far away contribute less)
      float  z    = max(0.0, 1.0 - abs(dot(v, wn) / kr));
      float  i    = z * gaussian(x_minus_x_i,a);
      // add kernel contribution
      phasor += i * vec2(cos(phase),sin(phase));
    }
  }
  return phasor;
}

// ---------------------------------------------------------------

vec2 makeNoiseSrf(vec3 tuv,vec3 wu, vec3 wv,vec3 nrm)
{
  vec2 phasor = vec2(0.0,0.0);
  vec3 uvw    = tuv;
  // sparse convolution
  float kr = kernelRadius(_a);
  // generate virtual grid coordinates
  vec3  cellsz = vec3(2.0*kr);
  vec3  _ijk   = uvw / cellsz;
  ivec3 ijk    = ivec3(round(_ijk));
  vec3  fijk   = _ijk - vec3(ijk);
  // sample eight 3d cells in the virtual grid
  ivec3 nd = ivec3(0);
  nd.x = (fijk.x > 0.5) ? 1 : -1;
  nd.y = (fijk.y > 0.5) ? 1 : -1;
  nd.z = (fijk.z > 0.5) ? 1 : -1;
  for (int k = 0; k < 2; k++) {
    for (int j = 0; j < 2; j++) {
      for (int i = 0; i < 2; i++) {
        phasor += sampleCellSrf(
          ijk + ivec3(i, j, k)*nd, fijk - vec3(i, j, k) * vec3(nd), 
          wu, wv, nrm, 
          _F_0, _omega_0, _omega_w, _a, kr);
      }
    }
  }
  return phasor; 
}

// ---------------------------------------------------------------

// Phasor noise returns a vec2(.,.) which is directly the phasor vector
// - the atan of the vector gives the instantaneous phase
// - the modulus gives the gabor intensity
vec2 phasorNoiseSrf(vec3 point, vec3 normal)
{
  vec3 tuv = point;
  vec3 nrm = normalize(normal);
  // generate a tangential u,v, frame
  vec3 wu  = normalize(cross(nrm, Vup));
  vec3 wv  = cross(wu, nrm);
  // make some noise!
  vec2 phasor = makeNoiseSrf(tuv, wu, wv, nrm);
  return phasor;
}

// ---------------------------------------------------------------
// Torus cracks with surface phasor noise, Sylvain Lefebvre
// see https://hal.archives-ouvertes.fr/hal-02118508 for details
// The MIT License
//
// -------------------------------------------------------
// routine for ray-torus intersection, https://www.shadertoy.com/view/4sBGDy
// The MIT License
// Copyright � 2014 Inigo Quilez
// Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
// -------------------------------------------------------
float iTorus( in vec3 ro, in vec3 rd, in vec2 torus )
{
	float Ra2 = torus.x*torus.x;
	float ra2 = torus.y*torus.y;
	
	float m = dot(ro,ro);
	float n = dot(ro,rd);
		
	float k = (m - ra2 - Ra2)/2.0;
	float a = n;
	float b = n*n + Ra2*rd.z*rd.z + k;
	float c = k*n + Ra2*ro.z*rd.z;
	float d = k*k + Ra2*ro.z*ro.z - Ra2*ra2;
	
    //----------------------------------

	float p = -3.0*a*a     + 2.0*b;
	float q =  2.0*a*a*a   - 2.0*a*b   + 2.0*c;
	float r = -3.0*a*a*a*a + 4.0*a*a*b - 8.0*a*c + 4.0*d;
	p /= 3.0;
	r /= 3.0;
	float Q = p*p + r;
	float R = 3.0*r*p - p*p*p - q*q;
	
	float h = R*R - Q*Q*Q;
	float z = 0.0;
	if( h < 0.0 )
	{
		float sQ = sqrt(Q);
		z = 2.0*sQ*cos( acos(R/(sQ*Q)) / 3.0 );
	}
	else
	{
		float sQ = pow( sqrt(h) + abs(R), 1.0/3.0 );
		z = sign(R)*abs( sQ + Q/sQ );

	}
	
	z = p - z;
	
    //----------------------------------
	
	float d1 = z   - 3.0*p;
	float d2 = z*z - 3.0*r;

	if( abs(d1)<1.0e-4 )
	{
		if( d2<0.0 ) return -1.0;
		d2 = sqrt(d2);
	}
	else
	{
		if( d1<0.0 ) return -1.0;
		d1 = sqrt( d1/2.0 );
		d2 = q/d1;
	}

    //----------------------------------
	
	float result = 1e20;

	h = d1*d1 - z + d2;
	if( h>0.0 )
	{
		h = sqrt(h);
		float t1 = -d1 - h - a;
		float t2 = -d1 + h - a;
		     if( t1>0.0 ) result=t1;
		else if( t2>0.0 ) result=t2;
	}

	h = d1*d1 - z - d2;
	if( h>0.0 )
	{
		h = sqrt(h);
		float t1 = d1 - h - a;
		float t2 = d1 + h - a;
		     if( t1>0.0 ) result=min(result,t1);
		else if( t2>0.0 ) result=min(result,t2);
	}

	return result;
}

// df(x)/dx
vec3 nTorus( in vec3 pos, vec2 tor )
{
	return normalize( pos*(dot(pos,pos)- tor.y*tor.y - tor.x*tor.x*vec3(1.0,1.0,-1.0)));
}

float max2(vec2 v) { return max(v.x,v.y); }
float min2(vec2 v) { return min(v.x,v.y); }

// -------------------------------------------------------
// Main
// -------------------------------------------------------

void mainImage( out vec4 fragColor, in vec2 fragCoord(knot = Projection) )
{
    // camera movement	
	float an = 1.7;
	vec3 ro  = vec3( 0.0, -1.5, 2.5*sin(an) );
    vec3 ta  = vec3( 0.0, -0.15, 0.0 );
    // camera matrix
    vec3 ww  = normalize( ta - ro );
    vec3 uu  = normalize( cross(ww,vec3(0.0,1.0,0.0) ) );
    vec3 vv  = normalize( cross(uu,ww));    
    vec3 tot = vec3(0.0);    
    // pixel coordinates
    vec2 p   = (-iResolution.xy + 2.0*fragCoord)/iResolution.y;
    // create view ray
    vec3 rd = normalize( p.x*uu + p.y*vv + 1.5*ww );
    // raytrace torus
    vec2 torus = vec2(1.0,0.45 + 0.04 * (1.0 - cos(iTime)));
    float t    = iTorus( ro, rd, torus );
    // shading/lighting	
    vec3 col = vec3(0.0);
    if( t>0.0 && t<100.0 ) {
        // there is a hit, get the normal
        vec3 pos = ro + t*rd;
        vec3 nor = nTorus( pos, torus );        
        // create cracks with phasor
        // -> first phasor
        _omega_0     = M_PI/2.0;
        vec2 phasor1 = phasorNoiseSrf(pos,nor);
        float u      = abs(0.5 - fract(atan(phasor1.y,phasor1.x) / (2.0*M_PI)));
        // -> second phasor, crossing the first
        _omega_0     = M_PI/2.0 + M_PI/7.0;
        vec2 phasor2 = phasorNoiseSrf(pos,nor);
        float v      = abs(0.5 - fract(atan(phasor2.y,phasor2.x) / (2.0*M_PI)));
        // width of the cracks
        float w = max(0.0, 0.15 * (1.0 - cos(iTime)) - 0.02);
        // combine phasor noises into the cracks pattern        
        float h = 1.0 - clamp( (max2(abs(vec2(u,v) - vec2(0.5,0.5))) - (0.5-w))/(w) ,0.0,1.0) > 0.5 ? 1.0 : 0.0;
        // shaed
        float dif = clamp( dot(nor,vec3(0.57703)), 0.0, 1.0 );
        float amb = clamp( 0.5 + 0.5*dot(nor,vec3(0.0,1.0,0.0)), 0.0, 1.0 );
        // done
        col       = vec3(h*(dif+amb));
    } else {
        // no hit, background color
        col = vec3(0.9);
    }

    col = sqrt( col );

    tot += col;

	fragColor = vec4( tot, 1.0 );
}