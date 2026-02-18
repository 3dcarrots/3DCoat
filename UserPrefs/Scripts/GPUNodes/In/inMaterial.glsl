
out float metalness;
out float gloss;
out float displacement;
out float Opacity;
out color AlbedoColor;

metalness = ioMetalness;   

Opacity = ioOpacity;

gloss = ioGloss;   

AlbedoColor.xyz = ioAlbedoColor;
AlbedoColor.w = ioOpacity;

displacement = ioDisplacement;  