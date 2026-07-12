in float displacement(min = -2, max = 2, default = 0, expression = R=V*K);
in float offset(min = -2, max = 2, default = 0, expression = R=V*K);

float finalDisp = displacement;

#ifdef IN_displacement
float dispM = 1.0;
if(displacement.INV) dispM *= 1.0-(displacement.K).x; 
else dispM *= (displacement.K).x;

finalDisp = ((displacement.DC(vec4(dispM))-vec4(0.5))*displacement.V).x;
#endif

finalDisp += offset;

ioDisplacement = finalDisp;