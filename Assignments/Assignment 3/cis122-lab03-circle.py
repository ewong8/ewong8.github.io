'''
CIS 122 Summer 2020 Lab 3
Author: Ethan Wong
Description: Lab 3 Circle
'''

# Import turtle graphics module and create a turtle for drawing
import turtle
morla = turtle.Turtle()

# Draw three concentric circles

def move(t, x, y):
    '''
    Move turtle to x, y position
    '''
    t.pu()
    t.goto(x, y)
    t.pd()
    
def draw_circle(t, radius, x, y):
    '''
    Draw a circle of length radius using turtle t, at position x, y
    '''
    move(t, x, y - radius)
    t.circle(radius)


def draw_concentric_circles(t, n_circles, start_radius, gap, x, y):
    '''
    Function draws concentric circles:
        t -> turtle used to draw
        n_circles -> number of circles
        start_radius -> radius of first circle
        gap -> gap between circles
        x, y -> starting coordinates of first circle
        '''
    # Use for loop to draw n_circles
    for i in range(n_circles):
        # Call the draw_circle function 
        draw_circle(t, start_radius, x, y)
        # increment the radius size by the desired gap between circles
        start_radius += gap

# Test
draw_concentric_circles(morla, 4, 70, 15, -100, -100)
        


