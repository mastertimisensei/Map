import folium
import pandas

data=pandas.read_csv("Volcanoes_USA.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])
map= folium.Map(location=[38.58, -99.09], zoom_start=6)

def color_producer(elevation):
    if elevation <1000:
        return "green"
    elif 1000  <= elevation <3000:
        return "red"
    else:
        return "blue"

fgv=folium.FeatureGroup(name="Volcanoes")
for lt,ln,el in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln], radius=6 ,popup=("Elevation is {}m".format(el)), fill_color=color_producer(el),
    color="black", fill_opacity=0.7))

fgp=folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open("115 world.json","r",encoding='utf-8-sig').read(),
style_function=lambda x: {"fillColor":"green" if x['properties']['POP2005']<10_000_000
else 'orange' if 10_000_000<=x['properties']['POP2005']<20_000_000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")
