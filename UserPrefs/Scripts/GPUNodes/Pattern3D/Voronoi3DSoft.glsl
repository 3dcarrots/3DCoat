// 3d voronoi based on florian berger (flockaroo) - 2017
vec3 hash(vec3 p)
{
    p = vec3(dot(p, vec3(171.0, 317.0, 747.0)),
             dot(p, vec3(295.0, 133.0, 261.0)),
             dot(p, vec3(135.0, 219.0, 146.0)));
    return fract(sin(p) * 45458.51423);
}

void main(
    in vec3 FragCoord(value= 1, knot= ioFragCoord, expression= R=(V*K), min= -10.0, max= 10.0),
    in float Scale(value= 1.0, min= 0.01, max= 100.0, expression= R=(V*K)),
    in float Strength(value= 1.0, min= 0.0, max= 2.0, expression= R=(V*K)),
    in float SoftSize(value= 0.05, min= 0.001, max= 1.0, expression= R=(V*K)),
    out float Distance,
    out float Closest,
    out float CellID
)
{
    float voronoiStrength = clamp(Strength, 0.0, 2.0);

    vec3 p = FragCoord * Scale;
    vec3 g = floor(p);
    p -= g;

    float mindist = 1000.0;
    vec3 minPos = p;
    vec3 minCell = vec3(0.0);

    int sampWidth = max(1, int(floor(voronoiStrength)));

    for (int z = -sampWidth; z <= sampWidth; z++)
    {
        for (int y = -sampWidth; y <= sampWidth; y++)
        {
            for (int x = -sampWidth; x <= sampWidth; x++)
            {
                vec3 b = vec3(float(x), float(y), float(z));
                vec3 pos = b + voronoiStrength * hash(g + b);
                
                vec3 r = pos - p;
                float dist = dot(r, r);

                if (dist < mindist)
                {
                    mindist = dist;
                    minPos = pos;
                    minCell = b;
                }
            }
        }
    }

    float minhdist = 0.0;
    for (int z = -sampWidth; z <= sampWidth; z++)
    {
        for (int y = -sampWidth; y <= sampWidth; y++)
        {
            for (int x = -sampWidth; x <= sampWidth; x++)
            {
                vec3 b = vec3(float(x), float(y), float(z));
                vec3 pos = b + voronoiStrength * hash(g + b);
                
                vec3 diff = pos - minPos;
                if (dot(diff, diff) > 0.00001)
                {
                    float hdist = abs(dot(p - (pos + minPos) * 0.5, normalize(diff))) - 0.1;
                    minhdist += exp(-hdist / SoftSize);
                }
            }
        }
    }
    
    minhdist = -log(minhdist) * SoftSize;

    Distance = minhdist*2.0;
    Closest = mindist;
    CellID = abs(dot(g + minCell, vec3(1.0, 57.0, 113.0)));
}
