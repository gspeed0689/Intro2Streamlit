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
st.link_button("View Vesuvius Source Code", "https://github.com/gspeed0689/lavalit")

geobenchmarks_md = """
## GIS Benchmarks

Not currently running, however It Works On My Machine™, and you can see the source code: 
An app for uploading GIS benchmark data and get immediate results visualizations. 

This app works with the output files of the ArcGIS Pro ProPAT benchmarking tool and has three components:

1. The FastAPI web server to interface with a database
2. The upload Streamlit app which has a file upload input, the app then parses the input file, creates a Pandas dataframe, displays that to the uploader for approval, then POSTs that to the FastAPI endpoint.
3. The viewer Streamlit app will query the FastAPI endpoint for data, build a Pandas dataframe, and then display the results with options for grouping by computer or storage system. 
"""

st.markdown(geobenchmarks_md)

st.link_button("View the upload app source code", "https://github.com/gspeed0689/propat-benchmark-viewer/tree/master/upload_app")
st.link_button("View the viewer app source code", "https://github.com/gspeed0689/propat-benchmark-viewer/blob/master/viewer_app/viewer.py")

audio_md = """
## Audio Converter

For some researchers in a remote location, I made a locally deployable Streamlit app that would accept a file upload and convert that file to the lowest quality MP3 setting. 
The goal of this is to reduce file sizes for upload to a cloud service, large file sizes were experiencing errors with the spotty remote internet connection.

"""

st.markdown(audio_md)

st.link_button("View the overview video", "https://youtu.be/DvkIuB-6pw0")

catalog_md = """
## Catalog Image Tool

For the new Earth Sciences Lab Photography Lab we would like to have the highest quality images, 
and a part of that for museum collections is to have clear in-photo metadata. 
I created a Streamlit app that accepts a CSV file, parses that, and makes the column and data in the column available for 
displaying on an e-ink screen on a Raspberry Pi. 
The app currently runs on the Pi, however it is very slow, 
it will be changed so the app runs on the computer in the lab, and interacts with a FastAPI server on the Pi. 
The video shows the app running:
"""

st.markdown(catalog_md)

st.link_button("View the catalog tool video", "https://youtu.be/NHVl-6ijqKU")