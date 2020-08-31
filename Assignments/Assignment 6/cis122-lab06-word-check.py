'''
CIS 122 Summer 2020 Lab 6
Author: Ethan Wong
Description: Lab 6 - Search for a word in a text file
'''
# Loop until nothing entered
while True:
    # Prompt for input
    word = input("Enter a search word: ")
    word = word.strip() # remove excess whitespace
    if len(word) == 0:
        break # Exit if nothing entered
    else:
        result = False
        # open the file object
        fin = open("words_alpha.txt")
        # iterate through each line
        for line in fin:
            line = line.strip() # remove excess whitespace from lines
            if line.lower() == word.lower():
                # perform matching search on line; result = True if the line matches search word
                result = True
                break
        fin.close() # close the file
        # Print results:
        if result:
            print("Word " + word + "found")
        else:
            print("Word " + word + " not found")




