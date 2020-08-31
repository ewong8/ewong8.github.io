'''
CIS 122 Summer 2020 Assignment 3
Author: Ethan Wong
Description Assignment 3 Grid
'''
# Question 2
def draw_grid(number):
    '''
    This function accepts an integer and returns a grid of numbers
    Extended Summary
    Arguments:
        number -> this will be the number that the grid is based on
    Returns:
        A grid of numbers
    '''
    row = ''
    for i in range(1, number + 1):
        for j in range(1, number + 1):
            row = row + " " + str(j)
        row = row + "\n"
    print(row) 

# Tests
draw_grid(2)
draw_grid(4)
draw_grid(10)

            
