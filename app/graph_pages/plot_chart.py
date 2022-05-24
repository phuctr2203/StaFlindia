import altair as alt
import streamlit as st
import pandas as pd


def app():
    st.title("Plot chart")
    with st.container():
        st.write("""
                    Our plot chart provides an analysis of the relationship between price and departure time of the given six airlines. 
                    In each chart, we compare the prices in business class with those in economy class.
                    """)
        st.header("Guide")
        st.write("""
                Step 1) Choose which airline you wish to see their ticket prices analysed. \n
                Step 2) Click the submit button.\n
                Step 3) See the result.
                """)


    csv_url ='https://raw.githubusercontent.com/Lee-GaIn/-BIIT-Project/main/lib/data/data.csv'
    df = pd.read_csv(csv_url)
    d = st.selectbox("Pie chart about:",
                                ('Air India', 'AirAsia', 'GO FIRST', 'Indigo', 'SpiceJet',
                                'Vistara'))


    scatter = alt.Chart(df ).mark_point(filled=True).encode(
        alt.X('dep_time'),
        alt.Y('price'),
        alt.Size('class', scale=alt.Scale(range=[200, 500])),
        alt.OpacityValue(0.6),
        alt.Color('class'),
        tooltip = ['date', 'ch_code', 'from', 'to']
    ).transform_filter(alt.FieldEqualPredicate(field='airline', equal=d)).properties(height=850, width=850, title = 'Plot chart').interactive()

    st.altair_chart(scatter)

    # Footer
    st.markdown("""
    <nav class="navbar fixed-bottom navbar-expand-xl navbar-dark" style="background-color: #234362; border-top-style: solid;">
    <div style="padding-left: 650px; color: #FFFFFF; "> ©All Rights Reserved By STAFLINDA</div>
    </nav>
    """, unsafe_allow_html=True)