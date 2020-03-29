from numpy import arange
import random
import json


features = []

def sample_floats(low, high, k=200):
    """ Return a k-length list of unique random floats
        in the range of low <= x <= high
    """
    result = []
    seen = set()
    for i in range(k):
        x = random.uniform(low, high)
        while x in seen:
            x = random.uniform(low, high)
        seen.add(x)
        result.append(x)
    return result

f = open("fakedata.json", "w")

x_lat = sample_floats(78.4767, 78.4970)
print(len(x_lat))
y_lat = sample_floats(17.3750, 17.3950)

for x in x_lat:
    for y in y_lat:
            x = round(x,4)
            y = round(y,4)
            features.append({ "type": "Feature", "properties": { "id": "Example_id", "severity": random.randint(1,10), "time": 1507425650893,
                                                             "felt": random.random() }, "geometry":
            { "type": "Point", "coordinates": [ x,y ] } })



geojson =  {
"type": "FeatureCollection",
"crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } },
"features": features}
f.write(str(json.dumps(geojson)))
f.close()

