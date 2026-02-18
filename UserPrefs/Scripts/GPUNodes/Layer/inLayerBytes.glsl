

out vec4 LayerBytes;
out float SpecularMask;
out float Gloss;
out float Metall;


LayerBytes = ioLayerBytes;

SpecularMask = ioLayerBytes.w;

Gloss = ioLayerBytes.z;

Metall = ioLayerBytes.x;
