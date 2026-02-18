
out color RGBCavity;
out float Mask;

out float convex;
out float concave;


in float Radius(value = 0.0, min = 0, max = 1);
in float Sharpness(value = 2, min = 0, max = 50);
in float Shift(value = 0, min = -1, max = 1);

RGBCavity = ioCavity;

Mask = mix(mix(ioCavity.x, ioCavity.y, clamp(Radius*2.0,0.0,1.0)), ioCavity.z, clamp(Radius*2.0-0.5*2,0.0,1.0));
convex = Mask*2.0-1.0;
concave = 1.0-Mask*2.0;

convex = clamp((convex-0.5+Shift)*Sharpness+0.5, 0.0, 1.0);
concave = clamp((concave-0.5+Shift)*Sharpness+0.5, 0.0, 1.0);

Mask = (Mask-0.5+Shift)*Sharpness+0.5;
