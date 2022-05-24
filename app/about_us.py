import streamlit as st


def app():

    # apply css file
    with open('lib//style//about_us_style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


    with st.container():
        mis_col1, mis_col2 = st.columns([1,1.5])
        with mis_col1:
            st.header("Background")
            st.write("""
            We are a team of five ambitious students from RMIT University, majoring in Information Technology. 
            By enrolling in course COSC2636 - Building IT Systems, with the guidance of professor Shan Chen, 
            our team has created this Data Analyst Web Application after witnessing the blossoming interest 
            in ticket research for the past decades.
                    """)

            st.write("""
            Our objective is to assist people coming from all over the world with different backgrounds in 
            choosing the most suitable aviation option. From a given dataset, we analyze the prices, 
            departure time, length of flight, flight directions and so on, so that we can provide users with 
            as much information as possible. This would help them understand what they are paying for and how 
            they utilize their budget to have the best service. 
                    """, styles= {"text-align": "justify"})

            st.write("""
            Our team used Streamlit, applying Machine Learning models to process data, make a prediction and suggestion.
            Our team also uses Python for graphic illustration.
            """, styles= {"text-align": "justify"})
        
        with mis_col2:
            st.image("https://dashboard.iammedia.am/assets/uploads/posts/thumbnails/image-1593853889761.jpg") #image for our mission

        st.markdown("""
                <body>
                    <div class = "empty" style="padding: 50px;">
                    </div>
                </body>
        """, unsafe_allow_html=True)


        #PART 3) ABOUT US
        abt_team_col1, abt_team_col2 = st.columns(2)

        with abt_team_col1:
            st.image("https://images.unsplash.com/photo-1476304884326-cd2c88572c5f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=869&q=80") #image for our mission
        with abt_team_col2:
            st.header("About our team")
            st.write("""
            After getting to know each other in course COSC2636, our team realized that everybody shared the same interests in working with datas. 
            Through several more research, we have decided to create StarFiIndia. Despite the differences in opinions and strong personalities, 
            our team managed to push those challenges aside to perfect the website, and proudly give you this final product.
                    """)

            st.write("""
            StaFiIndia is the name of the company. 
            This name is a compound word for Statistic, Flight, and India. 
            It means our company will make efforts to effectively display statistics related to 
            India's domestic airline tickets with fascinating graphics.
            Our company hopes that customers will get the information they want through their services in a short period of time.
            """)


            # Footer
    st.markdown("""
    <nav class="navbar fixed-bottom navbar-expand-xl navbar-dark" style="background-color: #234362; border-top-style: solid;">
    <div style="padding-left: 650px; color: #FFFFFF; "> ©All Rights Reserved By STAFLINDA</div>
    </nav>
    """, unsafe_allow_html=True)


