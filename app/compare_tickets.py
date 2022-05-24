# IMPORT LIBRARY
import streamlit as st
import pandas as pd
from prog import make_compare_table

# function
def app():
    with st.container():
        # SETTING

        # apply css file
        with open('lib//style//compare_tickets_style.css') as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    st.title("DATA COMPARISON")
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


        def_data = {'The first ticket ID': ['Vistara', '4792', '24/03/22', 'Bangalore', 'Mumbai', '19:55',
                                            '14:30', 'Economy', '18h 35m', '1-stop', 'UK-893'],

                    'The second ticket ID': ['Vistara', '4792', '24/03/22', 'Bangalore', 'Mumbai', '7:55',
                                             '10:00', 'Economy', '26h 05m', '1-stop', 'UK-897']
                    }

        def_idx = ['Airline', 'Cost', 'Date', 'Departure City', 'Arrival City', 'Departure Time',
                   'Arrival Time', 'Class', 'Duration', 'Layover/Stopover', 'Flight ID']

        # set table
        compare_df = pd.DataFrame(def_data)
        compare_df.index = def_idx  # set index
        compare_df.style.set_properties(subset=[' '], **{'width': '100px'})

        # BUILDING A WEBSITE
        st.header("Compare Tickets")  # write a title

        # PART 1) Get user input
        ui_col2, ui_col3 = st.columns(2)

        with st.form("compare_form"):


            with ui_col2:
                ticket_id1 = st.text_input("TICKET ID",
                                           value=1,
                                           max_chars=20,
                                           key="tid1",
                                           help="Please enter the ticket id. You can search it on the Data search page.")

            with ui_col3:
                ticket_id2 = st.text_input("TICKET ID",
                                           value=2,
                                           max_chars=20,
                                           key="tid2",
                                           help="Please enter the ticket id. You can search it on the Data search page.")

        # PART 2) submit form
            sm_col1, sm_col2, sm_col3 = st.columns([1, 1.5, 3])
            invalid_input = 0
            with sm_col1:
                pass
            with sm_col2:
                pass
            with sm_col3:
                submit_button = st.form_submit_button(label="Submit")
                if submit_button:  # function when submit button is turned on
                    # check data input
                    # return 0, if all inputs are valid
                    invalid_input = make_compare_table.get_invalid_input(ticket_id1, ticket_id2)

                    if (not invalid_input):
                        # get new data frame
                        new_data_frame = make_compare_table.get_data_frame(ticket_id1, ticket_id2)

                        # update data frame
                        compare_df = new_data_frame  # update data
                        compare_df.index = def_idx  # set index
                        compare_df.style.set_properties(
                            subset=[' '], **{'width': '100px'})  # set style

            if invalid_input:
                FIRST_TK_INVALID = 1
                SECOND_TK_INVALID = 2
                BOTH_INVALID = -1
                msg_invalid_tk = ""

                # set error message
                if (invalid_input == BOTH_INVALID):
                    msg_invalid_tk += "Both"
                elif (invalid_input == FIRST_TK_INVALID):
                    msg_invalid_tk += "The first"
                elif (invalid_input == SECOND_TK_INVALID):
                    msg_invalid_tk += "The second"

                st.error(msg_invalid_tk +
                         " ticket ID is invalid. Please check again.")

        # PART 3) displaying data
        st.table(compare_df)


        # Footer
    st.markdown("""
    <nav class="navbar fixed-bottom navbar-expand-xl navbar-dark" style="background-color: #234362; border-top-style: solid;">
    <div style="padding-left: 650px; color: #FFFFFF; "> ©All Rights Reserved By STAFLINDA</div>
    </nav>
    """, unsafe_allow_html=True)
