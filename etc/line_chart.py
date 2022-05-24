import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
from PIL import Image


st.title("Line Graph")

# LOAD DATA

def app():
    df = pd.read_csv("lib//data//data.csv")

    # SELECTION
    airline = df['airline'].unique().tolist()
    price = df['price'].unique().tolist()

    price_selection = st.slider('Price: ',
                                min_value=min(price),
                                max_value=max(price),
                                value=(min(price), max(price)))

    airline_selection = st.multiselect('Airline: ',
                                    airline,
                                    default=airline)

    # FILTER DATAFRAME
    mask = (df['price'].between(*price_selection)) & (df['airline'].isin(airline_selection))
    number_of_result = df[mask].shape[0]
    st.markdown(f'*Available Results: {number_of_result}*')

    # GRAPH

    chart = alt.Chart(df, title="Business Class").mark_line().encode(
        x='ticket_id',
        y='price'
    )

    st.altair_chart(chart, use_container_width=True)

    st.write(df)

