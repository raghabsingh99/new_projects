from textwrap import fill
from tkinter.ttk import Style
from turtle import fillcolor
import folium
import pandas

data = pandas.read_csv("volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elv = list(data["ELEV"])

def color_produce(elevation):
    if elevation<1000:
        return 'green'
    elif 1000<= elevation < 1500:
        return 'orange'
    else:
        return 'red'

 
map = folium.Map(location=[30.58, -99.09])
for lt,ln, elv in zip(lat,lon,elv):
    map.add_child(folium.CircleMarker(location=[lt,ln], radius= 6, fill_color=color_produce(elv), popup=str(elv), icon=folium.Icon(color=color_produce(elv))))

map.add_child(folium.GeoJson(data=open('world.json','r', encoding='utf-8-sig'),Style_function=lambda x:{'fillcolor' : 'green' if x['properties']['POP2005']<1000000 else 'orange' if 2000000<= x['properties']['progress'] else 'red'}))
map.save("Map1.html")  