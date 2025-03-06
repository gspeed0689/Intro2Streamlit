import streamlit as st

st.set_page_config(
    page_title="Introduction to Streamlit", 
    page_icon="🎏",
    layout="wide"
)

st.title("Welcome to the Programming Cafe Introduction to Streamlit!")

st.image("intro2streamlit/assets/qr_code.png")

with open("intro2streamlit/assets/intro_markdown_01.md", "r") as f:
    markdown_01 = f.read()

st.markdown(markdown_01)