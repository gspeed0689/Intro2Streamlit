import streamlit as st

st.title("Examples")

vesuvius_md = """
## Vesuvius

First of all, to toot my own horn, I'll share my first Streamlit app that got me excited about how easy it is.

The app explains what I did, the TL;DR is that I made a bunch of panoramas and 3D models of the Vesuvius caldera. 
The app uses many of the tools on the previous pages to explore what I created. 
"""

st.markdown(vesuvius_md)

st.link_button("Go to the Vesuvius Panorama Example", "https://vesuvius.garrettspeed.com/")

