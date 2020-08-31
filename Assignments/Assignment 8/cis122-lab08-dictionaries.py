'''
CIS 122 Summer 2020 Lab 8
Author: Ethan Wong
Description: Lab 8 - Dictionaries
'''

def pad_string(data, size, direction="left", pad_char=" "):
    data = str(data)
    if len(data) > size:
        result = data
    else:
        pad_size = size - len(data)
        if direction.lower() == "left":
            result = (pad_char * pad_size) + data
        elif direction.lower() == "right":
            result = data + (pad_char * pad_size)

    return result

def get_max_dict_key_size(d):
    '''
    This function returns the max length of a key
    '''
    max_key_length = 0
    for key in d:
        if len(key) > max_key_length:
            max_key_length = len(key)

    return max_key_length

def get_max_dict_value_size(d):
    '''
    This function returns the max length of a value
    '''
    max_value_length = 0
    for key in d:
        elem = d[key]
        if len(elem) > max_value_length:
            max_value_length = len(elem)

    return max_value_length

def create_dictionary(d):
    '''
    This function takes user input to add key:value pairs to a dictionary
    :param d: valid dictionary
    :return: none
    '''
    while True:
        key = input("Enter a key name (empty to exit): ")
        if len(key) == 0:
            break
        value = input("Enter a value: ")
        d[key] = value


def print_dictionary(d):
    '''
    This function prints out the key:value pairs of a dictionary once all modifications have been made
    :param d: valid dictionary
    :return: none
    '''
    # Set base number of dashes underline as length of "key" and "value" headers
    key_dashes = 3
    value_dashes = 5
    max_key_len = get_max_dict_key_size(d) # return max key size
    # print(max_key_len)
    if max_key_len > 3:
        key_dashes = max_key_len # set the number of dashes to the max key length if greater than 3
        # print("Key Dashes", key_dashes)
    max_value_len = get_max_dict_value_size(d) # return max value size
    # print(max_value_len)
    if max_value_len > 5:
        value_dashes = max_value_len # set number of dashes to max value length if greater than 5
        # print("Value dashes", value_dashes)
    pad_size = key_dashes + 2 # pad size is the number of key dashes plus 2
    header = pad_string("Key", pad_size, direction = "right") + "Value" # print column headers
    print(header)
    underline = pad_string("-" * key_dashes, pad_size, direction = "right") + "-" * value_dashes # print underlines
    print(underline)
    for key in d: # Iterate through the dictionary to print key, value pairs
        key_str = pad_string(key, pad_size, direction = "right")
        print(key_str + d[key])

def start():
    '''
    Start function to run the program
    '''
    my_dictionary = {}  # Initialize an empty dictionary to be modified by the program
    create_dictionary(my_dictionary)
    print_dictionary(my_dictionary)
# Test the function
# start()