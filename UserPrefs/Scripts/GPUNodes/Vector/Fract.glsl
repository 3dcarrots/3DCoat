#enum genType float vec2 vec3 vec4 color

in genType Source(AllowCurve = true);      
out genType FractID; 
out genType Result;

	FractID = floor(Source);
	Result = Source - FractID;   