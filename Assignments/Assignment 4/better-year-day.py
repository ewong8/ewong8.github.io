"""
CIS 122 Summer 2020: Assignment 4
Author: Ethan Wong
Description: Assignment 4 - Converting a number of days and year into a date string format
string
Credits: https://docs.microsoft.com/en-us/office/troubleshoot/excel/determine-a-leap-year
"""

# the is_leap_year function will be used to solve this problem
def is_leap_year(year):
    """
    This function determines if a given year is a leap year
    Arguments:
        year -> Should be an integer year
    Return:
        Will return a boolean value (True or False)
    """
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

# Determine if year input is valid
def valid_year(year):
    """
    This function validates that the user inputed year is valid (greater than 0)
    Arguments:
        year -> integer, taken from input_year function
    Returns:
        True/False -> Boolean value depending on validity of year value
    """
    if year > 0:
        result = True
    elif year <= 0:
        result = False
    return result

# Prompt user to input a year, continue asking for a year if input is invalid
def input_year():
    """
    This function prompts the user for a year value and converts it to an integer
    Arguments:
        none
    Return:
        returns the inputed year as an integer
    """
    year = int(input("Enter a year: "))
    # "Guardian Code"
    while not valid_year(year):  # if user enters invalid number, continue asking for an input
        print("Error: Please enter a valid positive integer")
        year = int(input("Enter a year: "))
    return year

# Determine the number of days in a year, depending on if it is a leap year or not
def get_days_in_year(year):
    """
    This function determines the total number of days in a year
    Arguments:
        year -> integer, taken from input_year function
    Returns:
        days_in_year -> total # of days in a year (leap or normal year)
    """
    if is_leap_year(year):
        days = 366
    else:
        days = 365
    return days

# Determine if the day of year input is valid
def valid_day_of_year(year, day_of_year):
    """
    This function validates if the day of the year inputed by the user is acceptable
    Arguments:
        year -> integer, taken from input_year function
        day_of_year -> integer value between 1 and 365 or 366
    Returns:
        True/False -> Boolean value depending on validity of day of year
        """
    if day_of_year <= 0:
        result = False
    elif day_of_year > get_days_in_year(year):
        result = False
    else:
        result = True
    return result

# Prompt user for day of year input, continue asking for day if input is invalid
def input_day_of_year(year):
    """
    This function prompts the user for a day of the year
    Arguments:
        year -> integer, taken from input_year function
    Returns:
        day_of_year -> if this is a valid value, it will be returned
        0 -> if the inputed value is invalid, the function returns 0
    """
    day_of_year = int(input("Enter a day of the year: "))
    # "Guardian Code"
    while not valid_day_of_year(year, day_of_year): # if user enters invalid number, continue asking for input
        print("Error: Day of the year must be between 1 and", get_days_in_year(year))
        day_of_year = int(input("Enter a day of the year: "))
    return day_of_year

# Calculate the month number based on results from previous year and day of year inputs
def get_month(year, day_of_year):
    """
    This function determines the month of the year (in integer form),
    depending on the year and day of year previously entered
    Arguments:
        year -> integer, taken from input_year functino
        day_of_year -> integer between 1 and 365 or 366
    Returns:
        mnth -> integer betwee 1-12, representing a month of the year
        """
    if is_leap_year(year):
        if day_of_year <= 31:
            mnth = 1
        elif day_of_year <= 60:
            mnth = 2
        elif day_of_year <= 91:
            mnth = 3
        elif day_of_year <= 121:
            mnth = 4
        elif day_of_year <= 152:
            mnth = 5
        elif day_of_year <= 182:
            mnth = 6
        elif day_of_year <= 213:
            mnth = 7
        elif day_of_year <= 244:
            mnth = 8
        elif day_of_year <= 274:
            mnth = 9
        elif day_of_year <= 305:
            mnth = 10
        elif day_of_year <= 335:
            mnth = 11
        elif day_of_year <= 366:
            mnth = 12
    else:
        if day_of_year <= 31:
            mnth = 1
        elif day_of_year <= 59:
            mnth = 2
        elif day_of_year <= 90:
            mnth = 3
        elif day_of_year <= 120:
            mnth = 4
        elif day_of_year <= 151:
            mnth = 5
        elif day_of_year <= 181:
            mnth = 6
        elif day_of_year <= 212:
            mnth = 7
        elif day_of_year <= 243:
            mnth = 8
        elif day_of_year <= 273:
            mnth = 9
        elif day_of_year <= 304:
            mnth = 10
        elif day_of_year <= 334:
            mnth = 11
        elif day_of_year <= 365:
            mnth = 12
    return mnth

