// Fast Voronoi Fracture 3D Pattern
// Uses the F2-F1 approximation for extremely fast cell boundaries (ideal for fracturing/cracking)

// Hash function
vec3 hash3(vec3 p) {
	p = vec3(dot(p, vec3(127.1, 311.7, 74.7)),
			 dot(p, vec3(269.5, 183.3, 246.1)),
			 dot(p, vec3(113.5, 271.9, 124.6)));
	return fract(sin(p) * 43758.5453123);
}

void main(
    in vec3 FragCoord(value= 1, knot= ioFragCoord, expression= R=(V*K), min= -10.0, max= 10.0),
    in float Scale(value= 4.0, min= 0.01, max= 100.0, expression= R=(V*K)),
    in float FractureWidth(value= 0.06, min= 0.0, max= 1.0, expression= R=(V*K)),
    in float Jitter(value= 1.0, min= 0.0, max= 1.0, expression= R=(V*K)),
    out float Distance,
    out float CellID,
    out vec4 BaseColor
)
{
    vec3 p = FragCoord * Scale;
    vec3 cell = floor(p);
    vec3 frac_pos = fract(p);
    
    float min_dist1 = 1000.0;
    float min_dist2 = 1000.0;
    
    vec3 closest_cell = vec3(0.0);
    
    // Single-pass loop for both closest (F1) and second-closest (F2) points
    // This is a massive optimization compared to true Voronoi boundaries!
    for(int x = -1; x <= 1; x++) {
        for(int y = -1; y <= 1; y++) {
            for(int z = -1; z <= 1; z++) {
                vec3 neighbor = vec3(float(x), float(y), float(z));
                
                // Calculate point position inside the cell, with adjustable Jitter
                vec3 rPoint = hash3(cell + neighbor);
                vec3 point = vec3(0.5) + (rPoint - vec3(0.5)) * Jitter;
                
                vec3 diff = neighbor + point - frac_pos;
                float dist = length(diff);
                
                if (dist < min_dist1) {
                    min_dist2 = min_dist1;
                    min_dist1 = dist;
                    closest_cell = cell + neighbor;
                } else if (dist < min_dist2) {
                    min_dist2 = dist;
                }
            }
        }
    }
    
    // The F2 - F1 approximation gives a very fast distance to the cell boundary (edges).
    // It creates variable-thickness cracks which actually look better for natural fracturing.
    float edge_factor = min_dist2 - min_dist1;
    
    // Convert to an SDF representing the fracture gaps.
    // We divide by Scale so the output Distance matches real world coordinates.
    Distance = (edge_factor - FractureWidth) / Scale;
    
    // Compute a pseudo-random ID for the closest cell
    CellID = fract(dot(closest_cell, vec3(12.9898, 78.233, 45.164)));
    
    // Basic coloring: Fracture gaps are dark, chunks are colored slightly randomly
    vec3 chunkColor = vec3(0.55, 0.6, 0.65) + hash3(closest_cell) * 0.3;
    vec3 gapColor = vec3(0.05, 0.05, 0.05);
    
    // Smooth blending at the fracture boundary based on the width
    float mask = clamp(edge_factor / max(FractureWidth, 0.001), 0.0, 1.0);
    BaseColor = vec4(mix(gapColor, chunkColor, mask), 1.0);
}
