
out color result;

in vec2 UV(knot= ioFragCoord);

#sampler TextureSource

#ifdef TextureSource
	result = texture(TextureSource,UV);
#else 
	result = vec4(0, 0, 0, 0);
#endif
         