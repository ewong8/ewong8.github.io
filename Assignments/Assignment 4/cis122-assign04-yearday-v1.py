'''
CIS 122 Summer 2020: Assignment 4
Author: Ethan Wong
Description: Assignment 4 - Converting a number of days and year into a date format
string
'''
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
'''
1) Prompt user for a year and a day of the year (1-365 or 366)
  - use input function
  - inputs will be used for calculations in the final code
  - validate year and day of year
  - use while loop: will continue prompting if input is invalid
'''
year = int(input("Enter a year: "))
while year <=0:
    print("Year must be > 0")
    year = int(input("Enter a year: "))

day_of_year = int(input("Enter a day of the year: "))
if is_leap_year(year):
    while day_of_year <= 0 or day_of_year > 366:
        if day_of_year <= 0:
            print("Day of year must be > 0")
            day_of_year = int(input("Enter a day of the year: "))
        elif day_of_year > 366:
            print("Day must be <= 366")
            day_of_year = int(input("Enter a day of the year: "))
else:
    while day_of_year <= 0 or day_of_year > 365:
        if day_of_year <= 0:
            print("Day of year must be > 0")
            day_of_year = int(input("Enter a day of the year: "))
        elif day_of_year > 365:
            print("Day must be <= 365")
            day_of_year = int(input("Enter a day of the year: "))
            
'''
2) Determine whether the specified year is a leap year with the is_leap_year() function
  - conditional "if" statement should be used
'''
if is_leap_year(year):
    '''
    3) Based on the result of the "if" statement and "day of the year" input,
    calculate the month of the year
        - if day of the year is less than the total number of days after
        a certain month has passed, but greater than the cumulative
        number of days from previous months, that month is correct
    '''
    '''4) Subtract out the number of days in prior months to get the remaining
    number of days in the current months
    '''
    if day_of_year <= 31:
        month = "January"
        day_of_month = day_of_year
    elif day_of_year <= 60:
        month = "February"
        day_of_month = day_of_year - 31
    elif day_of_year <= 91:
        month = "March"
        day_of_month = day_of_year - 60
    elif day_of_year <= 121:
        month = "April"
        day_of_month = day_of_year - 91
    elif day_of_year <= 152:
        month = "May"
        day_of_month = day_of_year - 121
    elif day_of_year <= 182:
        month = "June"
        day_of_month = day_of_year - 152
    elif day_of_year <= 213:
        month = "July"
        day_of_month = day_of_year - 182
    elif day_of_year <= 244:
        month = "August"
        day_of_month = day_of_year - 213
    elif day_of_year <= 274:
        month = "September"
        day_of_month = day_of_year - 244
    elif day_of_year <= 305:
        month = "October"
        day_of_month = day_of_year - 274
    elif day_of_year <= 335:
        month = "November"
        day_of_month = day_of_year - 305
    elif day_of_year <= 366:
        month = "December"
        day_of_month = day_of_year - 335
    '''
    5) Print a string containing the month, day and year
    '''
    date_string = month + " " + str(day_of_month) + ", " + str(year)
    print(date_string)    
    '''
    4) Subtract out the number of days in prior months to get the remaining
    number of days in the current months
    '''
else:
    if day_of_year <= 31:
        month = "January"
        day_of_month = day_of_year
    elif day_of_year <= 59:
        month = "February"
        day_of_month = day_of_year - 31
    elif day_of_year <= 90:
        month = "March"
        day_of_month = day_of_year - 59
    elif day_of_year <= 120:
        month = "April"
        day_of_month = day_of_year - 90
    elif day_of_year <= 151:
        month = "May"
        day_of_month = day_of_year - 120
    elif day_of_year <= 181:
        month = "June"
        day_of_month = day_of_year - 151
    elif day_of_year <= 212:
        month = "July"
        day_of_month = day_of_year - 181
    elif day_of_year <= 243:
        month = "August"
        day_of_month = day_of_year - 212
    elif day_of_year <= 273:
        month = "September"
        day_of_month = day_of_year - 243
    elif day_of_year <= 304:
        month = "October"
        day_of_month = day_of_year - 273
    elif day_of_year <= 334:
        month = "November"
        day_of_month = day_of_year - 304
    else:
        month = "December"
        day_of_month = day_of_year - 334
    '''
    5) Print a string containing the month, day and year
    '''
    date_string = month + " " + str(day_of_month) + ", " + str(year)
    print(date_string)












    
