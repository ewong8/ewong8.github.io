'''
CIS 122 Summer 2020 Lab 2 Square
Author: Ethan Wong
Credit: 
Description: Create a function that returns the square of any positive integer
'''

# Define a function that accepts a number:

def square(num):
    
    # Verify the number is a positive integer (we will not be able to code this step yet)
    # Multiply the number by itself
        result = num * num
        
    # Return the result
        return result

# Test and print results

# Print as tuple
result = square(2), square(10), square(100)
print(result)

# Print with comma inserted strings
print(str(square(2))+ ", " + str(square(10)) + ", " + str(square(100)))
