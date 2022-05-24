import streamlit as st

chosen_ch_code = []
chosen_num_code = []
chosen_departure = []
chosen_arrival = []
chosen_date = []
chosen_airlines = []
chosen_class = []
chosen_price = []


def read_date(filename):
    array = []
    my_file = open(filename, 'r')
    for line in my_file:
        words = line.split()
        array.append((words[0]))
    my_file.close()
    return array


def read_airlines(filename):
    array = []
    my_file = open(filename, 'r')
    for line in my_file:
        words = line.split()
        array.append((words[1]))
    my_file.close()
    return array


def read_departure(filename):
    array = []
    my_file = open(filename, 'r')
    for line in my_file:
        words = line.split()
        array.append((words[5]))
    my_file.close()
    return array


def read_arrival(filename):
    array = []
    my_file = open(filename, 'r')
    for line in my_file:
        words = line.split()
        array.append((words[-4]))
    my_file.close()
    return array


def read_price(filename):
    array = []
    my_file = open(filename, 'r')
    for line in my_file:
        words = line.split()
        array.append((words[-3]))
    my_file.close()
    return array


def read_class(filename):
    array = []
    my_file = open(filename, 'r')
    for line in my_file:
        words = line.split()
        array.append((words[-2]))
    my_file.close()
    return array


def read_ch_code(filename):
    array = []
    my_file = open(filename, 'r')
    for line in my_file:
        words = line.split()
        array.append((words[2]))
    my_file.close()
    return array


def read_num_code(filename):
    array = []
    my_file = open(filename, 'r')
    for line in my_file:
        words = line.split()
        array.append((words[3]))
    my_file.close()
    return array


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


def find_index(array1, array2, number_input):
    if number_input in array2:
        chosen_index = array2.index(number_input)
    else:
        array2.append(number_input)
        array2.sort()
        index = array2.index(number_input)
        if index == 0:
            chosen_index = 1
        elif index == (len(array2) - 1):
            chosen_index = index - 1
        else:
            result_1 = abs(number_input - array2[index - 1])
            result_2 = abs(array2[index + 1] - number_input)
            if result_1 < result_2:
                chosen_index = index - 1
            elif result_1 > result_2:
                chosen_index = index + 1
            else:
                chosen_index = index - 1
    chosen_value = array2[chosen_index]
    final_index = array1.index(chosen_value)
    return final_index


