import streamlit as st

# Text Section

with open("assets/page_01_section_01.md", "r") as f:
    markdown_text_section = f.read()

st.markdown(markdown_text_section)

st.link_button("Streamlit Text Documentation", "https://docs.streamlit.io/develop/api-reference/text")

with open("assets/page_01_section_02.md", "r") as f:
    markdown_input_section = f.read()

st.markdown(markdown_input_section)

st.link_button("Streamlit Input Documentation", "https://docs.streamlit.io/develop/api-reference/widgets")

with open("assets/page_01_section_03.md", "r") as f:
    markdown_media_section = f.read()

st.markdown(markdown_media_section)

st.link_button("Streamlit Media Documentation", "https://docs.streamlit.io/develop/api-reference/media")