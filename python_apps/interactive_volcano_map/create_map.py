from os import read
import folium
import pandas as pd
import pathlib

#set current working directory
cwd = pathlib.Path(__file__).parent.resolve()

#read in volcano locations
volcano_file = pd.read_csv(f'{cwd}\Volcanoes.txt')

#initialise the map and volcano feature group
map = folium.Map(location=[33.58,-99.09], zoom_start=6, tiles='Stamen Terrain')
volcano_points = folium.FeatureGroup(name='Volcanoes')

#create latitude, longitude lists to loop through
volcano_lat = list(volcano_file['LAT'])
volcano_lon = list(volcano_file['LON'])
volcano_name = list(volcano_file['NAME'])

#add all the volcano markers to the feature group
for lat, lon, name in zip(volcano_lat, volcano_lon, volcano_name):
    #iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    volcano_points.add_child(folium.Marker(location=[lat, lon], popup=folium.Popup(name), icon=folium.Icon(color='red')))

#add the feature group with the volcano markers to the map
map.add_child(volcano_points)

#output map html file
map.save(outfile=f'{cwd}\\volcanomap.html')