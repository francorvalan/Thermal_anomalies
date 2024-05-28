from localtileserver import get_leaflet_tile_layer, TileClient
from ipyleaflet import Map
image_path = 'Thermal_orthomosaic.tif'

# First, create a tile server from local raster file
tile_client = TileClient(image_path)

# Create ipyleaflet tile layer from that server
t = get_leaflet_tile_layer(tile_client, band=[1,2,3])

# Create ipyleaflet map, add tile layer, and display
m = Map(center=tile_client.center(), zoom=14)
m.add_layer(t)
m
m.save('Thermal_map.html')
