
out Material material;
out float metalness;
out float gloss;
out float displacement;
out float Opacity;
out color AlbedoColor;


material = ioMTL;
metalness = ioMetalness;   

Opacity = ioOpacity;

gloss = ioGloss;   

AlbedoColor.xyz = ioAlbedoColor;
AlbedoColor.w = ioOpacity;

displacement = ioDisplacement;  