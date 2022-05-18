import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

html = """
Volcano name: <a href="https://www.google.com/search?q=Mount+%s" target="_blank">%s</a> <br/>
Elevation: %s m
"""


def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif elevation < 3000:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=[49.21, -122.943],
                 zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Volcano Map")

for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=folium.Popup(
        iframe), color='grey', fill_opacity=0.7, fill=True, fill_color=color_producer(el)))


map.add_child(fg)
map.save("map.html")
