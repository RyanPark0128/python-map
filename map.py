import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
map = folium.Map(location=[49.21, -122.943],
                 zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for lt, ln in zip(lat, lon):
    fg.add_child(folium.Marker(
        location=[lt, ln], popup="Hi I am a Marker", icon=folium.Icon(color="green")))


map.add_child(fg)
map.save("map.html")
