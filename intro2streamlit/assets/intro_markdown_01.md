Welcome to this introduction to Streamlit at the UU Programming Cafe!
I have made this demonstration of Streamlit in Streamlit, it is very easy to get started with. 

![QR Code to access this app on your computer]("intro2streamlit/assets/qr_code.png")

## What is Streamlit?

Streamlit is a web interface for Python to make dashboards and interactive experiences. 
It is commonly used by machine learning teams to create a dashboard to visualize and interact with
the data they are working on. 

Streamlit has a concept of components that you can add to build up the webpage with static and dynamic content.
There are components to have text, buttons, graphs, maps, forms, and so much more. 

## How to install Streamlit

It is a library available through Pip and conda: 

* `pip install streamlit`
* `conda install streamlit`
* `uv pip install streamlit` / `uv add streamlit`

## Using Streamlit in Python

Streamlit is a simple import:

    import streamlit as st

Then you can call a Streamlit component to get started, and just for this example I'll just use the source code for this file:

    import streamlit as st

    st.title("Welcome to the Programming Cafe Introduction to Streamlit!")

This will create large text on the screen to act as a title, and is one of the basic text components. 
There are other basic components like `st.text()`, but for a long webpage like this is becoming, we can write content in markdown:

    import streamlit as st

    st.title("Welcome to the Programming Cafe Introduction to Streamlit!")
    
    with open("assets/intro_markdown_01.md", "r") as f:
        markdown_01 = f.read()

    st.markdown(markdown_01)

And that's it, that is this entire webpage.

### Wait, what about the tabs on the left?

These tabs were created using a file structure that Streamlit will recognize. 
By creating a subfolder called `pages`, and naming them with a number and then a title, 
Streamlit will put the `.py` files from this folder in order on the left side for navigation. 

## How to run streamlit

With your venv activated, in the command line run `streamlit run intro.py`, or whatever the name for your base `.py` file. 