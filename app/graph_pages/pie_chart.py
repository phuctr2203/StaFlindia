import streamlit as st
from prog import make_pie_chart
import altair as alt
import pandas as pd


def app():
    # apply css file
    with open('lib//style//pie_chart.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    st.title("Pie chart")
    with st.container():
        st.write("""
                    StaFiIdia provides a data comparison service for two tickets' information.
                    It enables users to see details of the ticket and compare two tickets by each element.
                    """)
        st.header("Guide")
        st.write("""
                Step 1) Put the first ticket id and the second ticket id on the input box.\n
                Step 2) Click the submit button.\n
                Step 3) See the result.
                """)


    with st.container():
        user_opt = st.selectbox("Pie chart about:",
                            ('Date', 'Airline', 'Country code', 'Departure time', 'Departure city', 
                            'Duration','Stops', 'Arrival time', 'Arrival city', 'Cost', 'Class')
        )

    with st.container():
        label, ratio, etc_dict = make_pie_chart.draw_piechart(user_opt)
        source = pd.DataFrame({"category": label, "value":ratio})

        pie_chart=alt.Chart(source).mark_arc().encode(
            theta=alt.Theta(field="value", type="quantitative"),
            color=alt.Color(field="category", type="nominal"))
        st.altair_chart(pie_chart)         # draw pie chart


        
        # show etc details
        etc_items_len = len(etc_dict)
        if etc_items_len >= 2:
            items_list_str = ""
            last_item_idx = etc_items_len - 1
            idx = 0
            
            for k in etc_dict.keys():
                items_list_str += k + "(" + str(etc_dict[k]) + "%)"
                if (idx != last_item_idx):
                    items_list_str += ",   "

                idx = idx + 1
            


            #display detail descrption
            st.write("Some elements accounting for less than 5% of the total were found. The elements were "
                        + items_list_str + ". These elements were consolidated in the 'etc' field on the chart.")
        
        # show detail description
        if user_opt == 'Departure time' or user_opt == 'Arrival time':
            st.write("The time range follows the criterion below.")
            st.write("""
                        From 05:00 to 11:59: Morning \n
                        From 12:00 to 16:59: Afternoon \n
                        From 17:00 to 20:59: Evening \n
                        From 21:00 to 04:59: Night \n
                    """)

    # Footer
    st.markdown("""
    <nav class="navbar fixed-bottom navbar-expand-xl navbar-dark" style="background-color: #234362; border-top-style: solid;">
    <div style="padding-left: 650px; color: #FFFFFF; "> ©All Rights Reserved By STAFLINDA</div>
    </nav>
    """, unsafe_allow_html=True)