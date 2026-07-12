out color result;

#bool OutputLOD0
#if OutputLOD0
in float LOD0_Level(value=0, min=0, max=10);
out color LOD0;
#endif

#bool OutputLOD1
#if OutputLOD1
in float LOD1_Level(value=0, min=0, max=10);
out color LOD1;
#endif

#bool OutputLOD2
#if OutputLOD2
in float LOD2_Level(value=0, min=0, max=10);
out color LOD2;
#endif


in vec2 UV(knot= ioFragCoord);

#sampler TextureSource

#ifdef TextureSource
	result = texture(TextureSource,UV);
    
    #if OutputLOD0
        LOD0 = textureLod(TextureSource, UV, LOD0_Level);
    #endif

    #if OutputLOD1
        LOD1 = textureLod(TextureSource, UV, LOD1_Level);
    #endif

    #if OutputLOD2
        LOD2 = textureLod(TextureSource, UV, LOD2_Level);
    #endif

#else 
	result = vec4(0, 0, 0, 0);
    #if OutputLOD0
        LOD0 = vec4(0, 0, 0, 0);
    #endif
    #if OutputLOD1
        LOD1 = vec4(0, 0, 0, 0);
    #endif
    #if OutputLOD2
        LOD2 = vec4(0, 0, 0, 0);
    #endif
#endif