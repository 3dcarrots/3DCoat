in vec2 fragCoord;
in float StripeWidth(value = 0.1, min = 0.0, max = 1.0);
in float StripeSharpness(value = 10.0, min = 0.0, max = 100.0);

out float DistanceToCenter;
out float SectionIdx;
out vec4 StripeColorID;
out float StripeMask;
out vec4 Stripe;

vec2 RAND(vec2 tileIndex, float fracRandomiser)//function for creation simple noise
{
  return fract(tan(dot(tileIndex+ vec2(1245,2566) ,tileIndex+vec2(7856,2156)+ fracRandomiser) / (tileIndex.y+4523)*(tileIndex+ vec2(2123, 5428))));// somthing random for noise 
}
	
	SectionIdx = floor(fragCoord.x);
	DistanceToCenter = 3.0;
	for (float i = -1.0; i < 1.1; i += 1.0){
      
      	
		vec2 SectionHash = RAND(vec2(SectionIdx + i, 1.0), 23.4556);
      	float d = abs(fragCoord.x -  SectionIdx - SectionHash.x - i );
      if (d < DistanceToCenter) 
      {
        DistanceToCenter = d;
        StripeColorID = vec4(RAND(SectionHash, 23.4556), RAND(SectionHash, 89.2586));
           
      }
    }
			
	StripeMask = 1 - clamp((DistanceToCenter -  StripeWidth) * StripeSharpness, 0, 1);
	Stripe = StripeMask * StripeColorID;
	Stripe.w = StripeMask;

 			  