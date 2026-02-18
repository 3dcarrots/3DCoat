
#enum ConditionType Always MoreOnConcave MoreOnConvex MoreOnFlat MoreOnCurved MoreOnLit MoreInShadow MoreOnTop MoreOnBottom MoreOnSides 

//	in vec3 CavityDistribution;
	in float ConditionMask(min = 0, max = 5, default = 1);
	in float Contrast(min = -10, max = 10, default = 1);

	in float EdgeScattering(min = 0, max = 2, default = 1);
	in float MaskDegree(min = 0, max = 5, default = 1);	

	in float CavityWidth(min = 0, max = 1, default = 1);
	



float cavity = mix(mix(ioCavity.x, ioCavity.y, clamp(CavityWidth*2.0,0.0,1.0)), ioCavity.z, clamp(CavityWidth*2.0-0.5*2,0.0,1.0));
float convex = cavity*2.0-1.0;
float concave = 1.0-cavity*2.0;



out float result;

result = 1;

#ifdef ConditionType_MoreOnTop
	result = clamp(ioNormal.y, 0.0, 1.0);
#endif
#ifdef ConditionType_MoreOnBottom
	result = clamp(-ioNormal.y, 0.0, 1.0);
#endif
#ifdef ConditionType_MoreOnSides
	result = 1.0-abs(ioNormal.y);
#endif
#ifdef ConditionType_MoreOnConcave
	result = concave;
#endif
#ifdef ConditionType_MoreOnConvex
	result = convex;
#endif
#ifdef ConditionType_MoreOnFlat
	result = 1.0-abs(convex);
#endif
#ifdef ConditionType_MoreOnCurved
	result = abs(convex);
#endif

#ifdef ConditionType_MoreOnLit
	result = ioOcclusion.x;
#endif

#ifdef ConditionType_MoreInShadow
	result = 1.0-ioOcclusion.x;
#endif

	result = (result-0.5)*Contrast+0.5-EdgeScattering+MaskDegree;
	result *= ConditionMask;
	result = clamp(result,0.0,1.0);
           