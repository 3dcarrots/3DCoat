
#enum MaskMode Replace Min Max Component  

in float Mask(value = 1, min = 0, max = 1);
Mask = clamp(Mask, 0, 1);
#ifdef MaskMode_Replace
NGMask = vec4(Mask);
#endif
#ifdef MaskMode_Min
NGMask = min(NGMask, vec4(Mask));
#endif
#ifdef MaskMode_Max
NGMask = max(NGMask, vec4(Mask));
#endif
#ifdef MaskMode_Component
ioMTL = mixMTL(ioCompMTL, ioMTL, Mask);
ioCompMTL = ioMTL;
#endif