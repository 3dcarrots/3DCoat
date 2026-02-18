in color Value;

out color Result;
  
Result.xyz = vec3((Value.x+Value.y+Value.z)*0.33333);
Result.w = Value.w;