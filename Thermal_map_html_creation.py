from localtileserver import get_leaflet_tile_layer, TileClient
from ipyleaflet import Map
image_path = '../02_Data/02_Thermal/DJI_202402291328_007_PRUEBAPANELESSOLARES-30-50-80_RGB_3_bands_COG_jpeg.tif'

# First, create a tile server from local raster file
tile_client = TileClient(image_path)

# Create ipyleaflet tile layer from that server
t = get_leaflet_tile_layer(tile_client, band=[1,2,3])

# Create ipyleaflet map, add tile layer, and display
m = Map(center=tile_client.center(), zoom=14)
m.add_layer(t)
m
m.save('Thermal_map.html')