// NGL Node for Photoshop-like layer blending 
#enum BlendMode Normal Add Subtract Multiply Screen Overlay Darken Lighten ColorDodge ColorBurn HardLight SoftLight Difference Exclusion Max Min 

in color Base(value=vec4(1.0, 1.0, 1.0, 1.0));
in color Blend(value=vec4(1.0, 1.0, 1.0, 1.0));
in float Opacity(value=1.0, min=0.0, max=1.0);
out color Result;

void main() {
    // Clamping to avoid artifacts on overbright colors 
    vec3 b = clamp(Base.rgb, 0.0, 1.0); 
    vec3 a = clamp(Blend.rgb, 0.0, 1.0); 
    
    vec3 blended = a;
    
    #ifdef BlendMode_Normal
        blended = a;
    #endif
    
    #ifdef BlendMode_Add
        blended = b + a;
    #endif
    
    #ifdef BlendMode_Subtract
        blended = max(b - a, vec3(0.0));
    #endif
    
    #ifdef BlendMode_Multiply
        blended = b * a;
    #endif
    
    #ifdef BlendMode_Screen
        blended = 1.0 - (1.0 - b) * (1.0 - a);
    #endif
    
    #ifdef BlendMode_Overlay
        vec3 mult_overlay = 2.0 * b * a; 
        vec3 screen_overlay = 1.0 - 2.0 * (1.0 - b) * (1.0 - a); 
        blended = mix(mult_overlay, screen_overlay, step(0.5, b));
    #endif
    
    #ifdef BlendMode_Darken
        blended = min(b, a);
    #endif
    
    #ifdef BlendMode_Lighten
        blended = max(b, a);
    #endif
    
    #ifdef BlendMode_ColorDodge
        blended = mix(min(vec3(1.0), b / max(1.0 - a, vec3(0.00001))), vec3(1.0), step(1.0, a));
    #endif
    
    #ifdef BlendMode_ColorBurn
        blended = mix(max(vec3(0.0), 1.0 - (1.0 - b) / max(a, vec3(0.00001))), vec3(0.0), step(a, vec3(0.0)));
    #endif
    
    #ifdef BlendMode_HardLight
        vec3 mult_hl = 2.0 * b * a; 
        vec3 screen_hl = 1.0 - 2.0 * (1.0 - b) * (1.0 - a); 
        blended = mix(mult_hl, screen_hl, step(0.5, a));
    #endif
    
    #ifdef BlendMode_SoftLight
        vec3 darken_sl = b - (1.0 - 2.0 * a) * b * (1.0 - b); 
        vec3 lighten_sl = b + (2.0 * a - 1.0) * (sqrt(b) - b); 
        blended = mix(darken_sl, lighten_sl, step(0.5, a));
    #endif
    
    #ifdef BlendMode_Difference
        blended = abs(b - a);
    #endif
    
    #ifdef BlendMode_Exclusion
        blended = b + a - 2.0 * b * a;
    #endif
    
    #ifdef BlendMode_Max
        blended = max(b, a);
    #endif
    
    #ifdef BlendMode_Min
        blended = min(b, a);
    #endif
    
    // Opacity and Alpha factoring 
    float totalBlendFactor = clamp(Blend.a * Opacity, 0.0, 1.0); 
    
    vec3 finalColor = mix(Base.rgb, blended, totalBlendFactor); 
    float finalAlpha = max(Base.a, Blend.a * Opacity); 
    
    Result = vec4(finalColor, finalAlpha);
}
