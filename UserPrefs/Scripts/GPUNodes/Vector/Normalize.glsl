#enum genType float vec2 vec3 vec4 color

in genType Value;

out genType Result;
  
Result = normalize(Value);  