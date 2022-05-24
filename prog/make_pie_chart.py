import csv
import math




def draw_piechart(btn_val):
    data, etc_items= get_clean_data_by_btn(btn_val)
    labels = []
    ratio = []

    for k, v in data.items():
        labels.append(k)
        ratio.append(v)

    return labels, ratio, etc_items


def get_clean_data_by_btn(mode):
    DATE = 0
    AIRLINE = 1
    COUNTRY_CODE = 2
    FLIGHT_NUM_CODE = 3
    DEPARTURE_TIME = 4
    DEPARTURE_CITY = 5
    DURATION = 6
    STOPS = 7
    ARRIVAL_TIME = 8
    ARRIVAL_CITY = 9
    COST = 10 
    CLASS = 12

    data = {}
    if mode == "Date":
        data, etc_items = get_basic_dict(DATE)

    elif mode == "Airline":
        data, etc_items = get_basic_dict(AIRLINE)

    elif mode == "Country code":
        data, etc_items = get_basic_dict(COUNTRY_CODE)

    elif mode == "Flight code":
        data, etc_items = get_basic_dict(FLIGHT_NUM_CODE)

    elif mode == "Departure time":
        data, etc_items = get_basic_dict(DEPARTURE_TIME)

    elif mode == "Departure city":
        data, etc_items = get_basic_dict(DEPARTURE_CITY)

    elif mode == "Duration":
        data, etc_items = get_basic_dict(DURATION)

    elif mode == "Stops":
        data, etc_items = get_basic_dict(STOPS)

    elif mode == "Arrival time":
        data, etc_items = get_basic_dict(ARRIVAL_TIME)

    elif mode == "Arrival city":
        data, etc_items = get_basic_dict(ARRIVAL_CITY)

    elif mode == "Cost":
        data, etc_items = get_basic_dict(COST)

    elif mode == "Class":
        data, etc_items = get_basic_dict(CLASS)

    return data, etc_items
    

def get_basic_dict(idx):
    # special idx in csv file
    DATE = 0
    DEPARTURE_TIME = 4
    DURATION = 6
    ARRIVAL_TIME = 8
    COST= 10 # COST = COST_1 + COST_2
 
    dic = {}
    with open("lib//data//compare_data.txt") as dataset:
        reader = csv.reader(dataset, delimiter=',')
        next(reader)  # ignore header

        # make dict
        for row in dataset:
            temp_list = row.split(",")
            row_data = temp_list[idx]

            #get abstract data when special cases: date, duration, cost, time
            if (idx == DATE) or (idx == DEPARTURE_TIME) or (idx == DURATION) or (idx == ARRIVAL_TIME):
                row_data = get_data_sc(row_data, idx)
            elif (idx == COST):
                #clean data 
                row_data = temp_list[idx] + temp_list[idx + 1] #COST = COST_1 + COST_2 #expected format <"nnnn">
                row_data = row_data.replace("\"", "") # remove " character
                row_data = get_data_sc(row_data, idx) 
                
            # check if dic has the key 
            is_key_exist = False
            for key in dic.keys():
                if key == row_data:
                    dic[key] += 1
                    is_key_exist = True
            
            if not is_key_exist:
                #key is not exist 
                #add key to dict 
                dic[row_data] = 1
        dataset.close()

    dic = get_percent_val(dic)
    dic, etc_items = get_major_val(dic)

    return dic, etc_items


def get_data_sc(row_data, mode):
    # row_data = string

    DATE = 0
    DEPARTURE_TIME = 4
    DURATION = 6
    ARRIVAL_TIME = 8
    COST= 10 # COST = COST_1 + COST_2

    #get abstract data for date and duration 
    if mode == DATE :
        row_data = get_abstract_date(row_data)

    elif mode ==  DURATION:
        row_data = get_abstract_duration(row_data)

    elif mode == COST:
        row_data = get_abstract_cost(row_data) 

    elif mode == DEPARTURE_TIME or mode == ARRIVAL_TIME:
        row_data = get_abstract_time(row_data)

    return row_data


def get_abstract_date(row_data):

    if row_data.find("/") != -1: # if row_data contains char "/"
        #if date format is [dd/mm/yyyy]
        row_data = row_data.split("/") # [dd, mm, yyyy]
        row_data = row_data[1] + "/" + format_year(row_data[2]) # "mm/yyyy"

    if row_data.find("-") != -1: # if row_data contains char "-"
        #if date format is [dd-mm-yyyy]
        row_data = row_data.split("-") # [dd, mm, yyyy]
        row_data = row_data[1] + "/" + format_year(row_data[2]) # "mm/yyyy"

    return row_data


def format_year(year):
    year = int(year)
    if(year < 2000):
        year += 2000 #format year #(ex) 22 to 2022

    return str(year)


def get_abstract_duration(row_data):
    row_data = row_data.split(" ") # [(hours)h, (minute)m]
    row_data = row_data[0].replace("h", "") #remove format #expected result [nn]
    row_data = int(row_data)

    if row_data >= 25:
        # duration is equal to or longer than 25 hours
        return "25 hours +"

    elif row_data >= 20:
        # duration is equal to or longer than 20 hours
        return "20 hours +"

    elif row_data >= 15:
        # duration is equal to or longer than 15 hours
        return "15 hours +"

    elif row_data >= 10:
        # duration is equal to or longer than 10 hours
        return "10 hours +"

    elif row_data >= 5:
        # duration is equal to or longer than 5 hours
        return "5 hours +"

    elif row_data >= 3:
        # duration is equal to or longer than 3 hours
        return "3 hours +"

    # duration is less than 3 hours
    return "Less than 3 hours"

def get_abstract_cost(row_data):
    #if data is smaller than 10000, return 10000
    #otherwise, return number by 10000 units
    UNIT = 10000
    if int(row_data) <= UNIT:
        return str(UNIT)
    
    else:
        row_data = int(row_data) / UNIT
        row_data = math.trunc(row_data)
        row_data = row_data * UNIT 
        return str(row_data)


def get_abstract_time(row_data):
    #Parts of the day
    #05:00 ~ 11:59 == "Morning"
    #12:00 ~ 16:59 == "Afternoon"
    #17:00 ~ 20:59 == "Evening"
    #21:00 ~ 04:59 == "Night"

    row_data = row_data.split(":") # hh:mm
    row_data = int(row_data[0]) # get hour value as integer

    if 5 <= row_data and row_data <= 11:
        return "Morning"

    elif 12 <= row_data and row_data <= 16:
        return "Afternoon"

    elif 17 <= row_data and row_data <= 20:
        return "Evening"

    elif (20 <= row_data and row_data <= 24) or (0 <= row_data and row_data <= 4):
        return "Night"


def get_percent_val(dic):
    # change value in dict as percentage
    # get total value 
    total = 0

    for v in dic.values():
        total += v

    for k in dic.keys():
        num = (dic[k] / total) * 100
        dic[k] = round(num , 2) # round float

    return dic


def get_major_val(dic):
    min_val = 5.0
    # merge value if it is less than min_val %

    etc_items = {} # key which has value is less than min_val %

    for k in dic.keys():
        if dic[k] <= min_val:
            etc_items[k] = dic[k] # add key and value if value is less than min_val %

    if len(etc_items) <= 1:
        return dic, etc_items

    # at least 2 items have a value which is less than min_val%
    dic["etc"] = 0 # add key "etc"

    for k in etc_items.keys():
        dic["etc"] += etc_items[k] # add value in dict, the key is 'etc' 
        del dic[k]     # remove original key and its value in dict



    return dic, etc_items