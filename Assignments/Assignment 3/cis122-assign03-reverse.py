'''
CIS 122 Summer 2020 Assigment 3
Author: Ethan Wong
Description: Assignment 3 Reverse
'''
# Question 1
def reverse(str):
    '''
    Write a fruitful function that accepts a string, and returns the string in return order
    Extended summary:
    Args:
        parameter1: str -> user inputs a string that will be reversed

    Returns:
        The function will return the string argument in reverse order
    '''
    # Initialize an empty string
    result_str = ""
    # For loop that interates through the lenght of the string 
    for i in range(1, len(str) + 1):
        char = str[len(str) - i]
        # Concatenate char to the result string
        result_str = result_str + char
    # Create a final output string that will be returned
    final_output = "Original: " + str + "\n" +"Reversed: " + result_str
    # Return the result
    return final_output

# Test
test1 = reverse("When in the Course of human events")
print(test1)

