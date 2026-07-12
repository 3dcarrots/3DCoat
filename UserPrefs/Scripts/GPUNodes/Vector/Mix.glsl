#enum genType color float vec2 vec3 vec4

in genType Value1 = genType(1);
in genType Value2 = genType(1);
in float Mask(min = 0.0, max = 1.0, legacy=Mix);

out genType Result;
  
Result = mix(Value1, Value2, genType(clamp(Mask, 0, 1)));   