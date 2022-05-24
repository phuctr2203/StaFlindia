import streamlit as st


def app():

    # apply css file
    with open('lib//style//homepage.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


    with st.container():
        #Website
        #Part 0) Introduction 
        with st.container():
            st.title("Welcome to StaFiIndia")
            st.image("lib/img/welcome.jpg"  )
            st.write("""
            Hello, welcome to StaFiIndia. Our company focuses on data visualization of the India local flight ticket information. 
            The company provides data in various ways such as graphs, tables and charts and the user is allowed to take granular control 
            to acquire specific data that the user desired. 
            You can also search the data and compare two data. Feel free to enjoy our services and contact us if you need any help.
            """)

        st.markdown("""
                <body>
                    <div class = "empty" style="padding: 50px;">
                    </div>
                </body>
        """, unsafe_allow_html=True)


        st.title("1. DATA VISUALIZATION")
        #Part 1-1) EXPLAIN EACH CHART
        with st.container():        
            # TABLE
            chart1_col1, chart1_col2 = st.columns(2)
            with chart1_col1:
                st.title("1) Table")
                st.image("https://scontent.fsgn13-1.fna.fbcdn.net/v/t1.15752-9/279376534_566833528012167_1745783498800769969_n.png?_nc_cat=107&ccb=1-5&_nc_sid=ae9488&_nc_ohc=doGDvopum8gAX8_seOU&_nc_ht=scontent.fsgn13-1.fna&oh=03_AVIP60MQ8WFFxJO1Uylrf1ZiueQEmTmlVNtfD5tFy8lUwQ&oe=6292E5E6" , caption = "Table")


            with chart1_col2:
                st.header("What data does staFiIdia show?")
                st.write("StaFlinda’s Table shows the whole data of flights.", 
                        styles= {"text-align": "justify"})
                
                st.header("What are things that you can control?")
                st.write("""Which information you want to view.""" , 
                            styles= {"text-align": "justify"})
                
                st.header("Guide")
                st.write("""
                        Filters\n
                        Step 1) Click on Filters function \n
                        Step 2) Choose a column that you want to sort\n
                        Step 3) Tick the boxes that contain the data\n
                        Step 4) Check the table and see the result\n\n
                        Columns\n
                        Step 1) Click on Columns function\n
                        Step 2) Tick the boxes to hide or show the columns\n
                        Step 3) Check the table and see the result\n
                                                """, styles= {"text-align": "justify"})
                                
            st.markdown("""
                    <body>
                        <div class = "empty" style="padding: 50px;">
                        </div>
                    </body>
            """, unsafe_allow_html=True)


            # BAR CHART
            chart2_col1, chart2_col2 = st.columns(2)

            
            with chart2_col1:
                st.title("2) Bar chart")
                st.header("What data does staFiIdia show?")
                st.write("StaFlinda shows the number of flights which are divided into \"Business\" and \"Economy\" classes by each airline agency.", 
                        styles= {"text-align": "justify"})
                
                st.header("What are things that you can control?")
                st.write("""You can enter the date. The input date from users should be in the valid format dd/mm/yyyy (ex: 04/03/2022).""" , 
                            styles= {"text-align": "justify"})
                
                st.header("Guide")
                st.write("""
                        Step 1) Please enter the valid date in the text box.\n
                        Step 2) Check the number of flights from the shifted chart.\n
                        """, styles= {"text-align": "justify"})
                                
                

            with chart2_col2:
                st.image("https://cdn.discordapp.com/attachments/872860802107990116/972010958769766410/Number_of_flight.PNG",caption = "Bar chart")
            
            st.markdown("""
                    <body>
                        <div class = "empty" style="padding: 50px;">
                        </div>
                    </body>
            """, unsafe_allow_html=True)

            # PIE CHART
            chart3_col1, chart3_col2 = st.columns(2)

            
            with chart3_col1:
                st.title("3) Pie chart")
                st.image("https://cdn.discordapp.com/attachments/872860802107990116/972010827915878440/Pie_chart.PNG",caption = "Pie chart")

            with chart3_col2:
                st.header("What data does staFiIdia show?")
                st.write("StaFiIndia provides more than ten pie charts by each data type so that you can acquire the data you want.", 
                        styles= {"text-align": "justify"})
                
                st.header("What are things that you can control?")
                st.write("""You can select one data type. 
                            Provided data types are 'Date', 'Airline', 'Country code', 'Departure time', 
                            'Departure city', 'Duration','Stops', 'Arrival time', 'Arrival city', 'Cost' and 'Class'.""" , 
                            styles= {"text-align": "justify"})
                
                st.header("Guide")
                st.write("""
                        Step 1) Please choose one of the data types on the select box.\n
                        Step 2) Check out a beautiful pie chart StaFiIndia provides.\n
                        Step 3) More details will be provided when selecting some data types, for example, departure time and arrival time.\n
                        """, styles= {"text-align": "justify"})

            st.markdown("""
                    <body>
                        <div class = "empty" style="padding: 50px;">
                        </div>
                    </body>
            """, unsafe_allow_html=True)


            # PLOT CHART
            chart4_col1, chart4_col2 = st.columns(2)

            
            with chart4_col1:
                st.title("4) Plot chart")
                st.header("What data does staFiIdia show?")
                st.write("Our plot chart provides a graphical representation about the relationship between the price and departure time.", 
                        styles= {"text-align": "justify"})
                
                st.header("What are things that you can control?")
                st.write("""You can select any airline that you wish to have the price analysed.""" , 
                            styles= {"text-align": "justify"})
                
                st.header("Guide")
                st.write("""
                        Step 1) Please select an airline in the selection options. \n
                        Step 2) Checkout the plot chart that StaFildia provides. \n
                        """, styles= {"text-align": "justify"})
                                

            with chart4_col2:
                st.image("https://cdn.discordapp.com/attachments/872860802107990116/970884752187994122/plot.PNG",caption = "Plot")


            st.markdown("""
                    <body>
                        <div class = "empty" style="padding: 50px;">
                        </div>
                    </body>
            """, unsafe_allow_html=True)                

            # MAP
            chart5_col1, chart5_col2 = st.columns(2)

           
            with chart5_col1:
                st.title("5) Map")
                st.image("https://cdn.discordapp.com/attachments/872860802107990116/970885256729231380/unknown.png",caption = "Map")

            with chart5_col2:
                st.header("What data does staFiIdia show?")
                st.write("StaFiIndia provides the location of departure locations and arrival locations on a map with real coordinates ", 
                        styles= {"text-align": "justify"})
                
                st.header("What are things that you can control?")
                st.write("""The map, the zoom of the map'.""" , 
                            styles= {"text-align": "justify"})
                
                st.header("Guide")
                st.write("""
                        Step 1) Choose the class of flight you want to view \n
                        Step 2) Click on the marker to view extra information \n
                        """, styles= {"text-align": "justify"})
                                

            st.markdown("""
                    <body>
                        <div class = "empty" style="padding: 80px;">
                        </div>
                    </body>
            """, unsafe_allow_html=True)


        #Part 1-2) EXPLAIN DATA SEARCH PAGE

            
            with st.container():
                st.title("2. DATA SEARCH")
                st.image("https://cdn.discordapp.com/attachments/872860802107990116/970959338598432778/unknown.png",caption = "Data search")

            with st.container():
                st.header("What data does staFiIdia show?")
                st.write("StaFiIndia offers a search service for a specific flight based on user input.", 
                        styles= {"text-align": "justify"})
                
                st.header("What are things that you can control?")
                st.write("""You can select various data. 
                            Provided data are departure city, arrival city, class and approximately price """ , 
                            styles= {"text-align": "justify"})
                
                st.header("Guide")
                st.write("""
                        Step 1) Enter your input \n
                        Step 2) View the information \n
                        """, styles= {"text-align": "justify"})


            st.markdown("""
                    <body>
                        <div class = "empty" style="padding: 50px;">
                        </div>
                    </body>
            """, unsafe_allow_html=True)


        #Part 1-3) EXPLAIN DATA COMPARE PAGE

            
            with st.container():
                st.title("3. DATA COMPARISON")
                st.image("https://cdn.discordapp.com/attachments/872860802107990116/970948034500362250/unknown.png",caption = "Data comparision")

            with st.container():
                st.header("What data does staFiIdia show?")
                st.write("StaFiIdia provides a data comparison service for two tickets' information. It enables users to see details of the ticket and compare two tickets by each element.", 
                        styles= {"text-align": "justify"})
                
                st.header("What are things that you can control?")
                st.write("""You can put the ticket id into the input box. 
                            Considering the data our company provides, the valid ticket id is from 1 to 500.
                            You can search for a ticket id on the 'table' page.""" , 
                            styles= {"text-align": "justify"})
                
                st.header("Guide")
                st.write("""
                        Step 1) Put the first ticket id and the second ticket id on the input box.\n
                        Step 2) Click the submit button.\n
                        Step 3) See the result.\n
                        """, styles= {"text-align": "justify"})

            st.markdown("""
                    <body>
                        <div class = "empty" style="padding: 8px;">
                        </div>
                    </body>
            """, unsafe_allow_html=True)



        #Part 1-3) EXPLAIN DATA PREDICTION PAGE

            
            with st.container():
                st.title("4. DATA PREDICTION")
                st.image("lib//img//data_prediction.jpg",caption = "Data prediction")

            with st.container():
                st.header("What data does staFiIdia show?")
                st.write("StaFiIndia provides price prediction based on your input", 
                        styles= {"text-align": "justify"})
                
                st.header("What are things that you can control?")
                st.write("""You can select various data. 
                            Provided data are class, source city, arriaval city, airline, stops and days left to flight.""" , 
                            styles= {"text-align": "justify"})
                
                st.header("Guide")
                st.write("""
                        Step 1) Input the information \n
                        Step 2) The price prediction will display below \n
                        """, styles= {"text-align": "justify"})

            st.markdown("""
                    <body>
                        <div class = "empty" style="padding: 8px;">
                        </div>
                    </body>
            """, unsafe_allow_html=True)

   
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
