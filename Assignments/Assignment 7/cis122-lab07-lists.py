'''
CIS 122 Summer 2020 Lab 7
Author: Ethan Wong
Description: Lab 7, working with lists
'''
import random

def gen_random_integer_list(num, start_range = 1, end_range = 100, sort_list = "N"):
    '''
    This function generates a list of random integers and will sort the list, depending on user preference
    Arguments:
        num -> should be an integer
        start_range -> should be an integer, defaults to 1
        end_range -> should be an integer, defaults to 100
        sort_list -> "Y" or "N" indicating whether the list should be sorted, defaults to "N" for no
    Returns:
        t -> the final list of random integers, sorted if asked for
    '''
    # Initialize the list
    t = []
    if num <= 0:
        print("num must be > 0") # If the num argument is less than or equal to zero, print an error statement
    elif not isinstance(start_range, int) or not isinstance(end_range, int):
        # if either the start or end rage is not an integer, print this error statement
        print("start range and end range must be integers")
    else:
        for i in range(num): # iterate through a range from 0 to the num argument
            r = random.randint(start_range, end_range) # generate a random integer between the start and end range
            t.append(r) # append the random number to the list
        if sort_list.upper() == "Y":
            t.sort() # Sort list if specified by the user
    return t # Return the final list

# rand_list = gen_random_integer_list(7, 0, 50, "Y")
# rand_list = gen_random_integer_list(5)
# rand_list = gen_random_integer_list(10, start_range = 0, sort_list = "Y")
# t = gen_random_integer_list(100)

def get_high_score(lst = []):
    '''
    This function accepts an optional list parameter, and will find the highest value in the list
    Arguments:
        lst -> optional list parameter
    Returns:
        high_score -> will be the highest value in the list
    '''
    if not isinstance(lst, list): # Guardian code; if argument is not a list, print error statement and score of -1
        print("List argument expected")
        high_score = -1
    else:
        if lst == []: # If the argument is an empty list, return 0
            high_score = 0
        else: # copy the list, sort the copied version, and return the last element
            copy_list = lst[0:]
            copy_list.sort()
            high_score = copy_list[len(copy_list) - 1]
    # return the overall high score
    return high_score

# high = get_high_score(t)
# print(high)

def get_low_score(lst = []):
    '''
    This function accepts an optional list parameter, and will find the lowest value in the list
    Arguments:
        lst -> optional list parameter
    Returns:
        low_score -> will be the lowest value in the list
    '''
    if not isinstance(lst, list):
        print("List argument expected")
        low_score = -1
    else:
        if lst == []:
            low_score = 0
        else:
            copy_list = lst[0:]
            copy_list.sort()
            low_score = copy_list[0]
    return low_score

# low = get_low_score(t)
# print(low)

def get_mean_score(lst = []):
    '''
    This function accepts an optional list parameter, and will calculate the mean value in the list
    Arguments:
        lst -> optional list parameter
    Returns:
        mean_score -> will be the mean value of the list
    '''
    if not isinstance(lst, list):
        print("List argument expected")
        mean = -1
    else:
        if lst == []:
            mean = 0
        else:
            total = sum(lst)
            mean = round(total / len(lst), 2)

    return mean

# average = get_mean_score(t)
# print(average)

def get_median_score(lst = []):
    '''
    This function accepts an optional list parameter, and will find the mean value of the list
    Arguments:
        lst -> optional list parameter
    Returns:
        median_score -> will be the median value in the list
    '''
    if not isinstance(lst, list):
        print("List argument expected")
        median_score = -1 # return -1 and print error statement if argument is not a list
    else:
        if len(lst) == 0:
            median_score = 0 # If the list is empty, return 0
        elif len(lst) == 1:
            median_score = lst[0] # If the list has 1 element, return that as the median
        elif len(lst) > 0 and len(lst) % 2 == 0: # For lists with an even amount of elements
            lst.sort() # Sort the list, high to low
            halfway = int(len(lst) / 2 - 1) # Find the halfway point, as an index
            mid1 = lst[halfway] # the first middle is at the halfway point
            mid2 = lst[halfway + 1] # the second middle is at one index after the halfway point
            median_score = (mid1 + mid2) / 2 # sum mid1 and mid2, divide by 2
        elif len(lst) % 2 != 0: # For lists with an odd number of elements
            lst.sort() # Sort the list, high to low
            median_score = lst[len(lst) // 2] # use floor division to find the index of the middle number
    return median_score

# median = get_median_score(t)
# print(median)

def count_range(low_score, high_score, lst = []):
    '''
    This function counts the number of scores within a low and high, range
    Arguments:
        lst -> valid list
        low_score -> integer
        high_score -> integer
    Returns:
        count -> the number of scores within the low and high range
    '''
    count = 0 # Initialize the ocunt
    if not isinstance(lst, list): # If the argument is not a list, return -1 and an error statement
        print("List argument expected")
        count = -1
    if not isinstance(low_score, int) or not isinstance(high_score, int):
        print("Low and high must be integers")
        count = -1 # If the low and high arguments are not integeres, return -1 and an error statement
    if low_score >= high_score:
        print("Low must be less than high")
        count = -1 # If the low score is greater or equal to the highscore, return -1 and an error statement
    if len(lst) == 0: # If the list is empty, return -1
        count = -1
    else:
        for score in lst: # Iterate through the list
            if low_score <= score <= high_score:
                count += 1 # Increase the count if the score is between low and high
    return count

# count = count_range(0, 100, t)
# print(count)

def list_range(lst = []):
    '''
    This function accepts a list and counts grades that fall within certain score ranges
    Arguments:
        lst -> valid list, optional parameter
    Returns:
        nothing -> void function that prints
    '''
    # Get counts for each grade, calling the count_range function for each grade range
    a_count = count_range(90, 100, lst)
    b_count = count_range(80, 89, lst)
    c_count = count_range(70, 79, lst)
    d_count = count_range(60, 69, lst)
    f_count = count_range(0, 59, lst)
    # Print results for each grade
    print("A -", a_count)
    print("B -", b_count)
    print("C -", c_count)
    print("D -", d_count)
    print("F -", f_count)
# Final Test
# list_range(t)