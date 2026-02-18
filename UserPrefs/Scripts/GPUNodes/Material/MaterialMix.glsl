

in Material Source1;
in float Mask(legacy=Mix);
in Material Source2;
out Material result;


result[0] = mix(Source1[0], Source2[0], vec4(Mask));
result[1] = mix(Source1[1], Source2[1], vec4(Mask));
result[2] = mix(Source1[2], Source2[2], vec4(Mask));
result[3] = mix(Source1[3], Source2[3], vec4(Mask));
result[4] = mix(Source1[4], Source2[4], vec4(Mask));
result[5] = mix(Source1[5], Source2[5], vec4(Mask));
result[6] = mix(Source1[6], Source2[6], vec4(Mask));

