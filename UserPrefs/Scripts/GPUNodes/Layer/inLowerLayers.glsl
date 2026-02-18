
out Material result;


out float metalness;
out float gloss;
out float displacement;
out float Opacity;
out color AlbedoColor;

result = ioBackgroundMTL;

metalness = result.ioMetalness;   

Opacity = result.ioOpacity;

gloss = result.ioGloss;   

AlbedoColor.xyz = result.ioAlbedoColor;
AlbedoColor.w = result.ioOpacity;

displacement = result.ioDisplacement;  