'''
CIS 122 Summer 2020 Assignment 7
Author: Ethan Wong
Description: Assignment 7 - List manager
'''
# Initialize list variable:
lst = []

def cmd_help():
    '''
    This function displays a manual for this program
    :return:
    '''
    cmds = ["Add", "Delete", "List", "Clear"]
    cmd_descriptions = ["Add to list", "Delete information", "List information", "Clear list"]
    max_length = get_max_list_item_size(cmds)  # Use the get_max_list_item_size function to find the max length of a command
    for i in range(len(cmds)):  # Iterate through the cmd list to print commands and descriptions
        element = cmds[i]
        padded_element = pad_right(element, 5 + max_length)
        print(padded_element, cmd_descriptions[i])
    print("Empty to Exit")

def cmd_add(t):
    '''
    This function adds items to the list
    '''
    while True:
        add_info = input("Enter information (empty to stop): ")
        if len(add_info) > 0:
            t.append(add_info)
            print("Added, item count =", len(t))
        else:
            break

def cmd_delete(t):
    '''
    This function removes individual items from the list
    '''
    for i in range(len(t)):
        padded_index = pad_right(str(i), len(str(i)) + 2)
        print(padded_index, t[i])
    while True:
        delete_input = input("Enter number to delete (empty to stop): ").strip()
        if delete_input.isdigit():
            if not 0 <= int(delete_input) < len(t):
                print("Input must be a valid integer in the range of the list")
            else:
                t.pop(int(delete_input))
                if len(t) == 0:
                    print("All items deleted")
                    break
        else:
            print("Input must be a valid integer in the range of the list")
        for i in range(len(t)):
            padded_index = pad_right(str(i), len(str(i)) + 2)
            print(padded_index, t[i])

def cmd_list(t):
    '''
    This function displays the number of items and each item in the list
    '''
    print("List contains", len(t), "items")
    for element in t:
        print(element)

def cmd_clear(t):
    '''
    This function clears the list of all items
    '''
    print(len(t), "item(s) removed, list empty")
    t.clear()

def get_max_list_item_size(t):
    '''
    This function returns the length of the longest command
    '''
    max_length = 0
    for element in t:
        if len(element) > max_length:
            max_length = len(element)
    return max_length


def pad_string(data, size, pad_char=" ", direction="left"):
    if len(data) > size:
        result = data
    else:
        pad_size = size - len(data)
        if direction.lower() == "left":
            result = (pad_char * pad_size) + data
        elif direction.lower() == "right":
            result = data + (pad_char * pad_size)
    return result

def pad_left(data, size, pad_char=" "):
    result = pad_string(data, size, pad_char, direction="left")
    return result

def pad_right(data, size, pad_char=" "):
    result = pad_string(data, size, pad_char, direction="right")
    return result

while True:
    cmd_input = input("Enter a command (? for help): ").strip()
    if cmd_input == "":  # If the input is blank, exit program
        print("Goodbye")
        break
    elif cmd_input == "?":  # If the input is a question mark, print a list of commands and descriptions
        cmd_help()
    elif cmd_input == "add":
        cmd_add(lst)
        # print(lst)
    elif cmd_input == "list":
        cmd_list(lst)
    elif cmd_input == "clear":
        cmd_clear(lst)
    elif cmd_input == "delete" or "del":
        cmd_delete(lst)

