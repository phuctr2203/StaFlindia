import re #import regex

def valid_ui_bar(user_input):
    #error message 
    INVALID_FORMAT = -1 
    INVALID_DATE = -2

    # get user_input:string and check format is valid or not 
    pattern = '[0-9]{2}\/[0-9]{2}\/[0-9]{4}'
    is_valid_format = re.match(pattern, user_input)
    
    if not is_valid_format:
        return INVALID_FORMAT # error code: format is not valid 
    
    # check scope of data is valid or not 
    is_valid_scope = is_valid_date_scope(user_input)

    if not is_valid_scope:
        return INVALID_DATE # error code: data is out of the scope based on data 
    
    return 1 # it is valid 



def is_valid_date_scope(user_input):
    user_input = user_input.split("/")
    day = int(user_input[0])
    month = int(user_input[1])
    year = int(user_input[2])

    #check month to set proper date scope, assign 1 if montth is even month, else 0
    set_day = 1 if month % 2 == 0 else 0

    #check validation
    if year != 2022:
        return False
    elif month < 3 or 5 < month:
        return False
    elif day < 1 or (31 - set_day) < day:
        return False

    return True 