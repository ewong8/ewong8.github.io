'''
CIS 122 Summer 2020 Assignment 6
Author: Ethan Wong
Description: Create padding functions that will be used as a module in another file
'''

def pad_string(data, size, pad_char=" ", direction="left", ):
    if len(data) > size:
        result = data
    else:
        pad_size = size - len(data)
        if direction.lower() == "left":
            result = (pad_char * pad_size) + data
        elif direction.lower() == "right":
            result = data + (pad_char * pad_size)
    return result

# print(pad_string("abc", 10))
def pad_left(data, size, pad_char=" "):
    result = pad_string(data, size, pad_char, direction="left")
    return result

# print(pad_left("abc", 10))

def pad_right(data, size, pad_char=" "):
    result = pad_string(data, size, pad_char, direction="right")
    return result

# print(pad_right("abc", 10, "$"))



