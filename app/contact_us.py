import streamlit as st
from PIL import Image
from prog import make_email

# functions
def app():

     # Button css
    buttoncss = st.markdown("""
    <style>
    div.stButton > button:first-child {
        width: 480px;
        height:40px;
        justify-content: center;
        font-family: "IBM Plex Sans", sans-serif;
        font-size: 0.8rem;
    }
    </style>""", unsafe_allow_html=True)

    with st.container():
        # Top part
        ui_col, st_col = st.columns(2)

        with ui_col:
            with st.form(key="contact_form"):  # user input col
                st.header("Contact Us")
                f_name = st.text_input("FIRST NAME", max_chars=20,
                                        help="Please enter your first name")
                l_name = st.text_input("LAST NAME", max_chars=20,
                                        help="Please enter your last name")
                email = st.text_input("EMAIL ADDRESS", max_chars=20,
                                        help="Please enter your email address (ex)abc123.gmail.com")
                inquiry_title = st.text_input("INQUIRY TITLE", max_chars=50, 
                                            help="Please enter inquiry title")
                detail = st.text_area("DETAILS", height=5, max_chars=300,
                                    help="Please enter inquiry details")
                submit_button = st.form_submit_button(label="Submit")

            # send email
            if submit_button:
                st.success(
                    "Thank you for getting in touch! We appreciate you contacting us.")
                make_email.send_email(f_name, l_name, email, inquiry_title, detail)

        with st_col:  # explaination col
            st.header("How Can We Help?")
            st.write("""
                        Please fill up the form. Out team will get back to you within 48 hours.\n\n\n

                        **Phone number:** +0123 4567 8910\n\n

                        **Email:** support_team@StaFiIndia.com\n\n

                        **Addreess:** 457-89, 254 Street, District 7
            """)

            st.header("Working hours")
            st.write("""
                        **Monday:** 9 AM - 5 PM \n
                        **Tuesday:** 9 AM - 5 PM \n
                        **Wednesday:** 9 AM - 5 PM \n
                        **Thursday:** 9 AM - 5 PM \n
                        **Friday:** 9 AM - 5 PM \n
                        **Saturday:** 10 AM - 5 PM \n
                        **Sunday:** 10 AM - 3 PM \n
            """)


        # Bottom part
        st.header("Meet our helpful support team!")

        # nested col in st_col2, show support team's team member
        sttm_col1, sttm_col2, sttm_col3 = st.columns(3)
        with sttm_col1:
            member_profile1 = Image.open("lib//img//support_team_member1.png")
            st.image(member_profile1,
                    caption="Phan Do Ngoc Linh")
        with sttm_col2:
            member_profile1 = Image.open("lib//img//support_team_member2.png")
            st.image(member_profile1,
                    caption="Nguyen Dang Nhat",)
        with sttm_col3:
            member_profile1 = Image.open("lib//img//support_team_member3.png")
            st.image(member_profile1,
                    caption="Vo Ngoc Diem Tien")


        # Footer
    st.markdown("""
    <nav class="navbar fixed-bottom navbar-expand-xl navbar-dark" style="background-color: #234362; border-top-style: solid;">
    <div style="padding-left: 650px; color: #FFFFFF; "> ©All Rights Reserved By STAFLINDA</div>
    </nav>
    """, unsafe_allow_html=True)
