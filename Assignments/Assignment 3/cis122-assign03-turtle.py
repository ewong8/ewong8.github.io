'''
CIS 122 Summer 2020 Assignment 3
Author: Ethan Wong
Description: Assignment 3 Turtle
'''

# Question 3

import turtle
theo = turtle.Turtle()

# Part A-D
def draw_line(t, x, y, angle, length):
    '''
    This function will use python's turtle module to draw a line
    
    Extended summary:
    The pen will be place up while the turtle moves to the x, y coordinate location.
    Once the turtle has reach the specified location, the turtle will face the specificed angle.
    Then, the pen is placed down and the turtle will move forward at the specified length.
    Finally, the pen will be lifted up. 
        Arguments:
            t (Turtle): the turtle that will be used to draw
            x, y (int/float): Starting coordinates of the line
            angle (int/float): What angle the line will be drawn at
            length (int/float): length of the line
        Returns:
            void function -> no return
    '''
    t.pu()
    t.goto(x, y)
    t.seth(angle)
    t.pd()
    t.fd(length)
    t.pu()

# Tests
# draw_line(theo, 100, 100, 0, 200)
# draw_line(theo, -100, -100, 270, 50)
# draw_line(theo, 200, -200, 45, 75)
    
# Part E-F
def draw_radial_lines(t, x, y, length, num_lines):
    '''
    This function will use python's turtle module to draw radial lines
    
    Extended summary:
    The pen starts in the upward position, and moves to the specified x, y coordinates. Then,
    The angle of the turtle will be set to a certain angle, depending on the number of lines and
    iteration in the for loop. The pen will then be set down and the turtle will move forward
    the specified length. This will be repeated for however many number of lines specified by the
    user.
        Arguments:
            t (Turtle): the turtle that will be used to draw
            x, y (int/float): Starting coordinates of the line
            length (int/float): length of the line
            num_lines(int): number of lines to be drawn
        Returns:
            void function -> no return
    '''
    for i in range(num_lines):
        t.pu()
        t.goto(x, y)
        t.seth((360/num_lines) * i)
        t.pd()
        t.fd(length)

# Tests
# draw_radial_lines(theo, -100, -100, 25, 8)
# draw_radial_lines(theo, -100, 100, 100, 4)
# draw_radial_lines(theo, 100, -100, 200, 16)
#draw_radial_lines(theo, 100, 100, 50, 32)

# Part G
def draw_radials_in_quadrants(t, length, num_lines):
    '''
    This function will draw radial lines in 4 quadrants using the turtle module

    Extended summary:
    The pen will start in the upward position. The turtle will then move to the
    first quadrant location. The pen will then be set down and the turtle will proceed
    to draw the radial lines based on the number of lines and length specified by the user.
    The pen will then be picked up and the turtle will move back to the center of the radial lines.
    After each iteration, the turtle will set it's angle to face the next quadrant and then move
    forward 4 times the length over to the next quadrant and new drawing location. The outer for loop
    will be repeated 4 times to draw radial lines in each of the 4 quadrants.

    Arguments:
        t (turtle): The turtle that will be used to draw lines
        length (int/float): The length of each line drawn
        num_lines (int): The number of lines that will be drawn in each radial set.

    Returns:
        void function -> no return
    '''
    t.pu()
    t.goto(2 * length, 2 * length)
    for j in range(4):
        for i in range(num_lines):
            t.pu()
            t.seth((360/num_lines) * i)
            t.pd()
            t.fd(length)
            t.pu()
            t.bk(length)
        t.pu()
        t.seth(90 * (j + 2))
        t.fd(4 * length)

# Tests
draw_radials_in_quadrants(theo, 75, 8)
draw_radials_in_quadrants(theo, 50, 16)
    










    
