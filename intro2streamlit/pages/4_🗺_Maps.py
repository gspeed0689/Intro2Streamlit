import folium.map
import streamlit as st
from streamlit_folium import st_folium
import folium
import pandas as pd

st.title("Maps")

map_intro_text = """
You can make maps in Streamlit with `streamlit-folium`, which also leverages the `folium` library. 

## RondstadRail

Here below I have created a map with a GeoJSON of rail lines and a Pandas DataFrame for station points.
These geographic features are added to a basic Folium map with OpenStreetMap as the basemap. 

The map itself is inspired by the Yamanote line in Tokyo, it runs clockwise and counter-clockwise. 
Here RondstadRail, RondstadAir, and ExtraRondstad would drive clockwise and counter-clockwise around the Randstad+,
no back and forth journies. 
"""

st.markdown(map_intro_text)

rondstad_lines = "assets/RondstadRail.geojson"
rondstad_points = "assets/RondstadStations.csv"

folium_map = folium.Map([52, 5.2])

folium.GeoJson(rondstad_lines).add_to(folium_map)

points_df = pd.read_csv(rondstad_points)
for i, x in points_df.iterrows():
    folium.Marker([x["lat"], x["lon"]], popup=x["name"], icon=folium.map.Icon("cadetblue")).add_to(folium_map)

sf_map = st_folium(folium_map, use_container_width=True)