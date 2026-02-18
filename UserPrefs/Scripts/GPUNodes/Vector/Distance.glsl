#enum genType float vec2 vec3 vec4 color

in genType Value1;
in genType Value2;

out float Result;
  
  	Result = distance(Value1, Value2);   