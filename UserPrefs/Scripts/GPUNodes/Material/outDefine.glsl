
#enum MaterialType ClearCoat Cloth Skin Glass
#int bbb 45 5 70
#bool fff

in color AlbedoColor;
out color ResultColor;


float myFunction(){
	return 0.5;

}

#if fff
	ResultColor = AlbedoColor;
#else
	ResultColor = AlbedoColor*0.5;
//	ResultColor = AlbedoColor*MaterialIO::Define::myFunction()*Define::myFunction();
#endif

/*
Material myMTL;
myMTL.ioAlbedoColor = AlbedoColor;
#if fff
myMTL.ioAlbedoColor *= 0.5;
#endif
ioMTL.ioAlbedoColor = myMTL.ioAlbedoColor;



*/










