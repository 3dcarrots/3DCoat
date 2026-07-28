//[NAME] GeometryInfo
//[GROUP] In

out color AO;
out color DirectionalOcclusion;
out color Thickness;

AO = ioGeometryInfo.zzzz;
DirectionalOcclusion = ioGeometryInfo.yyyy;
Thickness = ioGeometryInfo.xxxx;
