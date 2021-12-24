# Dask for parallel
import json
import os
import osm

# For running locally, use a dump in stead of querying the overpass API
test_courts_json = 'C:/Users/BartZwemmerGISSpecia/Documents/bball-court-finder/training_data/courts_nl.json'
if not os.path.isfile(test_courts_json):
    print("Fetching data from OSM")
    data = osm.downloadData()
else:
    print("Using local test data")
    # Opening JSON file
    d = open(test_courts_json, 'r')
    data = json.loads(d.read())

# Show JSON data
osm.plotData(data)