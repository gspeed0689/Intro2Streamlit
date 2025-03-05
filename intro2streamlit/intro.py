import streamlit as st

st.set_page_config(
    page_title="Introduction to Streamlit", 
    page_icon="🎏",
    layout="wide"
)

st.title("Welcome to the Programming Cafe Introduction to Streamlit!")

with open("assets/intro_markdown_01.md", "r") as f:
    markdown_01 = f.read()

st.markdown(markdown_01)