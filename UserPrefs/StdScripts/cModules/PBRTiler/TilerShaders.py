VERTEX_SHADER = """
#version 330 core

uniform int previewGrid; // 0 = off, 1 = 2x2 grid

out vec2 v_screen_coord;

void main() {
    vec2 pos;
    if (gl_VertexID == 0) pos = vec2(-1.0, -1.0);
    else if (gl_VertexID == 1) pos = vec2(1.0, -1.0);
    else if (gl_VertexID == 2) pos = vec2(-1.0, 1.0);
    else pos = vec2(1.0, 1.0);
    
    gl_Position = vec4(pos, 0.0, 1.0);
    v_screen_coord = (pos + 1.0) / 2.0; 
}
"""

FRAGMENT_SHADER = """
#version 330 core

uniform sampler2D tex_albedo;
uniform sampler2D tex_normal;
uniform sampler2D tex_height;
uniform sampler2D tex_custom[8];
uniform sampler2D tex_pass1;

uniform mat3 inverseHomography;
uniform float rotationAngle;
uniform vec2 cropOffset;
uniform vec2 cropScale;
uniform vec2 tileOffset;
uniform vec2 texelSize;

uniform float heightBlendThreshold;
uniform float heightBlendContrast;
uniform float blendMargin;
uniform float blendHeightInfluence;
uniform int useHeightBlend;

uniform int invertNormalY;
uniform int viewMode;
uniform int previewGrid; // 0 = off, 1 = 2x2 grid
uniform float zoomLevel;
uniform vec2 panOffset;
uniform int eqAlbedoEnabled;
uniform float eqAlbedoLodCenter;
uniform float eqAlbedoLodEdge;
uniform vec3 globalAvgColor;

uniform int isPass2;
uniform float hueShift;
uniform float satMult;
uniform float expShift;
uniform vec3 colorBalance;

in vec2 v_screen_coord;
out vec4 fragColor;

vec3 rgb2hsv(vec3 c) {
    vec4 K = vec4(0.0, -1.0 / 3.0, 2.0 / 3.0, -1.0);
    vec4 p = mix(vec4(c.bg, K.wz), vec4(c.gb, K.xy), step(c.b, c.g));
    vec4 q = mix(vec4(p.xyw, c.r), vec4(c.r, p.yzx), step(p.x, c.r));
    float d = q.x - min(q.w, q.y);
    float e = 1.0e-10;
    return vec3(abs(q.z + (q.w - q.y) / (6.0 * d + e)), d / (q.x + e), q.x);
}

vec3 hsv2rgb(vec3 c) {
    vec4 K = vec4(1.0, 2.0 / 3.0, 1.0 / 3.0, 3.0);
    vec3 p = abs(fract(c.xxx + K.xyz) * 6.0 - K.www);
    return c.z * mix(K.xxx, clamp(p - K.xxx, 0.0, 1.0), c.y);
}

void getSample(vec2 screenCoord, out vec4 albedo, out vec3 normal, out float height, out float mask) {
    vec3 proj = inverseHomography * vec3(screenCoord, 1.0);
    vec2 homography_uv = proj.xy / proj.z;
    
    vec2 cropped_uv = homography_uv * cropScale + cropOffset;
    
    float cosA = cos(rotationAngle);
    float sinA = sin(rotationAngle);
    mat2 rotMat = mat2(cosA, -sinA, sinA, cosA);
    vec2 rotated_uv = rotMat * (cropped_uv - 0.5) + 0.5;
    
    vec2 final_uv = fract(rotated_uv + tileOffset);
    vec2 safe_uv = clamp(final_uv, texelSize * 2.0, 1.0 - texelSize * 2.0);
    
    vec2 dx = dFdx(rotated_uv);
    vec2 dy = dFdy(rotated_uv);
    
    vec4 realAlbedo = textureGrad(tex_albedo, safe_uv, dx, dy);
    
    if (viewMode >= 3) {
        int customIdx = viewMode - 3;
        if (customIdx == 0) albedo = textureGrad(tex_custom[0], safe_uv, dx, dy);
        else if (customIdx == 1) albedo = textureGrad(tex_custom[1], safe_uv, dx, dy);
        else if (customIdx == 2) albedo = textureGrad(tex_custom[2], safe_uv, dx, dy);
        else if (customIdx == 3) albedo = textureGrad(tex_custom[3], safe_uv, dx, dy);
        else if (customIdx == 4) albedo = textureGrad(tex_custom[4], safe_uv, dx, dy);
        else if (customIdx == 5) albedo = textureGrad(tex_custom[5], safe_uv, dx, dy);
        else if (customIdx == 6) albedo = textureGrad(tex_custom[6], safe_uv, dx, dy);
        else if (customIdx == 7) albedo = textureGrad(tex_custom[7], safe_uv, dx, dy);
        else albedo = vec4(0.0);
    } else {
        albedo = realAlbedo;
    }
    
    vec4 normalData = textureGrad(tex_normal, safe_uv, dx, dy);
    height = textureGrad(tex_height, safe_uv, dx, dy).r;
    
    vec3 normalVec = normalData.rgb * 2.0 - 1.0;
    if (invertNormalY == 1) normalVec.y = -normalVec.y;
    
    float normAngle = rotationAngle + 1.5707963268;
    float cosN = cos(normAngle);
    float sinN = sin(normAngle);
    float nx = normalVec.x * cosN + normalVec.y * sinN;
    float ny = -normalVec.x * sinN + normalVec.y * cosN;
    normalVec.xy = vec2(nx, ny);
    normalVec = normalize(normalVec);
    normal = normalVec * 0.5 + 0.5;
    
    mask = 1.0;
    
    if (useHeightBlend == 1) {
        vec2 d = abs(homography_uv * 2.0 - 1.0);
        float distToEdge = 1.0 - max(d.x, d.y); 
        float normalizedBlend = clamp(distToEdge / blendMargin, 0.0, 1.0);
        float w = mix(normalizedBlend, height, blendHeightInfluence);
        
        float maskThresh = max(0.0, w - heightBlendThreshold);
        float hAlpha = smoothstep(0.0, heightBlendContrast, maskThresh);
        mask = min(mask, hAlpha);
    }
}

void main() {
    if (isPass2 == 1) {
        vec2 c = v_screen_coord;
        c = (c - 0.5) / zoomLevel + 0.5 - panOffset;
        
        vec2 sample_c = c;
        if (previewGrid == 1) sample_c *= 2.0;
        
        vec4 albedo = texture(tex_pass1, sample_c);
        
        if (eqAlbedoEnabled == 1 && (viewMode == 0 || viewMode >= 3)) {
            vec2 tile_c = fract(sample_c);
            vec2 d = abs(tile_c * 2.0 - 1.0);
            float distToEdge = max(d.x, d.y);
            float lodCenter = log2(max(1.0, eqAlbedoLodCenter));
            float lodEdge = log2(max(1.0, eqAlbedoLodEdge));
            float currentLod = mix(lodCenter, lodEdge, smoothstep(0.0, 1.0, distToEdge));
            
            vec3 blurred = textureLod(tex_pass1, sample_c, currentLod).rgb;
            vec3 eq = albedo.rgb / max(blurred, vec3(0.001));
            albedo.rgb = clamp(eq * globalAvgColor, 0.0, 1.0);
        }
        
        if (viewMode == 0 || viewMode >= 3) {
            vec3 hsv = rgb2hsv(albedo.rgb);
            hsv.x = fract(hsv.x + hueShift / 360.0);
            if (hsv.x < 0.0) hsv.x += 1.0;
            hsv.y = clamp(hsv.y * satMult, 0.0, 1.0);
            albedo.rgb = hsv2rgb(hsv);
            albedo.rgb *= colorBalance;
            albedo.rgb = clamp(albedo.rgb * pow(2.0, expShift), 0.0, 1.0);
        }
        
        fragColor = albedo;
        return;
    }

    vec2 c = v_screen_coord;
    float marginX = max(blendMargin, 0.001);
    float marginY = max(blendMargin, 0.001);
    
    // Stretch base texture to fit 1.0 - margin so the cut edge perfectly overlaps
    vec2 uv_base = c * vec2(1.0 - marginX, 1.0 - marginY);
    
    // The cut piece is pasted on the left side (0 to margin)
    // Left edge of cut piece (1.0 - margin) aligns with left edge of screen (c.x = 0)
    vec2 uv_blendX = vec2(c.x * (1.0 - marginX) + 1.0 - marginX, uv_base.y);
    vec2 uv_blendY = vec2(uv_base.x, c.y * (1.0 - marginY) + 1.0 - marginY);
    vec2 uv_blendXY = vec2(uv_blendX.x, uv_blendY.y);
    
    vec4 a1; vec3 n1; float h1; float m1;
    getSample(uv_base, a1, n1, h1, m1);
    
    vec4 ax; vec3 nx; float hx; float mx;
    getSample(uv_blendX, ax, nx, hx, mx);
    
    vec4 ay; vec3 ny; float hy; float my;
    getSample(uv_blendY, ay, ny, hy, my);
    
    vec4 axy; vec3 nxy; float hxy; float mxy;
    getSample(uv_blendXY, axy, nxy, hxy, mxy);
    
    // Opaque on left (c=0 -> w=1), transparent on right (c=margin -> w=0)
    float wx = clamp(1.0 - (c.x / marginX), 0.0, 1.0);
    float wy = clamp(1.0 - (c.y / marginY), 0.0, 1.0);
    
    float mx_mask1 = wx;
    if (useHeightBlend == 1) {
        float windowX = 1.0 - pow(abs(wx * 2.0 - 1.0), 2.0);
        float hDiffX = (hx - h1) * blendHeightInfluence * windowX;
        float w_rawX = wx + hDiffX;
        mx_mask1 = clamp((w_rawX - 0.5) / max(0.001, heightBlendContrast) + 0.5, 0.0, 1.0);
    } else {
        mx_mask1 = clamp((wx - 0.5) / max(0.001, heightBlendContrast) + 0.5, 0.0, 1.0);
    }
    vec4 mixAlbedoX1 = mix(a1, ax, mx_mask1);
    vec3 mixNormalX1 = normalize(mix(n1 * 2.0 - 1.0, nx * 2.0 - 1.0, mx_mask1)) * 0.5 + 0.5;
    float mixHeightX1 = mix(h1, hx, mx_mask1);
    
    float mx_mask2 = wx;
    if (useHeightBlend == 1) {
        float windowX = 1.0 - pow(abs(wx * 2.0 - 1.0), 2.0);
        float hDiffX = (hxy - hy) * blendHeightInfluence * windowX;
        float w_rawX = wx + hDiffX;
        mx_mask2 = clamp((w_rawX - 0.5) / max(0.001, heightBlendContrast) + 0.5, 0.0, 1.0);
    } else {
        mx_mask2 = clamp((wx - 0.5) / max(0.001, heightBlendContrast) + 0.5, 0.0, 1.0);
    }
    vec4 mixAlbedoX2 = mix(ay, axy, mx_mask2);
    vec3 mixNormalX2 = normalize(mix(ny * 2.0 - 1.0, nxy * 2.0 - 1.0, mx_mask2)) * 0.5 + 0.5;
    float mixHeightX2 = mix(hy, hxy, mx_mask2);
    
    float my_mask = wy;
    if (useHeightBlend == 1) {
        float windowY = 1.0 - pow(abs(wy * 2.0 - 1.0), 2.0);
        float hDiffY = (mixHeightX2 - mixHeightX1) * blendHeightInfluence * windowY;
        float w_rawY = wy + hDiffY;
        my_mask = clamp((w_rawY - 0.5) / max(0.001, heightBlendContrast) + 0.5, 0.0, 1.0);
    } else {
        my_mask = clamp((wy - 0.5) / max(0.001, heightBlendContrast) + 0.5, 0.0, 1.0);
    }
    
    vec4 fAlbedo = mix(mixAlbedoX1, mixAlbedoX2, my_mask);
    vec3 fNormal = normalize(mix(mixNormalX1 * 2.0 - 1.0, mixNormalX2 * 2.0 - 1.0, my_mask)) * 0.5 + 0.5;
    float fHeight = mix(mixHeightX1, mixHeightX2, my_mask);
    
    if (viewMode == 0 || viewMode >= 3) fragColor = fAlbedo;
    else if (viewMode == 1) fragColor = vec4(fNormal, 1.0);
    else if (viewMode == 2) fragColor = vec4(vec3(fHeight), 1.0);
}
"""
