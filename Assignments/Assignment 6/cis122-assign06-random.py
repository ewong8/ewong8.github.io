'''
CIS 122 Summer 2020 Assignment 6
Author: Ethan Wong
Description: Read a file of numbers and calculate sum, count, and average
'''
from cis122_assign06_shared import pad_left, pad_right
import os
while True:
    file_name = input("Enter filename (blank to exit): ").strip()
    if file_name == "":
        # print("Program Exited")
        break

    elif not os.path.exists(file_name):
        print("Invalid file name:", file_name)

    else:
        fin = open(file_name) #open the file
        sum = 0 # initialize sum and counts to 0
        num_count = 0
        comment_count = 0
        # iterate through each line in the file
        for line in fin:
            line = line.strip() # remove excess whitespace
            if line[0] == "#": # if the line contains/begins with a comment, increase counter
                comment_count += 1
            else: # If the line contains a number, increase num_count and add the current number to the running sum
                num_count += 1
                current = int(line)
                sum += current

        fin.close()
        avg = round((sum / num_count), 2)
        label_spacing = 10
        num_spacing = 10
        print(pad_right("Count:", label_spacing), pad_left(str(num_count), num_spacing))
        print(pad_right("Comments:", label_spacing), pad_left(str(comment_count), num_spacing))
        print(pad_right("Total:", label_spacing), pad_left(str(sum), num_spacing))
        print(pad_right("Average:", label_spacing), pad_left(str(avg), num_spacing))

