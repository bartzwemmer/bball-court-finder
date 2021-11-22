# Dask for parallel
import os, sys
import osm

#SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
#sys.path.append(os.path.dirname(SCRIPT_DIR))

data = osm.downloadData()
print(data)
osm.plotData(data)