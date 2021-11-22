from rasterio import MemoryFile
from rasterio.plot import show
from urllib.request import urlopen

url ='https://services.terrascope.be/wms/v2?service=WMS&version=1.3.0&request=GetMap&layers=CGS_S2_RADIOMETRY&format=image/png&time=2020-06-01&width=1920&height=592&bbox=556945.9710290054,6657998.9149440415,575290.8578174476,6663655.255037144&styles=&srs=EPSG:3857'

tif_bytes = urlopen(url).read()

with MemoryFile(tif_bytes) as memfile:
     with memfile.open() as dataset:
            print(dataset.profile)
            show(dataset)