'''
CIS 122 Summer 2020 Lab 5
Author: Ethan Wong
Credits: https://www.calculatorsoup.com/calculators/discretemathematics/factorials.php
Description: Lab 5 Factorial function
'''

num = int(input("Enter a number: "))
def factorial(num):
    '''
    This function accepts a number and calculates the factorial value
    Parameters:
        num -> should be an integer
    Returns:
        Factorial value of the inputed number
    '''
    # Prompt user to input a value for num
    # If the number is less than zero, return an error
    if num < 0:
        return "Error, number must be >= 0"
    # If the number is 0, return 1
    elif num == 0:
        return 1
    # Branch for all other valid conditions for factorials
    else:
        # Initialize a value to 1
        total = 1
        # Iterate through numbers 1 - num
        for i in range(1, num + 1):
            # Test for loop
            # print(i)
            # multiply the total by the next iterated value
            total = total * i
        # Return the final value
        return total

# Final Tests
print(factorial(num))

# Import math module
import math
def test_factorial(num, show = False):
    '''
    This function tests the above factorial function and compares
    it's value to the math.factorial methods calculations.
    Parameters:
        num -> The number of tests the should be run
        show -> True/False if user wants to see pairs
    Returns:
        none -> void function
    '''
    # Initialize an error count to count mismatches
    error_count = 0
    # Initialize the range to iterate over
    range_num = num + 1
    # Loop over the range
    for i in range(range_num):
        test_result = factorial(i)
        # print(test_result)
        actual_result = math.factorial(i)
        # print(actual_result)
        # If show == True, print the factorial pairs
        if show == True:
            print(str(i) + ": " + str(test_result) + " " + str(actual_result))
        # Use conditional to check if two values are equal
        if test_result != actual_result:
            # increment error count if an mismatch appears
            error_count += 1
            # Print the erroneous value
            print("*", "My value:", test_result, "Method value:", actual_result)
    print("Errors:" + "(" + str(num) + ") " + str(error_count))

# Test
# test_factorial(5, True)
