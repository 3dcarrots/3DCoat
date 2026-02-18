// CodeMirror, copyright (c) by Marijn Haverbeke and others
// Distributed under an MIT license: https://codemirror.net/LICENSE

(function(mod) {
  if (typeof exports == "object" && typeof module == "object") // CommonJS
    mod(require("../../lib/codemirror"));
  else if (typeof define == "function" && define.amd) // AMD
    define(["../../lib/codemirror"], mod);
  else // Plain browser env
    mod(CodeMirror);
})(function(CodeMirror) {
  "use strict";

  var WORD = /[\w$]+/, RANGE = 500;

  function AddHintWord(list, curWord, seen, aWord){
    if ((!curWord || aWord.lastIndexOf(curWord, 0) == 0) && !Object.prototype.hasOwnProperty.call(seen, aWord)) {
      seen[aWord] = true;
      list.push(aWord);
    }
  }

  CodeMirror.registerHelper("hint", "anyword", function(editor, options) {
    var word = options && options.word || WORD;
    var range = options && options.range || RANGE;
    var cur = editor.getCursor(), curLine = editor.getLine(cur.line);
    var end = cur.ch, start = end;
    while (start && word.test(curLine.charAt(start - 1))) --start;
    var curWord = start != end && curLine.slice(start, end);

    var list = options && options.list || [], seen = {};
    var re = new RegExp(word.source, "g");
    for (var dir = -1; dir <= 1; dir += 2) {
      var line = cur.line, endLine = Math.min(Math.max(line + dir * range, editor.firstLine()), editor.lastLine()) + dir;
      for (; line != endLine; line += dir) {
        var text = editor.getLine(line), m;
        while (m = re.exec(text)) {
          if (line == cur.line && m[0] === curWord) continue;
          if ((!curWord || m[0].lastIndexOf(curWord, 0) == 0) && !Object.prototype.hasOwnProperty.call(seen, m[0])) {
            seen[m[0]] = true;
            list.push(m[0]);
          }
        }
      }
    }
	AddHintWord(list, curWord, seen, "vec4Zero");
	AddHintWord(list, curWord, seen, "vec4One");
	AddHintWord(list, curWord, seen, "ioResolution");
	AddHintWord(list, curWord, seen, "ioTime");
	AddHintWord(list, curWord, seen, "ioTimeDelta");
	AddHintWord(list, curWord, seen, "ioFrame");
	AddHintWord(list, curWord, seen, "ioMouse");
	AddHintWord(list, curWord, seen, "ioDate");
	AddHintWord(list, curWord, seen, "ioReplaceAlpha");
	AddHintWord(list, curWord, seen, "ioFragCoord");
	AddHintWord(list, curWord, seen, "ioUV");
	AddHintWord(list, curWord, seen, "ioPosition");
	AddHintWord(list, curWord, seen, "ioNormal");
	AddHintWord(list, curWord, seen, "ioFragCoord_DX");
	AddHintWord(list, curWord, seen, "ioUV_DX");
	AddHintWord(list, curWord, seen, "ioPosition_DX");
	AddHintWord(list, curWord, seen, "ioNormal_DX");
	AddHintWord(list, curWord, seen, "ioFragCoord_DY");
	AddHintWord(list, curWord, seen, "ioUV_DY");
	AddHintWord(list, curWord, seen, "ioPosition_DY");
	AddHintWord(list, curWord, seen, "ioNormal_DY");

	AddHintWord(list, curWord, seen, "ioPM");
	AddHintWord(list, curWord, seen, "ioPQ1");
	AddHintWord(list, curWord, seen, "ioPQ2");
	AddHintWord(list, curWord, seen, "ioPQ3");
	AddHintWord(list, curWord, seen, "ioPQ4");
	AddHintWord(list, curWord, seen, "ioPN");

//	AddHintWord(list, curWord, seen, "ioAlbedoColor; \n"
//	AddHintWord(list, curWord, seen, "ioReflectionColor; \n"
//	AddHintWord(list, curWord, seen, "ioTSNormal; \n"
//	AddHintWord(list, curWord, seen, "ioGloss; \n"
//	AddHintWord(list, curWord, seen, "ioSubSurface; \n"
//	AddHintWord(list, curWord, seen, "ioSSSColor; \n"
//	AddHintWord(list, curWord, seen, "ioEmissive; \n"
//	AddHintWord(list, curWord, seen, "ioOpacity; \n"

	AddHintWord(list, curWord, seen, "Material");
	AddHintWord(list, curWord, seen, "One2DCurve");

//////////////////////////////////////////////////////////////////

AddHintWord(list, curWord, seen, "ioAlbedoColor");
AddHintWord(list, curWord, seen, "ioReflectionColor");
AddHintWord(list, curWord, seen, "ioTSNormal");
AddHintWord(list, curWord, seen, "ioEmissive");
AddHintWord(list, curWord, seen, "ioEmissiveColor");
AddHintWord(list, curWord, seen, "ioSubSurfaceColor");
AddHintWord(list, curWord, seen, "ioSpecularEdgeColor");
AddHintWord(list, curWord, seen, "ioMicroprotrusionsColor");
AddHintWord(list, curWord, seen, "ioMetalness");
AddHintWord(list, curWord, seen, "ioGloss");
AddHintWord(list, curWord, seen, "ioRoughness");
AddHintWord(list, curWord, seen, "ioRefraction");
AddHintWord(list, curWord, seen, "ioRefractionMetalness");
AddHintWord(list, curWord, seen, "ioVelvet");
AddHintWord(list, curWord, seen, "ioIridescence");
AddHintWord(list, curWord, seen, "ioAnisotropy");
AddHintWord(list, curWord, seen, "ioIOR");
AddHintWord(list, curWord, seen, "ioClearCoat");
AddHintWord(list, curWord, seen, "ioClearCoatRoughness");
AddHintWord(list, curWord, seen, "ioVolume");
AddHintWord(list, curWord, seen, "ioMicroprotrusionsRoughness");
AddHintWord(list, curWord, seen, "ioRefractionBlur");
AddHintWord(list, curWord, seen, "ioSpecularEdgePower");
AddHintWord(list, curWord, seen, "ioDiffuseSSS");
AddHintWord(list, curWord, seen, "ioSpecularSSS");
AddHintWord(list, curWord, seen, "ioRefractionChromatic");
AddHintWord(list, curWord, seen, "ioClearCoatEdgePower");
AddHintWord(list, curWord, seen, "ioMicroprotrusions");
AddHintWord(list, curWord, seen, "ioOpacity");


//////////////////////////////////////////////////////////////////

	AddHintWord(list, curWord, seen, "ioSpecularMask");
	AddHintWord(list, curWord, seen, "ioCavity");
	AddHintWord(list, curWord, seen, "ioOcclusion");

	AddHintWord(list, curWord, seen, "ioDisplacement");
	AddHintWord(list, curWord, seen, "ioPanorama");
	AddHintWord(list, curWord, seen, "ioCameraPosition");
	AddHintWord(list, curWord, seen, "ioRayDir");
	AddHintWord(list, curWord, seen, "ioLightDir");
	AddHintWord(list, curWord, seen, "ioIteration");	
	
		
	AddHintWord(list, curWord, seen, "float");
	AddHintWord(list, curWord, seen, "double");
	AddHintWord(list, curWord, seen, "int");
	AddHintWord(list, curWord, seen, "void");
	AddHintWord(list, curWord, seen, "bool");
	AddHintWord(list, curWord, seen, "true");
	AddHintWord(list, curWord, seen, "false");

	AddHintWord(list, curWord, seen, "attribute");
	AddHintWord(list, curWord, seen, "const");
	AddHintWord(list, curWord, seen, "uniform");
	AddHintWord(list, curWord, seen, "varying");
	AddHintWord(list, curWord, seen, "buffer");
	AddHintWord(list, curWord, seen, "shared");
	AddHintWord(list, curWord, seen, "coherent");
	AddHintWord(list, curWord, seen, "volatile");
	AddHintWord(list, curWord, seen, "restrict");
	AddHintWord(list, curWord, seen, "readonly");
	AddHintWord(list, curWord, seen, "writeonly");
	AddHintWord(list, curWord, seen, "atomic_uint");
	AddHintWord(list, curWord, seen, "layout");
	AddHintWord(list, curWord, seen, "centroid");
	AddHintWord(list, curWord, seen, "flat");
	AddHintWord(list, curWord, seen, "smooth");
	AddHintWord(list, curWord, seen, "noperspective");
	AddHintWord(list, curWord, seen, "patch");
	AddHintWord(list, curWord, seen, "sample");
	AddHintWord(list, curWord, seen, "subroutine");
	AddHintWord(list, curWord, seen, "in");
	AddHintWord(list, curWord, seen, "out");
	AddHintWord(list, curWord, seen, "inout");
	AddHintWord(list, curWord, seen, "break");
	AddHintWord(list, curWord, seen, "continue");
	AddHintWord(list, curWord, seen, "do");
	AddHintWord(list, curWord, seen, "for");
	AddHintWord(list, curWord, seen, "while");
	AddHintWord(list, curWord, seen, "switch");
	AddHintWord(list, curWord, seen, "case");
	AddHintWord(list, curWord, seen, "default");
	AddHintWord(list, curWord, seen, "if");
	AddHintWord(list, curWord, seen, "else");


	AddHintWord(list, curWord, seen, "invariant");
	AddHintWord(list, curWord, seen, "precise");

	AddHintWord(list, curWord, seen, "discard");
	AddHintWord(list, curWord, seen, "return");


	AddHintWord(list, curWord, seen, "lowp");
	AddHintWord(list, curWord, seen, "mediump");
	AddHintWord(list, curWord, seen, "highp");
	AddHintWord(list, curWord, seen, "precision");

	AddHintWord(list, curWord, seen, "sampler1D");
	AddHintWord(list, curWord, seen, "sampler2D");
	AddHintWord(list, curWord, seen, "sampler3D");
	AddHintWord(list, curWord, seen, "samplerCube");

	AddHintWord(list, curWord, seen, "sampler1DShadow");
	AddHintWord(list, curWord, seen, "sampler2DShadow");
	AddHintWord(list, curWord, seen, "samplerCubeShadow");

	AddHintWord(list, curWord, seen, "sampler1DArray");
	AddHintWord(list, curWord, seen, "sampler2DArray");

	AddHintWord(list, curWord, seen, "sampler1DArrayShadow");
	AddHintWord(list, curWord, seen, "sampler2DArrayShadow");

	AddHintWord(list, curWord, seen, "isampler1D");
	AddHintWord(list, curWord, seen, "isampler2D");
	AddHintWord(list, curWord, seen, "isampler3D");
	AddHintWord(list, curWord, seen, "isamplerCube");

	AddHintWord(list, curWord, seen, "isampler1DArray");
	AddHintWord(list, curWord, seen, "isampler2DArray");

	AddHintWord(list, curWord, seen, "usampler1D");
	AddHintWord(list, curWord, seen, "usampler2D");
	AddHintWord(list, curWord, seen, "usampler3D");
	AddHintWord(list, curWord, seen, "usamplerCube");

	AddHintWord(list, curWord, seen, "usampler1DArray");
	AddHintWord(list, curWord, seen, "usampler2DArray");

	AddHintWord(list, curWord, seen, "sampler2DRect");
	AddHintWord(list, curWord, seen, "sampler2DRectShadow");
	AddHintWord(list, curWord, seen, "isampler2DRect");
	AddHintWord(list, curWord, seen, "usampler2DRect");

	AddHintWord(list, curWord, seen, "samplerBuffer");
	AddHintWord(list, curWord, seen, "isamplerBuffer");
	AddHintWord(list, curWord, seen, "usamplerBuffer");

	AddHintWord(list, curWord, seen, "sampler2DMS");
	AddHintWord(list, curWord, seen, "isampler2DMS");
	AddHintWord(list, curWord, seen, "usampler2DMS");

	AddHintWord(list, curWord, seen, "sampler2DMSArray");
	AddHintWord(list, curWord, seen, "isampler2DMSArray");
	AddHintWord(list, curWord, seen, "usampler2DMSArray");

	AddHintWord(list, curWord, seen, "samplerCubeArray");
	AddHintWord(list, curWord, seen, "samplerCubeArrayShadow");
	AddHintWord(list, curWord, seen, "isamplerCubeArray");
	AddHintWord(list, curWord, seen, "usamplerCubeArray");

	AddHintWord(list, curWord, seen, "image1D");
	AddHintWord(list, curWord, seen, "iimage1D");
	AddHintWord(list, curWord, seen, "uimage1D");

	AddHintWord(list, curWord, seen, "image2D");
	AddHintWord(list, curWord, seen, "iimage2D");
	AddHintWord(list, curWord, seen, "uimage2D");

	AddHintWord(list, curWord, seen, "image3D");
	AddHintWord(list, curWord, seen, "iimage3D");
	AddHintWord(list, curWord, seen, "uimage3D");

	AddHintWord(list, curWord, seen, "image2DRect");
	AddHintWord(list, curWord, seen, "iimage2DRect");
	AddHintWord(list, curWord, seen, "uimage2DRect");

	AddHintWord(list, curWord, seen, "imageCube");
	AddHintWord(list, curWord, seen, "iimageCube");
	AddHintWord(list, curWord, seen, "uimageCube");

	AddHintWord(list, curWord, seen, "imageBuffer");
	AddHintWord(list, curWord, seen, "iimageBuffer");
	AddHintWord(list, curWord, seen, "uimageBuffer");

	AddHintWord(list, curWord, seen, "image1DArray");
	AddHintWord(list, curWord, seen, "iimage1DArray");
	AddHintWord(list, curWord, seen, "uimage1DArray");

	AddHintWord(list, curWord, seen, "image2DArray");
	AddHintWord(list, curWord, seen, "iimage2DArray");
	AddHintWord(list, curWord, seen, "uimage2DArray");

	AddHintWord(list, curWord, seen, "imageCubeArray");
	AddHintWord(list, curWord, seen, "iimageCubeArray");
	AddHintWord(list, curWord, seen, "uimageCubeArray");

	AddHintWord(list, curWord, seen, "image2DMS");
	AddHintWord(list, curWord, seen, "iimage2DMS");
	AddHintWord(list, curWord, seen, "uimage2DMS");

	AddHintWord(list, curWord, seen, "image2DMSArray");
	AddHintWord(list, curWord, seen, "iimage2DMSArray");
	AddHintWord(list, curWord, seen, "uimage2DMSArray");

	//AddHintWord(list, curWord, seen, "mat");
	AddHintWord(list, curWord, seen, "mat2");
	AddHintWord(list, curWord, seen, "mat3");
	AddHintWord(list, curWord, seen, "mat4");
	AddHintWord(list, curWord, seen, "dmat2");
	AddHintWord(list, curWord, seen, "dmat3");
	AddHintWord(list, curWord, seen, "dmat4");

	AddHintWord(list, curWord, seen, "mat2x2");
	AddHintWord(list, curWord, seen, "mat2x3");
	AddHintWord(list, curWord, seen, "mat2x4");
	AddHintWord(list, curWord, seen, "dmat2x2");
	AddHintWord(list, curWord, seen, "dmat2x3");
	AddHintWord(list, curWord, seen, "dmat2x4");

	AddHintWord(list, curWord, seen, "mat3x2");
	AddHintWord(list, curWord, seen, "mat3x3");
	AddHintWord(list, curWord, seen, "mat3x4");
	AddHintWord(list, curWord, seen, "dmat3x2");
	AddHintWord(list, curWord, seen, "dmat3x3");
	AddHintWord(list, curWord, seen, "dmat3x4");

	AddHintWord(list, curWord, seen, "mat4x2");
	AddHintWord(list, curWord, seen, "mat4x3");
	AddHintWord(list, curWord, seen, "mat4x4");
	AddHintWord(list, curWord, seen, "dmat4x2");
	AddHintWord(list, curWord, seen, "dmat4x3");
	AddHintWord(list, curWord, seen, "dmat4x4");

	AddHintWord(list, curWord, seen, "vec2");
	AddHintWord(list, curWord, seen, "vec3");
	AddHintWord(list, curWord, seen, "vec4");
	AddHintWord(list, curWord, seen, "ivec2");
	AddHintWord(list, curWord, seen, "ivec3");
	AddHintWord(list, curWord, seen, "ivec4");
	AddHintWord(list, curWord, seen, "bvec2");
	AddHintWord(list, curWord, seen, "bvec3");
	AddHintWord(list, curWord, seen, "bvec4");
	AddHintWord(list, curWord, seen, "dvec2");
	AddHintWord(list, curWord, seen, "dvec3");
	AddHintWord(list, curWord, seen, "dvec4");

	AddHintWord(list, curWord, seen, "uint");
	AddHintWord(list, curWord, seen, "uvec2");
	AddHintWord(list, curWord, seen, "uvec3");
	AddHintWord(list, curWord, seen, "uvec4");

	AddHintWord(list, curWord, seen, "hvec2");
	AddHintWord(list, curWord, seen, "hvec3");
	AddHintWord(list, curWord, seen, "hvec4");
	AddHintWord(list, curWord, seen, "fvec2");
	AddHintWord(list, curWord, seen, "fvec3");
	AddHintWord(list, curWord, seen, "fvec4");

	AddHintWord(list, curWord, seen, "sampler3DRect");

	AddHintWord(list, curWord, seen, "filter");

	AddHintWord(list, curWord, seen, "sizeof");
	AddHintWord(list, curWord, seen, "cast");

	AddHintWord(list, curWord, seen, "namespace");
	AddHintWord(list, curWord, seen, "using");


	AddHintWord(list, curWord, seen, "struct");

	AddHintWord(list, curWord, seen, "common");
	AddHintWord(list, curWord, seen, "partition");
	AddHintWord(list, curWord, seen, "active");

	AddHintWord(list, curWord, seen, "asm");

	AddHintWord(list, curWord, seen, "class");
	AddHintWord(list, curWord, seen, "union");
	AddHintWord(list, curWord, seen, "enum");
	AddHintWord(list, curWord, seen, "typedef");
	AddHintWord(list, curWord, seen, "template");
	AddHintWord(list, curWord, seen, "this");

	AddHintWord(list, curWord, seen, "resource");

	AddHintWord(list, curWord, seen, "goto");

	AddHintWord(list, curWord, seen, "inline");
	AddHintWord(list, curWord, seen, "noinline");
	AddHintWord(list, curWord, seen, "public");
	AddHintWord(list, curWord, seen, "static");
	AddHintWord(list, curWord, seen, "extern");
	AddHintWord(list, curWord, seen, "external");
	AddHintWord(list, curWord, seen, "interface");

	AddHintWord(list, curWord, seen, "long");
	AddHintWord(list, curWord, seen, "short");
	AddHintWord(list, curWord, seen, "half");
	AddHintWord(list, curWord, seen, "fixed");
	AddHintWord(list, curWord, seen, "unsigned");
	AddHintWord(list, curWord, seen, "superp");

	AddHintWord(list, curWord, seen, "input");
	AddHintWord(list, curWord, seen, "output");	
	
	//////////////////////////////////
	//// GLSL ////////////////////////
AddHintWord(list, curWord, seen, "acos");
AddHintWord(list, curWord, seen, "acosh");
AddHintWord(list, curWord, seen, "asin");
AddHintWord(list, curWord, seen, "asinh");
AddHintWord(list, curWord, seen, "atan");
AddHintWord(list, curWord, seen, "atanh");
AddHintWord(list, curWord, seen, "cos");
AddHintWord(list, curWord, seen, "cosh");
AddHintWord(list, curWord, seen, "degrees");
AddHintWord(list, curWord, seen, "radians");
AddHintWord(list, curWord, seen, "sin");
AddHintWord(list, curWord, seen, "sinh");
AddHintWord(list, curWord, seen, "tan");
AddHintWord(list, curWord, seen, "tanh");


AddHintWord(list, curWord, seen, "abs");
AddHintWord(list, curWord, seen, "ceil");
AddHintWord(list, curWord, seen, "clamp");
AddHintWord(list, curWord, seen, "dFdx");
AddHintWord(list, curWord, seen, "dFdy");
AddHintWord(list, curWord, seen, "exp");
AddHintWord(list, curWord, seen, "exp2");
AddHintWord(list, curWord, seen, "floor");
AddHintWord(list, curWord, seen, "floor");
AddHintWord(list, curWord, seen, "fma");
AddHintWord(list, curWord, seen, "fract");
AddHintWord(list, curWord, seen, "fwidth");
AddHintWord(list, curWord, seen, "inversesqrt");
AddHintWord(list, curWord, seen, "isinf");
AddHintWord(list, curWord, seen, "isnan");
AddHintWord(list, curWord, seen, "log");
AddHintWord(list, curWord, seen, "log2");
AddHintWord(list, curWord, seen, "max");
AddHintWord(list, curWord, seen, "min");
AddHintWord(list, curWord, seen, "mix");
AddHintWord(list, curWord, seen, "mod");
AddHintWord(list, curWord, seen, "modf");
AddHintWord(list, curWord, seen, "noise");
AddHintWord(list, curWord, seen, "pow");
AddHintWord(list, curWord, seen, "round");
AddHintWord(list, curWord, seen, "roundEven");
AddHintWord(list, curWord, seen, "sign");
AddHintWord(list, curWord, seen, "smoothstep");
AddHintWord(list, curWord, seen, "sqrt");
AddHintWord(list, curWord, seen, "step");
AddHintWord(list, curWord, seen, "trunc");


AddHintWord(list, curWord, seen, "floatBitsToInt");
AddHintWord(list, curWord, seen, "frexp");
AddHintWord(list, curWord, seen, "intBitsToFloat");
AddHintWord(list, curWord, seen, "ldexp");
AddHintWord(list, curWord, seen, "packDouble2x32");
AddHintWord(list, curWord, seen, "packHalf2x16");
AddHintWord(list, curWord, seen, "packUnorm");
AddHintWord(list, curWord, seen, "unpackDouble2x32");
AddHintWord(list, curWord, seen, "unpackHalf2x16");
AddHintWord(list, curWord, seen, "unpackUnorm");

AddHintWord(list, curWord, seen, "gl_ClipDistance");
AddHintWord(list, curWord, seen, "gl_CullDistance");
AddHintWord(list, curWord, seen, "gl_FragCoord");
AddHintWord(list, curWord, seen, "gl_FragDepth");
AddHintWord(list, curWord, seen, "gl_FrontFacing");
AddHintWord(list, curWord, seen, "gl_GlobalInvocationID");
AddHintWord(list, curWord, seen, "gl_HelperInvocation");
AddHintWord(list, curWord, seen, "gl_InstanceID");
AddHintWord(list, curWord, seen, "gl_InvocationID");
AddHintWord(list, curWord, seen, "gl_Layer");
AddHintWord(list, curWord, seen, "gl_LocalInvocationID");
AddHintWord(list, curWord, seen, "gl_LocalInvocationIndex");
AddHintWord(list, curWord, seen, "gl_NumSamples");
AddHintWord(list, curWord, seen, "gl_NumWorkGroups");
AddHintWord(list, curWord, seen, "gl_PatchVerticesIn");
AddHintWord(list, curWord, seen, "gl_PointCoord");
AddHintWord(list, curWord, seen, "gl_PointSize");
AddHintWord(list, curWord, seen, "gl_Position");
AddHintWord(list, curWord, seen, "gl_PrimitiveID");
AddHintWord(list, curWord, seen, "gl_PrimitiveIDIn");
AddHintWord(list, curWord, seen, "gl_SampleID");
AddHintWord(list, curWord, seen, "gl_SampleMask");
AddHintWord(list, curWord, seen, "gl_SampleMaskIn");
AddHintWord(list, curWord, seen, "gl_SamplePosition");
AddHintWord(list, curWord, seen, "gl_TessCoord");
AddHintWord(list, curWord, seen, "gl_TessLevelInner");
AddHintWord(list, curWord, seen, "gl_TessLevelOuter");
AddHintWord(list, curWord, seen, "gl_VertexID");
AddHintWord(list, curWord, seen, "gl_ViewportIndex");
AddHintWord(list, curWord, seen, "gl_WorkGroupID");
AddHintWord(list, curWord, seen, "gl_WorkGroupSize");

AddHintWord(list, curWord, seen, "cross");
AddHintWord(list, curWord, seen, "distance");
AddHintWord(list, curWord, seen, "dot");
AddHintWord(list, curWord, seen, "equal");
AddHintWord(list, curWord, seen, "faceforward");
AddHintWord(list, curWord, seen, "length");
AddHintWord(list, curWord, seen, "normalize");
AddHintWord(list, curWord, seen, "notEqual");
AddHintWord(list, curWord, seen, "reflect");
AddHintWord(list, curWord, seen, "refract");

AddHintWord(list, curWord, seen, "all");
AddHintWord(list, curWord, seen, "any");
AddHintWord(list, curWord, seen, "greaterThan");
AddHintWord(list, curWord, seen, "greaterThanEqual");
AddHintWord(list, curWord, seen, "lessThan");
AddHintWord(list, curWord, seen, "lessThanEqual");
AddHintWord(list, curWord, seen, "not");

AddHintWord(list, curWord, seen, "interpolateAtCentroid");
AddHintWord(list, curWord, seen, "interpolateAtOffset");
AddHintWord(list, curWord, seen, "interpolateAtSample");
AddHintWord(list, curWord, seen, "texelFetch");
AddHintWord(list, curWord, seen, "texelFetchOffset");
AddHintWord(list, curWord, seen, "texture");
AddHintWord(list, curWord, seen, "textureGather");
AddHintWord(list, curWord, seen, "textureGatherOffset");
AddHintWord(list, curWord, seen, "textureGatherOffsets");
AddHintWord(list, curWord, seen, "textureGrad");
AddHintWord(list, curWord, seen, "textureGradOffset");
AddHintWord(list, curWord, seen, "textureLod");
AddHintWord(list, curWord, seen, "textureLodOffset");
AddHintWord(list, curWord, seen, "textureOffset");
AddHintWord(list, curWord, seen, "textureProj");
AddHintWord(list, curWord, seen, "textureProjGrad");
AddHintWord(list, curWord, seen, "textureProjGradOffset");
AddHintWord(list, curWord, seen, "textureProjLod");
AddHintWord(list, curWord, seen, "textureProjLodOffset");
AddHintWord(list, curWord, seen, "textureProjOffset");
AddHintWord(list, curWord, seen, "textureQueryLevels");
AddHintWord(list, curWord, seen, "textureQueryLod");
AddHintWord(list, curWord, seen, "textureSamples");
AddHintWord(list, curWord, seen, "textureSize");

AddHintWord(list, curWord, seen, "determinant");
AddHintWord(list, curWord, seen, "groupMemoryBarrier");
AddHintWord(list, curWord, seen, "inverse");
AddHintWord(list, curWord, seen, "matrixCompMult");
AddHintWord(list, curWord, seen, "outerProduct");
AddHintWord(list, curWord, seen, "transpose");


AddHintWord(list, curWord, seen, "bitCount");
AddHintWord(list, curWord, seen, "bitfieldExtract");
AddHintWord(list, curWord, seen, "bitfieldInsert");
AddHintWord(list, curWord, seen, "bitfieldReverse");
AddHintWord(list, curWord, seen, "findLSB");
AddHintWord(list, curWord, seen, "findMSB");
AddHintWord(list, curWord, seen, "uaddCarry");
AddHintWord(list, curWord, seen, "umulExtended");
AddHintWord(list, curWord, seen, "usubBorrow");


AddHintWord(list, curWord, seen, "imageAtomicAdd");
AddHintWord(list, curWord, seen, "imageAtomicAnd");
AddHintWord(list, curWord, seen, "imageAtomicCompSwap");
AddHintWord(list, curWord, seen, "imageAtomicExchange");
AddHintWord(list, curWord, seen, "imageAtomicMax");
AddHintWord(list, curWord, seen, "imageAtomicMin");
AddHintWord(list, curWord, seen, "imageAtomicOr");
AddHintWord(list, curWord, seen, "imageAtomicXor");
AddHintWord(list, curWord, seen, "imageLoad");
AddHintWord(list, curWord, seen, "imageSamples");
AddHintWord(list, curWord, seen, "imageSize");
AddHintWord(list, curWord, seen, "imageStore");


AddHintWord(list, curWord, seen, "atomicAdd");
AddHintWord(list, curWord, seen, "atomicAnd");
AddHintWord(list, curWord, seen, "atomicCompSwap");
AddHintWord(list, curWord, seen, "atomicCounter");
AddHintWord(list, curWord, seen, "atomicCounterDecrement");
AddHintWord(list, curWord, seen, "atomicCounterIncrement");
AddHintWord(list, curWord, seen, "atomicExchange");
AddHintWord(list, curWord, seen, "atomicMax");
AddHintWord(list, curWord, seen, "atomicMin");
AddHintWord(list, curWord, seen, "atomicOr");
AddHintWord(list, curWord, seen, "atomicXor");

AddHintWord(list, curWord, seen, "barrier");
AddHintWord(list, curWord, seen, "groupMemoryBarrier");
AddHintWord(list, curWord, seen, "memoryBarrier");
AddHintWord(list, curWord, seen, "memoryBarrierAtomicCounter");
AddHintWord(list, curWord, seen, "memoryBarrierBuffer");
AddHintWord(list, curWord, seen, "memoryBarrierImage");
AddHintWord(list, curWord, seen, "memoryBarrierShared");
	
    return {list: list, from: CodeMirror.Pos(cur.line, start), to: CodeMirror.Pos(cur.line, end)};
  });
});
