import streamlit as st
import pandas as pd
import altair as alt
import plotly.figure_factory as ff
import plotly.express as px


# Hide menu
hide_menu = """
<style>
#MainMenu { visibility: hidden;}
</style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)

st.title("Airline-Price Chart")

# Link css footer
st.markdown(
    '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',
    unsafe_allow_html=True)

# Function
# CSV file
csv = 'https://raw.githubusercontent.com/Lee-GaIn/-BIIT-Project/main/lib/data/data_integer.csv'
df = pd.read_csv(csv)

st.write("The chart shows the price of each airline with both economy class and business class")

  
  # LOAD DATA

df.columns = ['date', 'airline', 'ch_code', 'num_code', 'dep_time', 'from', 'time_taken', 'stop', 'arr_time', 'to', 'price', 'class', 'ticket_id', 'weekday']
price = df['price'].unique().tolist()
airline = df['airline'].unique().tolist()
flight_class = df['class'].unique().tolist()
from_des = df['from'].unique().tolist()

start_price = st.selectbox('Start Price: ', price, 0)
end_price = st.selectbox('End Price: ', price, 0)
airline_options = st.multiselect('Airline: ', airline, default=airline)
class_options = st.multiselect('Class: ', flight_class, default=flight_class)

df = df[df['airline'].isin(airline_options)]
df = df[df['price'] >= start_price]
df = df[df['price'] <= end_price]
df = df[df['class'].isin(class_options)]

x = df['airline']
y = df['price']

fig = alt.Chart(df).mark_bar().encode(
  x="airline", y="price", color="airline").interactive()



st.altair_chart(fig, use_container_width=True)


# Footer
st.markdown("""
<nav class="navbar fixed-bottom navbar-expand-xl navbar-dark" style="background-color: #234362; border-top-style: solid;">
<div style="padding-left: 650px; color: #FFFFFF; "> ©All Rights Reserved By STAFLINDA</div>
</nav>
""", unsafe_allow_html=True)
