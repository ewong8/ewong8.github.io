"""
CIS 122 Summer 2020: Assignment 4
Author: Ethan Wong
Description: Assignment 4 - Converting a number of days and year into a date string format
string
Credits: https://docs.microsoft.com/en-us/office/troubleshoot/excel/determine-a-leap-year
"""
# the is_leap_year function will be used to solve this problem
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

def input_year():
    '''
    This function prompts the user for a year value and converts it to an integer
    Arguments: 
        none
    Return:
        returns the inputed year as an integer
    '''
    year = int(input("Enter a year: "))
    if year <= 0:
        year = 0
    return year
    
def valid_year(year):
    '''
    This function validates that the user inputed year is valid (greater than 0)
    Arguments:
        year -> integer, taken from input_year function
    Returns:
        True/False -> Boolean value depending on validity of year value
    '''   
    if year > 0:
        result = True
    elif year <= 0:
        print("Year must be > 0")
        result = False
    return result

def get_days_in_year(year):
    '''
    This function determines the total number of days in a year
    Arguments:
        year -> integer, taken from input_year function
    Returns:
        days_in_year -> total # of days in a year (leap or normal year)
    '''
    if valid_year(year):
        if is_leap_year(year):
            days_in_year = 366
        else:
            days_in_year = 365
    else:
        days_in_year = 0
    return days_in_year

def valid_day_of_year(year, day_of_year):
    '''
    This function validates if the day of the year inputed by the user is acceptable
    Arguments:
        year -> integer, taken from input_year function
        day_of_year -> integer value between 1 and 365 or 366
    Returns:
        True/False -> Boolean value depending on validity of day of year
        '''
    if day_of_year <= 0:
        print("Day of year must be > 0")
        result = False
    elif day_of_year > get_days_in_year(year) and year > 0:
            print("Day of year must be <=", get_days_in_year(year))
            result = False
    else:
        result = True
        return result

def input_day_of_year(year):
    '''
    This function prompts the user for a day of the year
    Arguments:
        year -> integer, taken from input_year function
    Returns:
        day_of_year -> if this is a valid value, it will be returned
        0 -> if the inputed value is invalid, the function returns 0
    '''
    day_of_year = int(input("Enter a day of the year: "))
    if valid_day_of_year(year, day_of_year):
        result = day_of_year
    else:
        if day_of_year > get_days_in_year(year):
            result = day_of_year
        elif day_of_year <= 0:
            result = 0
    return result

def get_month(year, day_of_year):
    '''
    This function determines the month of the year (in integer form),
    depending on the year and day of year previously entered
    Arguments:
        year -> integer, taken from input_year functino
        day_of_year -> integer between 1 and 365 or 366
    Returns:
        mnth -> integer betwee 1-12, representing a month of the year
        '''
    mnth = 0
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

def valid_month(month):
    '''
    This function validates that the month determined by the previous
    function is correct
    Arguments:
        month -> integer, taken from get_month function
    Returns:
        True/False -> Boolean value depending on validity of month
    '''
    if month <= 0:
        result = False
    elif month > 12:
        result = False
    else:
        result = True
    return result

def translate_month(month):
    '''
    This function translates the integer value for a month into it's string/name form
    Arguments:
        month -> integer between 1-12
    Returns:
        m -> a string representation of the month's name
    '''
    m = ""
    if valid_month(month):
        if month == 1:
            m = "January"
        elif month == 2:
            m = "February"
        elif month == 3:
            m = "March"
        elif month == 4:
            m = "April"
        elif month == 5:
            m = "May"
        elif month == 6:
            m = "June"
        elif month == 7:
            m = "July"
        elif month == 8:
            m = "August"
        elif month == 9:
            m = "September"
        elif month == 10:
            m = "October"
        elif month == 11:
            m = "November"
        elif month == 12:
            m = "December"
    else:
        m = ""
    return m

def get_days_in_month(year, month):
    '''
    This function calculates the total number of days in previous months
    Arguments:
        year -> integer, taken from input_year function
        month -> integer between 1-12, taken from get_month function
    Return:
        total_days -> returns the total days in prior months
        '''
    if valid_year(year) and valid_month(month):
        if is_leap_year(year):
            total_days = 0
            month_arr = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            for i in range(len(month_arr)):
                while i + 1 < month:
                    total_days += month_arr[i]
                    i += 1
                return total_days
        else:
            total_days = 0
            month_arr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            for i in range(len(month_arr)):
                while i + 1 < month:
                    total_days += month_arr[i]
                    i += 1
                return total_days
    else:
        total_days = 0
    return total_days

def valid_day(year, month, day):
    '''
    This function validates that all 3 of the year, month, and day are correct
    Arguments:
        year -> integer, taken from input_year function
        month -> integer between 1-12, taken from get_month function
        day -> integer between 1-365 or 366, taken from input_day_of_year function
    Returns:
        True/False -> Boolean value depending on the validity of the 3 inputs
    '''
    if year > 0 and month > 0 and 0 < day <= get_days_in_year(year):
        result = True
    else:
        result = False
    return result

def get_date_string(year, month, day):
    '''
    This function returns a string representing the year, month, day in m/d/y format
    Arguments:
        year -> integer, taken from input_year function
        month -> integer between 1-12, taken from get_month function
        day -> integer between 1-365 or 366, taken from input_day_of_year function
    Returns:
        result_str -> string in m/d/y format
        '''
    if valid_day(year, month, day):
        day_of_month = day - get_days_in_month(year, month)
        result_str = str(translate_month(month)) + " " + str(day_of_month) + ", " + str(year)
    else:
        result_str = ""
    return result_str

def start():
    '''
    This function encapsulates all code that is needed to convert
    a day and year into a month, day, year string format
    Arguments:
        none
    Returns
        void function -> none
    '''
    yr = input_year()
    d = input_day_of_year(yr)
    m_num = get_month(yr, d)
    valid_params = valid_day(yr, m_num, d)
    if valid_params:
        date_str = get_date_string(yr, m_num, d)
        print(date_str)
    
start()
