#enum genType float vec2 vec3 vec4 color
#enum InputCount 2 3 4 5 6 7 8 9 10

in genType Value1;
in genType Value2;
#if InputCount > 2
in genType Value3;
#endif
#if InputCount > 3
in genType Value4;
#endif
#if InputCount > 4
in genType Value5;
#endif
#if InputCount > 5
in genType Value6;
#endif
#if InputCount > 6
in genType Value7;
#endif
#if InputCount > 7
in genType Value8;
#endif
#if InputCount > 8
in genType Value9;
#endif
#if InputCount > 9
in genType Value10;
#endif

out genType Result;
  
Result = min(Value1, Value2);  

#if InputCount > 2
Result = min(Result, Value3);  
#endif
#if InputCount > 3
Result = min(Result, Value4);  
#endif
#if InputCount > 4
Result = min(Result, Value5);  
#endif
#if InputCount > 5
Result = min(Result, Value6);  
#endif
#if InputCount > 6
Result = min(Result, Value7);  
#endif
#if InputCount > 7
Result = min(Result, Value8);  
#endif
#if InputCount > 8
Result = min(Result, Value9);  
#endif
#if InputCount > 9
Result = min(Result, Value10);  
#endif