'''
CIS 122 Summer 2020 Assignment 2
Author: Ethan Wong
Description: Defining a function to calculate travel time based on speed and distance
References: https://www.calculatorsoup.com/calculators/math/speed-distance-time-calculator.php
'''

# Question 3

# Calculate travel time in minutes given the distance in miles and the speed in mph
def calc_travel_time(distance, speed):
    # Find the total amount of time in minutes it takes to travel the distance
    total_minutes = (distance / speed) * 60
    
    # Use integer division operater to calculate the number of hours
    hours = int(total_minutes // 60)
    
    # Find the remaining minutes after subtracting out the hours
    remaining_minutes = int(total_minutes - hours * 60)
    
    # Find the remaining seconds
    remaining_seconds = int(round((total_minutes - hours * 60 - remaining_minutes) * 60, 0))
    
    # Return each of the 3 times variables needed to print a result string
    return hours, remaining_minutes, remaining_seconds

# Test the function for accuracy
print(calc_travel_time(120, 55))

# Output the travel time in hours, minutes, and seconds given the distance and speed
def print_travel_time(distance, speed):
    # Set variable values equal to the respective variables from the previous function
    hours, minutes, seconds = calc_travel_time(distance, speed)
    
    # Make sure tuple values are assigned correctly
    # print(hours, minutes, seconds)
    
    # Print the result string
    print("To travel " + str(distance) + " miles at " + str(speed) + " MPH will take "
          + str(hours) + " hr, " + str(minutes) + " min and " + str(seconds) + " sec")

# Test the function multiple times
print_travel_time(120, 55)
print_travel_time(120, 70)
print_travel_time(5, 25)
print_travel_time(5, 35)
    