# Convert the previous month number into a string containing the month's name
def translate_month(month):
    """
    This function translates the integer value for a month into it's string/name form
    Arguments:
        month -> integer between 1-12
    Returns:
        m -> a string representation of the month's name
    """
    # Create array containing month names, return the correct moth name based on the month number found earlier
    months = ['January', 'February', 'March', 'April', 'May', "June", "July", "August", "September", "October",
              "November", "December"]
    if (month >= 1) and (month <= 12):
        return months[month - 1]
    else:
        return "Error"

# Determine if the month conversion is valid, to be used later
def valid_month(month):
    """
    This function validates that the month determined by the previous
    function is correct
    Arguments:
        month -> integer, taken from get_month function
    Returns:
        True/False -> Boolean value depending on validity of month
    """
    if month <= 0:
        result = False
    elif month > 12:
        result = False
    else:
        result = True
    return result

# Calculate the total number of days in preceeding months, given a year and month paramter, to be used later
def get_days_in_month(year, month):
    """
    This function calculates the total number of days in previous months
    Arguments:
        year -> integer, taken from input_year function
        month -> integer between 1-12, taken from get_month function
    Return:
        total_days -> returns the total days in prior months
        """
    if is_leap_year(year):
        total_days = 0
        # Create an array containing the number of days in each month, for loop iterates through to sum up days in previous months
        month_arr = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for i in range(len(month_arr)):
            while i + 1 < month:
                total_days += month_arr[i]
                i += 1
            return total_days
    else:
        total_days = 0
        # Create an array containing the number of days in each month, for loop iterates through to sum up days in previous months
        month_arr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for i in range(len(month_arr)):
            while i + 1 < month:
                total_days += month_arr[i]
                i += 1
            return total_days

# Uses previous functions that validate year, month, and day to determine validity of all inputs, to be used later
def valid_day(year, month, day):
    """
    This function validates that all 3 of the year, month, and day are correct
    Arguments:
        year -> integer, taken from input_year function
        month -> integer between 1-12, taken from get_month function
        day -> integer between 1-365 or 366, taken from input_day_of_year function
    Returns:
        True/False -> Boolean value depending on the validity of the 3 inputs
    """
    if valid_year(year) and valid_month(month) and valid_day_of_year(year, day):
        result = True
    else:
        result = False
    return result

# Return the finals date string based on year, month, and day inputs
def get_date_string(year, month, day):
    """
    This function returns a string representing the year, month, day in m/d/y format
    Arguments:
        year -> integer, taken from input_year function
        month -> integer between 1-12, taken from get_month function
        day -> integer between 1-365 or 366, taken from input_day_of_year function
    Returns:
        result_str -> string in m/d/y format
    """
    if valid_day(year, month, day):
        day_of_month = day - get_days_in_month(year, month)
        result_str = translate_month(month) + " " + str(day_of_month) + ", " + str(year)
    else:
        result_str = ""
    return result_str

# Encapsulating function that calls for inputs and prints the final string
def start():
    """
    This function encapsulates all code that is needed to convert
    a day and year into a month, day, year string format
    Arguments:
        none
    Returns
        void function -> none
    """
    yr = input_year()                # Create variable that contains value of year input
    d = input_day_of_year(yr)        # Create variable that contains value of day
    m_num = get_month(yr, d)         # calculate the month number based on year and day
    print(get_date_string(yr, m_num, d))   # final output

# Call the start() function
start()

