'''
CIS 122 Summer 2020 Assignment 2
Author: Ethan Wong
Description: Defining functions to calculate the amount of cement used and print results
References: https://www.concretenetwork.com/concrete/howmuch/calculator.htm;
https://www.todayshomeowner.com/cubic-yard-calculator/
'''

# Question 2
# import math module
import math
# Define the first function that calculates the amount of cement used
''' Return cement amount in yards using cubic inches given
thickness (t), width (w) and length (l) in inches
'''

def calc_yards_cement(t, w, l):
    # Convert dimensions to yards
    t_yards = t / 36
    w_yards = w / 3
    l_yards = l / 3
    # Calculate cubic yardage of cement used
    cubic_yards = t_yards * w_yards * l_yards
    # Return the result of cubic_yards
    return round(cubic_yards, 2)

# Test the first function for accuracy
print(calc_yards_cement(4, 5, 10))

# Define a second functions to print the results
''' Output (print) results of calculating yards given
thickness (t), width (w) and length (l) in inches
'''

def print_results(t, w, l):
    # Call the first function that calculates the amount of cement)
    volume = calc_yards_cement(t, w, l)
    # Print the resulting string with results
    print("A cement slab that is " + str(t) + '" thick, ' + str(w * 12) + '" wide, and ' +
          str(l * 12) + '" long requires', volume, "yards of cement")

# Call the function for each slab
print_results(4, 5, 10)
print_results(4, 20, 20)
