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
volcano_elevation = list(volcano_file['ELEV'])

#Function to set colour of volcano based on elevation level
def setVolcanoMarkerColour(elevation):
    if elevation >= 3000:
        return 'red'
    elif elevation >= 2000:
        return 'orange'
    elif elevation >= 1000:
        return 'green'
    else:
        return 'blue'

#Define html for pop-up text
popup_html = """
<h4 class='volcano-name' style='margin-bottom: 5px;'>%s</h4>
<div class='volcano-info-list'>
    <div class='list-item'>Latitude: %s</div>
    <div class='list-item'>Longitude: %s</div>
    <div class='list-item'>Elevation: %sm</div>
</div>
"""

#add all the volcano markers to the feature group
for lat, lon, name, elevation in zip(volcano_lat, volcano_lon, volcano_name, volcano_elevation):
    popup_display = folium.IFrame(html=popup_html % (name, lat, lon, elevation), width=200, height=100)
    volcano_points.add_child(folium.CircleMarker(location=[lat, lon], popup=folium.Popup(popup_display), radius=6, 
    color='black', weight=2, fill_color=setVolcanoMarkerColour(elevation=elevation), fill_opactiy=0.95))

#add the feature group with the volcano markers to the map
map.add_child(volcano_points)

#output map html file
map.save(outfile=f'{cwd}\\volcanomap.html')