def app():
    ch_array = read_ch_code("lib//data//data.txt")
    num_code = read_num_code("lib//data//data.txt")
    date = read_date("lib//data//data.txt")
    airlines = read_airlines("lib//data//data.txt")
    departure = read_departure("lib//data//data.txt")
    arrival = read_arrival("lib//data//data.txt")
    price = read_price("lib//data//data.txt")
    class_of_flight = read_class("lib//data//data.txt")

    st.title("Data Search")
    with st.container():
        st.write("""StaFiIndia offers a search service for a specific flight based on user input."
                    """)
        st.header("Guide")
        st.write("""
                Step 1) Enter your input \n
                Step 2) View the information \n
                """)
    departure_input = st.selectbox("Select your departure", ("Bangalore", "Delhi",
                                                            "Kolkata", "Chennai",
                                                            "Hyderabad", "Mumbai"))
    arrival_input = st.selectbox("Select your arrival", ("Mumbai", "Delhi", "Chennai"))
    class_input = st.selectbox("Select your class", ("economy", "business"))
    price_input = st.slider("Choose the approximately price", min_value=2000, max_value=94000, value=2000, step=1)
    search = st.button("Search", key="option")

    index_keep_final = "" #init

    if search:
        index_keep_1 = [i for i, x in enumerate(departure) if x == departure_input]
        index_keep_2 = [i for i, x in enumerate(arrival) if x == arrival_input]
        index_keep_3 = [i for i, x in enumerate(class_of_flight) if x == class_input]
        index_keep_4 = intersection(index_keep_1, index_keep_2)
        index_keep_final = intersection(index_keep_4, index_keep_3)
    if len(index_keep_final) == 0:
        st.write("Sorry, there is no result for your search, please try again")
    else:
        for i in index_keep_final:
            chosen_ch_code.append(ch_array[i])
            chosen_num_code.append(num_code[i])
            chosen_departure.append(departure[i])
            chosen_arrival.append(arrival[i])
            chosen_date.append(date[i])
            chosen_airlines.append(airlines[i])
            chosen_class.append(class_of_flight[i])
            chosen_price.append(price[i])

        price_int_1 = [int(x) for x in chosen_price]
        price_int_2 = [int(x) for x in chosen_price]
        find_data = find_index(price_int_1, price_int_2, price_input)
        final_ch_code = chosen_ch_code[find_data]
        final_num_code = chosen_num_code[find_data]
        final_departure = chosen_departure[find_data]
        final_arrival = chosen_arrival[find_data]
        final_date = chosen_date[find_data]
        final_airlines = chosen_airlines[find_data]
        final_class = chosen_class[find_data]
        final_price = chosen_price[find_data]

        #display ticket
        st.markdown("""
                        <style>
                            div {
                                box-sizing: border-box;
                                -moz-box-sizing: border-box;
                                -webkit-box-sizing: border-box;
                                color: black;
                                
                            }

                            .container, .topBox, .bottomBox,
                            .flightNumBox, .detailBox, .detailSub,
                            .item1, .item2 {display: flex; }

                            .container, .flightNumBox, .detailBox{flex-direction: column;}
                            
                            .container {
                                        margin: 3% 10%;
                                        height: 200px;
                                        max-width: 200px;
                                        min-width: 900px;
                                        height: 300px;
                                        background-color: #FFFFFF;}
                            
                            .topBox{height: 20%;
                                    margin: 5px 0%;
                                    margin-bottom: 0;}
                            .bottomBox{height: 80%; }

                            .icon{width: 20%;}
                            .airline{width: 80%; text-align: center; font-weight: bolder; font-size: 1.5rem;}

                            .flightNumBox{width: 20%;}
                            .detailBox{width: 75%; padding: 0px 10px;}

                            .title{height:30%; background-color: #FFB039; padding: 0% 25%; text-align: center; font-size: 120%;}
                            .flightCode{height: 70%; padding: 25%; text-align: center; font-size: 200%;}
                            
                            .detailSub {height: 35%;}
                            .top {height: 30%}
                            .item1, .item2 {width: 50%; justify-content: space-between;}
                            .detailTitle, .detailVar {padding:20px;}
                            .detailTitle {font-size: 1.2em; font-weight: 550; width: 60%; font-size: 140%;}
                            .detailVar{width: 35%;}      
                        </style>
                        <body>
                            <div class = "container" style="border: 5px solid black;">
                                <div class = "topBox" style="border-bottom: 3px solid black;">
                                    <div class = "icon" style="padding-left:10px; padding-bottom:10px;"><img src="https://cdn.discordapp.com/attachments/872860802107990116/970964147971952700/transport-airplane-takeoff-icon--android-iconset--icons8-2_1.png" alt=""></div>
                                    <div class = "airline" > """ + str(final_airlines) +""" </div>
                                </div>
                                <div class = "bottomBox">
                                    <div class = "flightNumBox">
                                        <div class = "title" style="border-bottom: 3px solid black; font-weight: bold;">FLIGHT NUMBER</div>
                                        <div class = "flightCode">"""+ str(final_ch_code) + str(final_num_code) + """</div>
                                    </div>
                                    <div class = "detailBox"  style="border-left: 3px solid black;">
                                        <div class = "detailSub top">
                                            <div class = "item1">
                                                <div class = "detailTitle">Date: </div>
                                                <div class = "detailVar">""" + str(final_date) +"""</div>
                                            </div>
                                            <div class = "item2"></div>
                                        </div>
                                        <div class = "detailSub">
                                            <div class = "item1">
                                                <div class = "detailTitle">Arrivial city: </div>
                                                <div class = "detailVar">""" + str(final_arrival) +"""</div>
                                            </div>
                                            <div class = "item2">
                                                <div class = "detailTitle">Departure city: </div>
                                                <div class = "detailVar">""" + str(final_departure) +"""</div>
                                            </div>
                                        </div>
                                        <div class = "detailSub">
                                            <div class = "item1">
                                                <div class = "detailTitle">Cost: </div>
                                                <div class = "detailVar">""" + str(final_price) +"""</div>
                                            </div>
                                            <div class = "item2">
                                                <div class = "detailTitle">Class: </div>
                                                <div class = "detailVar">""" + str(final_class) +"""</div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </body>
                    """, unsafe_allow_html=True)

            # Footer
        st.markdown("""
        <nav class="navbar fixed-bottom navbar-expand-xl navbar-dark" style="background-color: #234362; border-top-style: solid;">
        <div style="padding-left: 650px; color: #FFFFFF; "> ©All Rights Reserved By STAFLINDA</div>
        </nav>
        """, unsafe_allow_html=True)
