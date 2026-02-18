// https://www.shadertoy.com/view/tldSRj
// The MIT License
// Copyright � 2020 Inigo Quilez
// Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


// A wave based noise, similar to gabor and all its variants but much
// simplified, originially explored in shadertoy by user robobo1221
// in this shader: https://www.shadertoy.com/view/wttSRj
//
// It is comparable in speed to traditional gradient noise (if the
// architecture supports fast sin/cos, like GPUs do anyways), but
// slower than value noise of course. The advantage is that it's
// infinitely derivable. It can also be easily animated by moving
// the waves over time or rotating the gradients, which is fun.
//
// But the main advantage is that it can generate a wromy look, as
// in robobo1221's original shader, by changing the kF constant in 
// line 45 to be closer to 6



// Value    Noise 2D, Derivatives: https://www.shadertoy.com/view/4dXBRH
// Gradient Noise 2D, Derivatives: https://www.shadertoy.com/view/XdXBRH
// Value    Noise 3D, Derivatives: https://www.shadertoy.com/view/XsXfRH
// Gradient Noise 3D, Derivatives: https://www.shadertoy.com/view/4dffRH
// Value    Noise 2D             : https://www.shadertoy.com/view/lsf3WH
// Value    Noise 3D             : https://www.shadertoy.com/view/4sfGzS
// Gradient Noise 2D             : https://www.shadertoy.com/view/XdXGW8
// Gradient Noise 3D             : https://www.shadertoy.com/view/Xsl3Dl
// Simplex  Noise 2D             : https://www.shadertoy.com/view/Msf3WH
// Wave     Noise 2D             : https://www.shadertoy.com/view/tldSRj



#enum Projection UV Top Left Front
#define UV ioUV.xyxy
#define Top ioFragCoord.xzxz
#define Left ioFragCoord.zyzy
#define Front ioFragCoord.xyxy


// You should replace this hash by one that you like and meets
// your needs. This one is here just as example and should not
// be used in production.
vec2 g( vec2 n ) { return sin(n.x*n.y*vec2(12,17)+vec2(1,2)); }
//vec2 g( vec2 n ) { return sin(n.x*n.y+vec2(0,1.571)); } // if you want the gradients to lay on a circle

float noise(vec2 p)
{
    const float kF = 2.0;  // make 6 to see worms
    
    vec2 i = floor(p);
	vec2 f = fract(p);
    f = f*f*(3.0-2.0*f);
    return mix(mix(sin(kF*dot(p,g(i+vec2(0,0)))),
               	   sin(kF*dot(p,g(i+vec2(1,0)))),f.x),
               mix(sin(kF*dot(p,g(i+vec2(0,1)))),
               	   sin(kF*dot(p,g(i+vec2(1,1)))),f.x),f.y);
}

void mainImage( out float Noise, out float Perlin, in vec2 fragCoord(knot = Projection) )
{
    vec2 p = fragCoord/iResolution.xy;

	vec2 uv = p*vec2(iResolution.x/iResolution.y,1.0);

    float f = 0.0;
	
    // left: noise
	Noise = noise( 24.0*uv + iTime*4.0 );
    // right: fractal noise (4 octaves)
		uv *= 8.0;
        uv += iTime*4.0/3.0;
        const mat2 m = mat2( 1.6,  1.2, -1.2,  1.6 );
	Perlin  = 0.5000*noise( uv ); uv = m*uv;
	Perlin += 0.2500*noise( uv ); uv = m*uv;
	Perlin += 0.1250*noise( uv ); uv = m*uv;
	Perlin += 0.0625*noise( uv ); uv = m*uv;

	Noise = 0.5 + 0.5*Noise;
	Perlin = 0.5 + 0.5*Perlin;
	
} 