

in Material Source;
out float Gloss;
out float Metalness; 
out float Opacity;
out color AlbedoColor;
out float Displacement;

ioMTL = Source;


Gloss = Source.ioGloss;
Metalness = Source.ioMetalness;
Opacity = Source.ioOpacity;
AlbedoColor.xyz = Source.ioAlbedoColor;
AlbedoColor.w;
Displacement = Source.ioDisplacement;