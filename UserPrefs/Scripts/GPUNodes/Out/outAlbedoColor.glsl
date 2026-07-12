
#bool AlphaIsOpacity

in color AlbedoColor;
ioAlbedoColor = AlbedoColor.xyz;

#if AlphaIsOpacity
	ioOpacity = AlbedoColor.w;
#else 	
	in float Opacity(value=1, min=0, max=1);
	ioOpacity = Opacity;
#endif