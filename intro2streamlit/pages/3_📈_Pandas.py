import pandas as pd
import plotly.express as px
import streamlit as st

st.title("Data Frames and Graphs")

intro_md = """
You can work with data frames and graphs using many standard libraries.
For data frames there is a Streamlit native format, and that can import from Pandas and Polars data frames. 
For graphs, you can use matplotlib, Plotly, Bokeh, Altair, Vega, GraphViz, and PyDeck. 

In the example below, I have supplied several CSVs that get loaded into a Pandas Data Frame, 
you can view the table, and then make small edits to format a Plotly chart. 
"""

st.markdown(intro_md)

datasets = {
    "Fruits and Vegetables": "intro2streamlit/assets/FruitsVeg_Weights.csv",
    "Grand Theft Auto V Robberies": "intro2streamlit/assets/GTA_V_Robberies.csv",
}

dataset = st.pills("Select a Dataset", 
                   list(datasets.keys()), 
                   default=list(datasets.keys())[0])

df = pd.read_csv(datasets[dataset])

data_column = st.pills("Select a column for data",
                           list(df.columns),
                           default=list(df.columns)[-1])

category_column = st.pills("Select a column for categories",
                           list(df.columns) + ["None"],
                           default="None")
if category_column == "None":
    category_column = None

st.dataframe(df)

chart_types = {
    "Box": px.box,
    "Violin": px.violin
}

box_violin = st.pills("Select a chart type",
                      list(chart_types.keys()),
                      default="Violin")

graph = chart_types[box_violin]

box = graph(df, y=data_column, x=category_column)
st.plotly_chart(box)