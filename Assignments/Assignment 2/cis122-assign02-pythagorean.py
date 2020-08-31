'''
CIS 122 Summer 2020 Assignment 2
Author: Ethan Wong
Description: Defining a function to use the Pythagorean Theorem
References: https://www.rapidtables.com/calc/math/pythagorean-calculator.html;
http://mathforum.org/dr.math/faq/faq.pythagorean.html;
https://docs.python.org/3/library/math.html
'''
# Question 1
# Import Math module
import math
# Calculate the missing side "c"
def calc_side_c(a, b):
    # Use math.sqrt to solve for C (taking sqrt of the sum of sqaures of a & b)
    c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
    # Return the result of c, rounding value to the nearest hundreths
    return round(c, 2)

# Test function
c = calc_side_c(5, 10)
print("c =", c)

# Calculate the missing side a or b
def calc_side_ab(ab, c):
    # Let x be the missing side (a or b) and solve for x using pythagorean theorem
    x = math.sqrt(math.pow(c, 2) - math.pow(ab, 2))
    # Return the result and round to the nearest hundreth
    return round(x, 2)

# Test function
x = calc_side_ab(4, 8)
print("a/b =", x)
