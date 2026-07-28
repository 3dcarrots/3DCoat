// NGL Color Invert Node
#bool InvertR
#bool InvertG
#bool InvertB
#bool InvertA

in color Color(value=vec4(1.0, 1.0, 1.0, 1.0));
out color Result;

void main() {
    vec4 inverted = vec4(1.0) - Color;
    vec4 finalColor = Color;
    
#if !InvertR && !InvertG && !InvertB && !InvertA
    // Default behavior if no specific channels are selected: invert RGB
    finalColor.rgb = inverted.rgb;
#else
#if InvertR
    finalColor.r = inverted.r;
#endif
#if InvertG
    finalColor.g = inverted.g;
#endif
#if InvertB
    finalColor.b = inverted.b;
#endif
#if InvertA
    finalColor.a = inverted.a;
#endif
#endif

    Result = finalColor;
}
