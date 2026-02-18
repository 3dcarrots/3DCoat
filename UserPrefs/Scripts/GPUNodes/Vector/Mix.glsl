#enum genType float vec2 vec3 vec4 color

in genType Value1;
in genType Value2;
in float Mask(min = 0.0, max = 1.0, legacy=Mix);

out genType Result;
  
Result = mix(Value1, Value2, genType(Mask));   