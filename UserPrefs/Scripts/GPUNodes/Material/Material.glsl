

in float Gloss(min = 0, max = 1);
in float Metalness(min = 0, max = 1);
in color AlbedoColor;

out Material result;

result = _init_Material_;
result.ioAlbedoColor = AlbedoColor;
result.ioGloss = Gloss;
result.ioMetalness = Metalness; 
result.ioOpacity = AlbedoColor.w;    

