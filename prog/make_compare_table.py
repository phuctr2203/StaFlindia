from ast import Try
import csv
import pandas as pd


def get_data_frame(ticket_id1, ticket_id2):
    # remove spaces
    ticket_id1 = remove_spaces(ticket_id1)
    ticket_id2 = remove_spaces(ticket_id2)

    # index from csv
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
    COST_1 = 10
    COST_2 = 11
    CLASS = 12
    TICKET_ID = 13

    with open("lib//data//compare_data.txt") as dataset:
        reader = csv.reader(dataset, delimiter=',')
        next(reader)  # ignore header
        raw_tk1 = []  # raw ticket1 info on csv
        raw_tk2 = []  # raw ticket2 info on csv

        # search information
        for row in dataset:
            if len(raw_tk1) != 0 and len(raw_tk2) != 0:
                break  # breask after finding two tickets info

            temp_list = row.split(",")

            if int(temp_list[TICKET_ID]) == int(ticket_id1):
                raw_tk1 = temp_list  # get ticket1 info from cvs file
            elif int(temp_list[TICKET_ID]) == int(ticket_id2):
                raw_tk2 = temp_list  # get ticket2 info from cvs file

        # close file
        dataset.close()

    tk1_flightID = raw_tk1[COUNTRY_CODE] + "-" + raw_tk1[FLIGHT_NUM_CODE]
    tk2_flightID = raw_tk2[COUNTRY_CODE] + "-" + raw_tk2[FLIGHT_NUM_CODE]
    tk1_cost = raw_tk1[COST_1].replace(
        "\"", "") + "," + raw_tk1[COST_2].replace("\"", "")
    tk2_cost = raw_tk2[COST_1].replace(
        "\"", "") + "," + raw_tk2[COST_2].replace("\"", "")

    new_data_dict = {raw_tk1[TICKET_ID]: [raw_tk1[AIRLINE], tk1_cost, raw_tk1[DATE],
                                          raw_tk1[DEPARTURE_CITY], raw_tk1[ARRIVAL_CITY], raw_tk1[DEPARTURE_TIME],
                                          raw_tk1[ARRIVAL_TIME], raw_tk1[CLASS], raw_tk1[DURATION], raw_tk1[STOPS], tk1_flightID],

                     raw_tk2[TICKET_ID]: [raw_tk2[AIRLINE], tk2_cost, raw_tk2[DATE],
                                          raw_tk2[DEPARTURE_CITY], raw_tk2[ARRIVAL_CITY], raw_tk2[DEPARTURE_TIME],
                                          raw_tk2[ARRIVAL_TIME], raw_tk2[CLASS], raw_tk2[DURATION], raw_tk2[STOPS], tk2_flightID]
                     }

    return pd.DataFrame(new_data_dict)


def remove_spaces(str):
    # remove space
    str.strip()
    res = ""

    # remove spaces between chars
    for i in range(len(str)):
        if str[i] == " ":
            continue
        res += str[i]

    return res

def is_valid_ticket_idx(ticket_id):
    try:
        num_of_items = get_num_of_items()
        temp = int(ticket_id)

        if (0 <= temp and temp <= num_of_items):
            return True
    except Exception as e:
        return False



def get_num_of_items():
    num_of_items = 0
    HEADER = 1
    with open("lib//data//compare_data.txt") as dataset:
        for row in dataset:
            if row != "":
                num_of_items += 1

    dataset.close()

    return num_of_items - HEADER


def is_valid_ticket(ticket_str):
    if ((not ticket_str.isnumeric() or not is_valid_ticket_idx(ticket_str))):
        return False

    return True


def get_invalid_input(ticket_id1, ticket_id2):
    ALL_VALID = 0
    FIRST_TK_INVALID = 1
    SECOND_TK_INVALID = 2
    BOTH_INVALID = -1

    # remove space
    ticket_id1 = remove_spaces(ticket_id1)
    ticket_id2 = remove_spaces(ticket_id2)

    # return invalid ticket id
    if (not is_valid_ticket(ticket_id1)) and (not is_valid_ticket(ticket_id2)):
        return BOTH_INVALID

    elif not is_valid_ticket(ticket_id1):
        return FIRST_TK_INVALID

    elif not is_valid_ticket(ticket_id2):
        return SECOND_TK_INVALID

    return ALL_VALID
