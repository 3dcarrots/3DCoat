
#enum colorProp ioAlbedoColor ioReflectionColor ioSheenColor ioEmissive ioSubSurfaceColor ioMicroprotrusionsColor ioFWSNormal

in Material Source;

out vec3 OutColor;
OutColor = ( Source . colorProp ).xyz;

