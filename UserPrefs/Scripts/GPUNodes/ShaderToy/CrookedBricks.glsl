// MIT License - Kasper Arnklit Frandsen 2022

#enum Projection UV Top Left Front
#define UV ioUV.xyxy
#define Top ioFragCoord.xzxz
#define Left ioFragCoord.zyzy
#define Front ioFragCoord.xyxy


vec2 perpendicular(vec2 vector) {
	vector = vector.yx;
	vector.y = -vector.y;
	return vector;
}

float rand(vec2 x) {
	return fract(cos(mod(dot(x, vec2(13.989, 8.141)), 3.14)) * 43758.5453);
}

// https://wiki.secondlife.com/wiki/Geometric#Line_and_Line.2C_intersection_point
// Copyright 2001, softSurfer (www.softsurfer.com); 2008, LSL-port by Nexii Malthus
// (CC BY-SA 3.0 License)
vec2 get_line_intersection( vec2 A, vec2 B, vec2 C, vec2 D ) {
    vec2 b = B - A;
	vec2 d = D - C;
    float dotperp = b.x * d.y - b.y * d.x;
	// if I had to worry about parallel lines, but I shouldn't have to here
    // if (dotperp == 0) return <-1,-1,-1>;
	vec2 c = C - A;
    float t = (c.x * d.y - c.y * d.x) / dotperp;
	return vec2(A.x + t * b.x, A.y + t * b.y);
}

void mainImage( out vec4 fragColor, in vec2 fragCoord(knot = Projection) )
{
    vec2 scale = vec2(6.0, 6.0);
    float randomness = sin(iTime);
    
    vec2 uv = fragCoord;
    uv += iTime * .1;

    vec2 scaled_uv = uv * scale;
	
	float x_offset = 0.5*step(0.5, fract(uv.y*scale.y*0.5));
		
	vec2 cell_id = floor(scaled_uv);
	vec2 cell_uv = fract(scaled_uv);
	
	cell_id -= vec2(x_offset, 0.0);
	
	float min_distance = 1.0;
	vec2 c_point;
	vec2 left_top;
	vec2 right_top;
	vec2 right_bottom;
	vec2 left_bottom;
	
	for (int i = -1; i <= 1; i++) {
		// neighbor in uv space
		vec2 neighbor = vec2(float(i), 0.0);
		vec2 point = cell_id + neighbor + vec2(0.5) + (vec2(0.0, rand(mod(cell_id + neighbor, scale)) - 0.5) * randomness);
		point /= scale;
		float dist = distance(point, uv);
		
		// get left, right neighbor in here as well, to calculate perpendicular and intersect
		vec2 left = cell_id + neighbor + vec2(-1.0, 0.0) + vec2(0.5) + (vec2(0.0, rand(mod(cell_id + neighbor + vec2(-1.0, 0.0), scale)) - 0.5) * randomness);
		left /= scale;
		vec2 right = cell_id + neighbor + vec2(1.0, 0.0) + vec2(0.5) + (vec2(0.0, rand(mod(cell_id + neighbor + vec2(1.0, 0.0), scale)) - 0.5) * randomness);
		right /= scale;
		

		// Find the midpoint between current and left and a vector perpendicular to the vector between the two points
		vec2 left_midpoint = (left + point) / 2.0;
		vec2 left_perpendicular = perpendicular(point - left);
		vec2 left_2 = left_midpoint + left_perpendicular;
		// Do the same for midpoint to right point
		vec2 right_midpoint = (point + right) / 2.0;
		vec2 right_perpendicular = perpendicular(right - point);
		vec2 right_2 = right_midpoint + right_perpendicular;
		
		if (dist < min_distance) {
			min_distance = dist;
			c_point = point;
   			left_top = get_line_intersection(left_midpoint, left_2, cell_id / scale, cell_id / scale + vec2(1.0, 0.0));
			right_top = get_line_intersection(right_midpoint, right_2, cell_id / scale, cell_id / scale + vec2(1.0, 0.0));
			right_bottom = get_line_intersection(right_midpoint, right_2, (cell_id + 1.0) / scale, (cell_id + 1.0) / scale + vec2(1.0, 0.0));
			left_bottom = get_line_intersection(left_midpoint, left_2, (cell_id + 1.0) / scale, (cell_id + 1.0) / scale + vec2(1.0, 0.0));
		}
	}
    
    float grad = (uv.x - mix(left_top.x, left_bottom.x, cell_uv.y)) / mix(right_top.x - left_top.x, right_bottom.x - left_bottom.x, cell_uv.y);

    vec2 brick_uv = vec2(grad, cell_uv.y);

    // Render the bricks
    
    float brick_height = 1.0 / scale.y;
	float round = 0.5 / brick_height;
	float mortar = 0.01 / brick_height;
	float bevel = 0.1 / brick_height;

    float iColor;
	vec2 d = (min(brick_uv.xy, 1.0 - brick_uv.xy) * -2.0)*scale.yx+vec2(round+mortar);
    iColor = length(max(d,vec2(0))) + min(max(d.x,d.y),0.0)-round;
	iColor = clamp(-iColor/bevel, 0.0, 1.0);
    
    // Output to screen
    fragColor = vec4(vec3(iColor),1.0);
} 