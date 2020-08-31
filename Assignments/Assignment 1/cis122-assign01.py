'''
CIS 122 Summer 2020 Assignment 1
Author: Ethan Wong
Description: Introduction to programming problem set uses Python numeric data types and 
operations to solve a variety of small problems.
'''

# Question 1
# Calculate the number of red hats and total cost for both red and blue hats
print("*** Question 1: Calculate total hat cost ***")
total_hats = 65                                #5
# Part B bug fix: If total number of hats is odd, round the number of red hats down (buy one more blue than red)
total_red = total_hats // 2                    #8
cost_red = 10                                  #2
total_red_cost = total_red * cost_red          #1
total_blue = total_hats - total_red            #3
cost_blue = 5                                  #4
total_blue_cost = total_blue * cost_blue       #6
total_cost = total_red_cost + total_blue_cost  #7
#print(total_cost)                             #9
print("Total Hat Cost:", total_cost)
print()

#Question 2
print("*** Question 2: Calculate the number of daily steps taken ***")
# Part 1
target_steps = 10000
per_hour = target_steps / 24
per_minute = per_hour / 60
per_second = per_minute / 60
print("Daily steps:", target_steps)
print("Per hour:", per_hour)
print("Per minute:", per_minute)
print("Per second:", per_second)
print()

# Part 2
target_steps = 50000
per_hour = target_steps / 24
per_minute = per_hour / 60
per_second = per_minute / 60
print("Daily steps:", target_steps)
print("Per hour:", per_hour)
print("Per minute:", per_minute)
print("Per second:", per_second)
print()

# Part 3
target_steps = 100000
per_hour = target_steps / 24
per_minute = per_hour / 60
per_second = per_minute / 60
print("Daily steps:", target_steps)
print("Per hour:", per_hour)
print("Per minute:", per_minute)
print("Per second:", per_second)
print()

# Part 4
target_steps = 200000
per_hour = target_steps / 24
per_minute = per_hour / 60
per_second = per_minute / 60
print("Daily steps:", target_steps)
print("Per hour:", per_hour)
print("Per minute:", per_minute)
print("Per second:", per_second)
print()

# Question 3
print("Question 3: Determine how far the person walked during the week")
# circumference = 2 * pi * radius 
radius = 400
# Calculate distance traveled during one inspection
import math # Import the math module to use pi
circumference = 2 * math.pi * radius
systems = 4
inspections = 2
days = 6
# Find the total number of inspections performed per week
weekly_inspections = systems * inspections * days
# Calculate total weekly distance traveled
weekly_distance = circumference * weekly_inspections
print("Weekly distance (ft): ", round(weekly_distance, 2))
print("Weekly distance (miles): ", round((weekly_distance / 5280), 2))
print()





