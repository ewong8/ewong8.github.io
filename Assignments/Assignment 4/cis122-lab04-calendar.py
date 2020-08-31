'''
CIS 122 Summer 2020 Lab 4
Author: Ethan Wong
Description Lab 4 Calendar
'''

def get_full_month(n):
    '''
    This function converts an integer into the corresponding
    month of the year.

    Argument:
        n -> integer that represents a month of the year

    Return:
        The month of the year corresponding to the argument
    '''
    month = ""
    if n == 1:
        month = "January"
    elif n == 2:
        month = "February"
    elif n == 3:
        month = "March"
    elif n == 4:
        month = "April"
    elif n == 5:
        month = "May"
    elif n == 6:
        month = "June"
    elif n == 7:
        month = "July"
    elif n == 8:
        month = "August"
    elif n == 9:
        month = "September"
    elif n == 10:
        month = "October"
    elif n == 11:
        month = "November"
    elif n == 12:
        month = "December"
    else:
        month = ""
        print("Must be an integer betwen 1 and 12 " + "(" + str(n) + " is invalid).")
    return month    
# Test
# print(get_full_month(9))
# print(get_full_month(13))
# print(get_full_month(9.4))
      
def test_get_full_month():
    '''
    This function test the get_full_month function with a for loop
    Arguments:
        none
    Return:
        void function -> none
    '''
    for i in range(14):
        print(i, get_full_month(i))
# Test
# test_get_full_month()

def is_leap_year(year):
    '''
    This function determines if a given year is a leap year
    Arguments:
        year -> Should be an integer year
    Return:
        Will return a boolean value (True or False)
    '''
    is_leap = False
    if year % 4 == 0:
        # print("Year is divisible by 4")
        if year % 100 == 0:
            # print("Year is divisible by 100")
            if year % 400 == 0:
                # print("Year is divisible by 400")
                is_leap = True
            else:
                is_leap = False
        else:
            is_leap = True
            
    else:
        is_leap = False
    return is_leap
# Test
# print(is_leap_year(1997))
# print(is_leap_year(2020))

def test_is_leap_year(start_year, end_year):
    '''
    This function tests the is_leap_year function
    Arguments:
        start_year -> should be an integer year
        end_year -> should be an integer year
    Return:
        void function -> none
    '''
    for year in range(start_year, end_year + 1):
        if is_leap_year(year):
            print(year)

# Test
test_is_leap_year(1996, 2112)

import calendar
def validate_is_leap_year(start_year, end_year):
    '''
    This function Uses the calendar module to validate
    the accuracy of the previous is_leap_year function
    Arguments:
        start_year -> should be an integer year
        end_year -> should be an integer year
    Return:
        void function -> none
    '''
    count = 0
    for year in range(start_year, end_year + 1):
        result1 = calendar.isleap(year)
        result2 = is_leap_year(year)
        if result1 != result2:
            print(year)
            count += 1
    if count >= 1:
        print("The number of mismatches is:", count)
    elif count == 0:
        print("No mismatches found")

# Test
validate_is_leap_year(1996, 2112)
    






    
