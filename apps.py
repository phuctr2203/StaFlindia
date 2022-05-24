import streamlit as st
from app import compare_tickets, contact_us, homepage, search2, about_us, data_prediction
from app.graph_pages import table, plot_chart,bar_chart, pie_chart, map
from streamlit_option_menu import option_menu


#build webpage
st.set_page_config(layout="wide")

with open ('style.css') as f:
    st.markdown(f'<style>{f.read()}<\style>',unsafe_allow_html=True)


###################################################
#Title: streamlit_all_gallery
#Author: insightsbees
#Date: 18 Feb 2022
# Code version: (Unknown)
#Availability: https://github.com/insightsbees/streamlit_app_gallery/blob/main/streamlit_app_gallary.py (Accessed 6 May 2022)
###################################################


# SET NAVIGATION BAR
with st.sidebar:
    choose = option_menu("Menu", ["HOME", "DATA SEARCH", 
                                    "ㄴTable", "ㄴBar chart", "ㄴPie chart", "ㄴPlot chart", "ㄴMap", 
                                    "DATA COMPARISON", "DATA PREDICTION", "ABOUT US", "CONTACT US"],
                         icons=['house', 'search', 
                                'bar chart', 'bar chart', 'bar chart', 'bar chart', 'bar chart', 
                                'square-half','graph-up-arrow','question-circle', 'person-lines-fill'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
                            "container": {"padding": "5!important", "background-color": "#234362!important"},
                            "icon": {"color": "orange", "font-size": "25px"}, 
                            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee", "color": "#FFFFFF"},
                            "nav-link-selected": {"background-color": "#FFFFFF", "color": "#234362"},
                        }
    )

if choose == "HOME":
    homepage.app()
elif choose == "DATA SEARCH":
    search2.app()
#grach pages 
elif choose ==  "ㄴTable":
    table.app()
elif choose ==  "ㄴBar chart":
    bar_chart.app()
elif choose ==  "ㄴPie chart":
    pie_chart.app()
elif choose ==  "ㄴPlot chart":
    plot_chart.app()
elif choose ==  "ㄴMap":
    map.app()
elif choose == "DATA COMPARISON":
    compare_tickets.app()
elif choose == "DATA PREDICTION":  #Nhat's page
    data_prediction.app() 
elif choose == "ABOUT US":
    about_us.app()
elif choose == "CONTACT US":
    contact_us.app()
    
