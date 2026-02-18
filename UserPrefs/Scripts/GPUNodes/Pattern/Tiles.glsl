in float Size = 1;
in float Edge =1;
in float face_tone = 0.9; // 0.9 for the face of the tile
in   float edge_tone = 0.5; // 0.5 for the edge
void mainImage( out vec4 fragColor, in vec2 fragCoord(knot = ioUV) )
{
    vec2 uv = fragCoord/iResolution.yy;
    float size = 1.0/8.0 * Size;   // size of the tile
    float edge = size/32.0 * Edge; // size of the edge
    float face_tone = 0.9; // 0.9 for the face of the tile
    float edge_tone = 0.5; // 0.5 for the edge
    uv = sign(vec2(edge) - mod(uv, size));
    fragColor = vec4(face_tone - sign(uv.x + uv.y + 2.0) * (face_tone - edge_tone));
}