// "Wavelet Noise" 
// The MIT License
// Copyright � 2020 Martijn Steinrucken
// Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
// Email: countfrolic@gmail.com
// Twitter: @The_ArtOfCode
// YouTube: youtube.com/TheArtOfCodeIsCool
// Facebook: https://www.facebook.com/groups/theartofcode/
//
// I needed something as a base for a cheap water effect and thought this
// might help someone. This has probably been done before cuz its quite a 
// simple concept. 
// See below for an expanded version if you wanna understand how it works!
// Source link https://www.shadertoy.com/view/wsBfzK

#enum Projection UV Top Left Front
#define UV ioUV.xyxy
#define Top ioFragCoord.xzxz
#define Left ioFragCoord.zyzy
#define Front ioFragCoord.xyxy

float WaveletNoise(vec2 p, float z, float k) {
    float d=0.,s=1.,m=0., a;
    for(float i=0.; i<4.; i++) {
        vec2 q = p*s, g=fract(floor(q)*vec2(123.34,233.53));
    	g += dot(g, g+23.234);
		a = fract(g.x*g.y)*1e3;// +z*(mod(g.x+g.y, 2.)-1.); // add vorticity
        q = (fract(q)-.5)*mat2(cos(a),-sin(a),sin(a),cos(a));
        d += sin(q.x*10.+z)*smoothstep(.25, .0, dot(q,q))/s;
        p = p*mat2(.54,-.84, .84, .54)+i;
        m += 1./s;
        s *= k; 
    }
    return d/m;
}

void mainImage( out vec4 fragColor, in vec2 fragCoord(knot = Projection) ) {
    vec2 uv = (fragCoord-.5*iResolution.xy)/iResolution.y;
	vec2 m = iMouse.xy/iResolution.xy;
    
    vec3 col = vec3(0);
    
    col += WaveletNoise(uv*5., iTime, 1.24)*.5+.5; 
    if(col.r>.99) col= vec3(1,0,0); 
    if(col.r<0.01) col = vec3(0,0,1);
    
    fragColor = vec4(col,1.0);
}

/* The function above is a minification of the code below
mat2 Rot(float a) {
    float s = sin(a);
    float c = cos(a);
    return mat2(c, -s, s, c);
}

float Hash21(vec2 p) {
    p = fract(p*vec2(123.34,233.53));
    p += dot(p, p+23.234);
    return fract(p.x*p.y);
}

float GetWavelet(vec2 p, float z, float scale) {
	p *= scale;
    
    vec2 id = floor(p);
    p = fract(p)-.5;
    
    float n = Hash21(id);
    p *= Rot(n*100.);
    float d = sin(p.x*10.+z);

    d *= smoothstep(.25, .0, dot(p,p));
    return d/scale;
}

float WaveletNoise(vec2 p, float phase, float scaleFactor) {
    float d = 0.;
    float scale = 1.;
    float mag=0.;
    for(float i=0.; i<4.; i++) {
        d += GetWavelet(p, phase, scale);
        p = p*mat2(.54,-.84, .84, .54)+i;
        mag += 1./scale;
        scale *= scaleFactor; 
    }
    d /= mag;
    return d;
}
*/
