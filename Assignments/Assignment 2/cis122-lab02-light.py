'''
CIS 122 Summer 2020 Lab 2 Light
Author: Ethan Wong
Credit:
Description: Create a functions that calculate and print
the time it takes for light to travel from the sun to a given planetary object
'''

# Define a function that calculates the average amount of time in seconds that it takes for light to reach the surface of the Earth and Pluto
def avg_light_travel_seconds(distance_miles):
    # Constant for Speed of Light
    speed_of_light = 186282
    # Calculate the number of seconds in the distance input, given the speed of light 
    seconds = distance_miles/speed_of_light
    # Return the result
    return round(seconds, 2)

# Test fruitful function to verify it's accuracy
x = avg_light_travel_seconds(1000000)
print(x)

# Define a function that prints the reuslts for two planetary objects
''' Arguments are the planetary object and the distance (which will be input into
the avg)light_travel_seconds function 
'''
def print_results(planetary_object, distance):
    '''
    Print a string and the variable input for planetary_object
    and call the function that calculates the time it takes for
    light to travel a given distance
    '''
    print("Light travels from the sun to", planetary_object,
          "in an average of", avg_light_travel_seconds(distance), "seconds")

# Test and call the print_results function for Earth and Pluto
print_results("Earth", 9300000)
print_results("Pluto", 3670050000)
    

    
        
    
        

    
