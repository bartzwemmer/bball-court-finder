import json
from geopy.geocoders import Nominatim
import numpy as np
import matplotlib.pyplot as plt
import requests

def getOSMId(cityname):
  # Geocoding request via Nominatim
  geolocator = Nominatim(user_agent="city_compare")
  geo_results = geolocator.geocode(cityname, exactly_one=False, limit=3)
  # Searching for relation in result set
  for r in geo_results:
    #print(r.address, r.raw.get("osm_type"))
    if r.raw.get("osm_type") == "relation":
        city = r
        break

  # Calculating area id from relation id
  area_id = int(city.raw.get("osm_id")) + 3600000000

  return area_id

def downloadData():
    # For testing, using Almere to verify fields
    area_id = getOSMId('Almere')

    overpass_url = "http://overpass-api.de/api/interpreter"
    """
    geocodeArea is an address or locality. All data that intersects is retrieved
    """
    overpass_query = """
    [out:json] [timeout:600];
    area(%s) -> .area_0;
    (
    way["sport"="basketball"](area.area_0);
    relation["sport"="basketball"](area.area_0);
    );
    (._;>;);
    out body;
    """ % area_id
    response = requests.get(overpass_url, 
                        params={'data': overpass_query})
    try:
      data = response.json()
      return data
    except:
      print("No data in reponse: "+str(response))
      return None

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

if __name__ == '__main__':
  # Get OSM data
  data = downloadData()
  # Write data to file if it doesn't exist, so we don't need to re-download it with every run during development.
  if data is not None:
    with open('C:/Users/BartZwemmerGISSpecia/Documents/bball-court-finder/training_data/courts_nl.json', 'w') as outfile:
        json.dump(data, outfile)
    print("Data written")
  else:
    print("No data written")

  
