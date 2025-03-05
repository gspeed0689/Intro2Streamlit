import streamlit as st
from streamlit_image_coordinates import streamlit_image_coordinates as sic

intro_text = """# Forms and Input

There are lots of options for forms and input in Streamlit: 
            
"""

st.markdown(intro_text)

st.write("Basic checkboxes and radios")
st.checkbox("Checkboxes", value=False, key="CB1")
st.radio("Radio", ["Universiteit Utrecht", "Utrecht University"])

st.write("Fancier multi- and single-select")
st.multiselect("Tagged multi-select", ["str", "float", "int", "numpy.array"])
st.pills("Pills", ["Paracetamol", "paracetamol", "para-ceta-mol"])
st.feedback("stars")
st.feedback("thumbs")
st.segmented_control("Segments", ["Yes", "Maybe", "No"])
st.select_slider("Wavelength", ["red", "orange", "yellow", "green", "blue", "violet", "violent", "ultra-violet", "ultra-violent"])

st.write("There are also some more advanced inputs.")

st.color_picker("Pick a color", value="#c00a35")

st.date_input("Select a date")

st.time_input("What time is it?")

st.header("Advanced Inputs")

st.write("You can also accept audio and camera inputs.")

st.audio_input("Record an audio bit")

st.camera_input("Take a picture")

st.subheader("Image annotations")

st.write("There are many first and third party components for image annotation. Please click on the cat that sold me pears by Fort Rijnauwen")

value = sic("assets/cat.jpg", width=500)
if value:
    st.write(f"You clicked on {value}")