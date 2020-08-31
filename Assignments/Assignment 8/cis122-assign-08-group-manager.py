'''
CIS 122 Summer 2020 Assignment 8
Author: Ethan Wong
Description: Assignment 8 - Group Manager
'''

group_dict = {} # Empty group variable, type: dictionary

def create_group(d):
    '''
    This function allows the user to create a group and add properties to the group
    :param d: valid dictionary
    :return: modified main dictionary storing groups and properties
    '''
    while True:
        group_name = input("Enter group name (empty to cancel): ").strip()
        if len(group_name) == 0:
            break
        elif group_name in d:
            print("Error: Group name already exists")
        else:
            properties = []
            while True:
                property_name = input("Enter field name (empty to stop): ").strip()
                if len(property_name) == 0:
                    d[group_name] = {'_keys_': properties, '_data_': []}
                    break
                else:
                    properties.append(property_name)

def list_groups(d):
    '''
    This function prints out the groups and associated properties in the main dictionary
    :param d: valid dictionary
    :return: none
    '''
    print("** List of groups **")
    for group in d:
        prop_list = d[group]['_keys_']
        prop_str = ""
        for i in prop_list:
            prop_str += i + ", "
        print(group, ":", len(d[group]['_keys_']), "properties (" + prop_str[0:len(prop_str) - 2] + ")")

def add_group_data(d):
    '''
    This function allows users to add values to properties within groups
    :param d: valid dictionary
    :return: modified dictionary with added values
    '''
    list_groups(d)
    while True:
        group = input("Enter group (empty to cancel): ").strip()
        if len(group) == 0:
            break
        elif group in d:
            d[group]['_data_'].append(dict())
            for key in d[group]['_keys_']:
                # print(key)
                prop_input = input("Enter {}: ".format(key))
                d[group]['_data_'][-1][key] = prop_input
        elif group not in d:
            print("Error: group does not exist")


def list_group_data(d):
    '''
    This function prints out all group data, including group name, properties, and values
    :param d: valid dictionary
    :return: none
    '''
    list_groups(d)
    while True:
        group = input("Enter group name (empty to cancel): ").strip()
        if len(group) == 0:
            break
        elif group in d:
            for d1 in d[group]['_data_']:
                result_str = "{} ".format(d[group]['_data_'].index(d1))
                for prop in d1:
                    result_str += "{} = {}, ".format(prop, d1[prop])
                result_str = result_str[0:len(result_str) - 2]
                print(result_str)
        elif group not in d:
            print("Error: group does not exist")

def display_help():
    '''
    This function displays help: commands and the functionalities
    :return:
    '''
    print("?: list commands")
    print("C: Create a new group")
    print("A: Add data to a group")
    print("G: List groups")
    print("L: List data for a group")
    print("X: Exit")

def input_loop(d):
    '''
    This function takes user input and calls the specified function to perform specific actions
    Arguments:
        d -> valid dictionary
    Returns: modified dictionary specified as the argument
    '''
    # Print welcome message
    print(">> Welcome to Group Manager <<\nThis program creates groups with dynamic properties")
    while True:
        cmd_input = input("Command (empty or X to quit, ? for help): ").strip().upper()
        # Based on user input, perform a specific action/call a function
        if cmd_input == "" or cmd_input == "X":
            break
        elif cmd_input == "?":
            display_help()
        elif cmd_input == "C":
            create_group(d)
        elif cmd_input == "A":
            add_group_data(d)
        elif cmd_input == "G":
            list_groups(d)
        elif cmd_input == "L":
            list_group_data(d)

# Test function
input_loop(group_dict)