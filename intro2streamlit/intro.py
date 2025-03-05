import streamlit as st

st.title("Welcome to the Programming Cafe Introduction to Streamlit!")

with open("assets/intro_markdown_01.md", "r") as f:
    markdown_01 = f.read()

st.markdown(markdown_01)