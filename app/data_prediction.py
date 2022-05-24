import streamlit as st
import pickle
import pandas as pd
def app() :
    model = pickle.load(open('lib//data//model.sav', 'rb'))

    st.title('Data Prediction')
    st.sidebar.header('Data')
    st.write("""
                StaFiIndia provides price prediction based on your input
                """)
    st.header("Guide")
    st.write("""
            Step 1) Input the information \n
            Step 2) The price prediction will display below \n
            """)

    class_to_view = st.slider("Choose class (Economy: 1, Business: 0):", 0, 1, 0, 1, key=1)
    source_city = st.slider('Source city (Bangalore: 0, Chennai: 1, Delhi: 2, Hyderabad: 3, Kokalta: 4, Mumbai: 5):', 0, 5, 0, key=2)
    arrival_city = st.slider('Arrival (Bangalore: 0, Chennai: 1, Delhi: 2, Hyderabad: 3, Kokalta: 4, Mumbai: 5):', 0, 5, 0, key=3)
    airline = st.slider('Airline (AirAsia: 0, Air_India: 1, GO_FIRST: 2, INDIGO: 3, SpiceJet: 4, Vistara: 5):', 0, 5, 0, key=5)
    stops = st.slider("Stops", 0, 2, 0, key=7)
    days_left_to_flight = st.slider("Days left to flight:", 1, 49, 1, key=6)

    report_data = pd.DataFrame({"airline": [airline], "source_city": [source_city], "stops": [stops],
                                "arrival_city": [arrival_city], "class": [class_to_view],
                                "days_left_to_flight": [days_left_to_flight]})


    price_predict = model.predict(report_data)
    st.write("The approximately price for the flight is:", price_predict)

    ###################################################
    #Title: streamlit_navbar
    #Author: Chanin Nantasenamat
    #Date: 3 Oct, 2021
    # Code version: (Unknown)
    #Availability: https://github.com/dataprofessor/streamlit_navbar/blob/main/app_navbar.py (Accessed 8 May 2022)
    ###################################################


    # Link css footer
    st.markdown(
        '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',
        unsafe_allow_html=True)
 
    # Footer
    st.markdown("""
    <nav class="navbar fixed-bottom navbar-expand-xl navbar-dark" style="background-color: #234362; border-top-style: solid;">
    <div style="padding-left: 650px; color: #FFFFFF; "> ©All Rights Reserved By STAFLINDA</div>
    </nav>
    """, unsafe_allow_html=True)