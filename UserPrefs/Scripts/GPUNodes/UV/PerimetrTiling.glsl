in vec2 UVCoord;
in vec2 Tiling;
in vec2 Padding(value = 0.0, min = 0.0, max = 0.5);


out vec2 TiledUV;
out float PerimetrMask;	
out vec2 TileIdx;	
	PerimetrMask = 1.0;
	UVCoord *= 1.0+Padding*2.0;
	UVCoord -= Padding;
	UVCoord = clamp(UVCoord, 0.0, 1.0);        
	Tiling = floor(Tiling);
	vec2 tileSize = 1.0/Tiling;
	vec2 scaledUV = UVCoord*Tiling;
	TileIdx = floor(scaledUV);
	TiledUV = scaledUV-TileIdx;
	if (UVCoord.x > tileSize.x && UVCoord.x < 1-tileSize.x && UVCoord.y > tileSize.y && UVCoord.y < 1-tileSize.y)
    {
      PerimetrMask = 0.0;
      TiledUV = vec2(0.0);
    }
 