#import overpy
import json
import numpy as np
import matplotlib.pyplot as plt
import requests

#api = overpy.Overpass()

def downloadData():
    overpass_url = "http://overpass-api.de/api/interpreter"
    overpass_query = """
[timeout:600]
[out:json]
;
area(3600047796)->.area_0;
(
  node
    ["sport"="basketball"]
    (area.area_0);
  relation
    ["sport"="basketball"]
    (area.area_0);
);
(
  ._;
  >;
);
out;
"""
    response = requests.get(overpass_url, 
                        params={'data': overpass_query})
    data = response.json()
    return data

def plotData(data):
    # Collect coords into list
    coords = []
    for element in data['elements']:
        if element['type'] == 'node':
            lon = element['lon']
            lat = element['lat']
            coords.append((lon, lat))
        elif 'center' in element:
            lon = element['center']['lon']
            lat = element['center']['lat']
            coords.append((lon, lat))
    # Convert coordinates into numpy array
    X = np.array(coords)
    plt.plot(X[:, 0], X[:, 1], 'o')
    plt.title('Basketball field locations')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.axis('equal')
    plt.show()
