#enum ConditionType Always MoreOnConcave MoreOnConvex LessOnConcave LessOnConvex MoreOnFlat MoreOnCurved MoreOnLit MoreInShadow MoreOnTop MoreOnBottom MoreOnSides MoreOnBright MoreOnMidtone MoreOnDark MoreOnPicked MoreOnBumped MoreOnDent
#enum Mapping triplanar UV cilindrical spherical

in float Contrast(min = -1.0, max = 1.0, default = 0.0);
// Corresponds to CavContrast
in float MaskDegree(min = 0.0, max = 10.0, default = 1.0, expression = R=V*K);
// Corresponds to DegreeOfCavity
in float CavityWidth(min = 0.0, max = 1.0, default = 0.5);

// New properties for color and depth modes
in color SurfaceColor(knot = ioBackgroundMTL[0]*2.0);
in color PickedColor(value = vec4(1.0));
in float SurfaceDepth(value = 0.0);

float ioAO = ioOcclusion.x;

out float result;

float CavityScale = 0.5;



float wave01(float v) {
    v = clamp(v, 0.0, 1.0);
    return 0.5 - 0.5 * cos(v * 3.14159265359);
}

float fcontrastAsym0(float x, float c) {
    if (c == 1.0) return x;
    c = clamp(c, 0.03, 1.99);
    float con = c > 1.0 ? 1.1 / (2.1 - c) : c;
    if (x < 0.5) {
        return pow(x * 2.0, con) / 2.0;
    } else {
        return 0.5 + (x - 0.5) * con;
    }
}

float fcontrast3(float x, float c) {
    if (c == 1.0) return x;
    c = clamp(c, 0.03, 1.96);
    float con = c > 1.0 ? 1.0 / (2.0 - c) : c;
    if (x < 0.5) {
        float p = x * 2.0;
        float p2 = p * p;
        float weight = p2 * (3.0 - 2.0 * p);
        return ((1.0 - con) * weight + con * p) / 2.0;
    } else {
        return 0.5 + (x - 0.5) * con;
    }
}

float fcontrastAsym(float x, float c) {
    if (c >= 1.0) return fcontrastAsym0(x, c);
    return fcontrast3(x, c);
}

// --- Main logic ---

int cType = 0;
#ifdef ConditionType_MoreOnConcave
    cType = 1;
#endif
#ifdef ConditionType_MoreOnConvex
    cType = 2;
#endif
#ifdef ConditionType_LessOnConcave
    cType = 3;
#endif
#ifdef ConditionType_LessOnConvex
    cType = 4;
#endif
#ifdef ConditionType_MoreOnFlat
    cType = 5;
#endif
#ifdef ConditionType_MoreOnCurved
    cType = 6;
#endif
#ifdef ConditionType_MoreOnLit
    cType = 7;
#endif
#ifdef ConditionType_MoreInShadow
    cType = 8;
#endif
#ifdef ConditionType_MoreOnTop
    cType = 9;
#endif
#ifdef ConditionType_MoreOnBottom
    cType = 10;
#endif
#ifdef ConditionType_MoreOnSides
    cType = 11;
#endif
#ifdef ConditionType_MoreOnBright
    cType = 12;
#endif
#ifdef ConditionType_MoreOnMidtone
    cType = 13;
#endif
#ifdef ConditionType_MoreOnDark
    cType = 14;
#endif
#ifdef ConditionType_MoreOnPicked
    cType = 15;
#endif
#ifdef ConditionType_MoreOnBumped
    cType = 16;
#endif
#ifdef ConditionType_MoreOnDent
    cType = 17;
#endif



float w = 1.0;
float cv = Contrast + 1.0;
float cv0 = cv;
float cv2 = cv0;

if (cType != 0) {
    bool usecav = cType < 7;
    bool useaod = cType >= 7 && cType < 18;

    // 1. Calculate BASE mask w (using MaskDegree as DegreeOfCavity from C++)
    if (usecav) {
        float ca = CavityScale;
        float cl = CavityWidth;
        cl = 1.0 - cl * cl;
        if (cl < 0.0) ca *= (cl + 1.0);
        else ca = 1.0 - (1.0 - ca) * (1.0 - cl);
        ca = clamp(ca, 0.0, 1.0);
        float x2 = ca * ca;
        vec3 C = vec3(x2, (ca - x2) * 4.0, 1.0 - ca);
        float s = C.x + C.y + C.z * 0.5;
        vec3 CavityDistribution = C / s;
        
        w = dot(vec3(1.0) - ioCavity.xyz * 2.0, CavityDistribution) * MaskDegree * MaskDegree * 5.0;
    } 
    // Masks based on AO, Normals, Colors, and Depth
    else if (cType == 7) { w = ioAO + (MaskDegree - 1.0) / 2.0; }
    else if (cType == 8) { w = (1.0 - ioAO) + (MaskDegree - 1.0) / 2.0; }
    else if (cType == 9) { w = (1.0 + ioNormal.y) / 2.0 + MaskDegree - 1.0; }
    else if (cType == 10) { w = (1.0 - ioNormal.y) / 2.0 + MaskDegree - 1.0; }
    else if (cType == 11) { w = (ioNormal.x * ioNormal.x + ioNormal.z * ioNormal.z) + MaskDegree - 1.0; }
    else if (cType == 12) {
        float lum = dot(SurfaceColor.rgb, vec3(0.11, 0.59, 0.3));
        w = lum * SurfaceColor.a * MaskDegree;
    } else if (cType == 13) {
        float lum = dot(SurfaceColor.rgb, vec3(0.11, 0.59, 0.3));
        w = (1.0 - wave01(abs(lum * 2.0 - 1.0))) * MaskDegree * SurfaceColor.a;
        w = max(w, 0.0);
    } else if (cType == 14) {
        float lum = dot(SurfaceColor.rgb, vec3(0.11, 0.59, 0.3));
        w = (1.0 - lum) * SurfaceColor.a * MaskDegree;
    } else if (cType == 15) {
        w = (1.0 - distance(SurfaceColor.rgb, PickedColor.rgb)) * SurfaceColor.a;
        w = max(w, 0.0);
    } else if (cType == 16) {
        w = max(SurfaceDepth, 0.0);
    } else if (cType == 17) {
        w = max(-SurfaceDepth, 0.0);
    }

    // 2. Apply DegreeMap (corresponds to ConditionTex in C++)


    if (cv2 > 1.0) {
        cv2 = min(cv2, 1.99);
        cv2 = 1.0 / (2.0 - cv2);
    }

    // 3. Apply contrast (CavContrast)
    if (Contrast != 0.0) {
        float w0 = w;
        w = abs(w);
        if (usecav) {
            if (cv < 0.005) cv = 0.005;
            if (cv0 > 1.0) w *= cv0;
            if (w < 0.0001) w = 0.0001;
            w = pow(w, cv);
            w = fcontrastAsym(w, cv0);
        } else if (useaod) {
            w += (cv - cv0) / 3.0;
            w = 0.5 + (w - 0.5) * cv2;
        }

        // Apply wave smoothing (as in C++)
        w = wave01(w);
        if (w0 < 0.0) w *= -1.0;
    }

    // 4. Final inversions depending on cType
    if (cType == 2) { w = -w; } 
    else if (cType == 3) { w = 1.0 - w; } 
    else if (cType == 4) { w = 1.0 + w; } 
    else if (cType == 5) { w = 1.0 - abs(w); } 
    else if (cType == 6) { w = abs(w); }

    w = clamp(w, 0.0, 1.0);
}

result = w;