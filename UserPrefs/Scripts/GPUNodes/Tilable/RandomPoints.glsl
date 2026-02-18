// Tileable Cells. By David Hoskins. 2013.

#define NUM_CELLS	16.0	// Needs to be a multiple of TILES!
#define TILES 		2.0		// Normally set to 1.0 for a creating a tileable texture.

#define SHOW_TILING			// Display yellow lines at tiling locations.
		// Basic movement using texture values.
in vec2 CiclesMask;
//------------------------------------------------------------------------
vec2 Hash2(vec2 p)
{
	

	float r = 523.0*sin(dot(p, vec2(53.3158, 43.6143)));
	return vec2(fract(15.32354 * r), fract(17.25865 * r));
		}

//------------------------------------------------------------------------
float Cells(in vec2 p, in float numCells)
{
	p *= numCells;
	float d = 1.0e10;
	for (int xo = -1; xo <= 1; xo++)
	{
		for (int yo = -1; yo <= 1; yo++)
		{
			vec2 tp = floor(p) + vec2(xo, yo);
			tp = p - tp - Hash2(mod(tp, numCells / TILES));
			d = min(d, dot(tp, tp));
		}
	}
	return sqrt(d);
	//return 1.0 - d;// ...Bubbles.
}

//------------------------------------------------------------------------
void mainImage( out vec4 fragColor, in vec2 fragCoord )
{
	vec2 uv = fragCoord.xy / iResolution.xy;
	
	
	float c = Cells(uv, NUM_CELLS);


	vec3 col = vec3(c*.83, c, min(c*1.3, 1.0));
	
	

	fragColor = vec4(col, 1.0);
}
