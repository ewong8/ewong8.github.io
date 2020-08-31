'''
CIS 122 Summer 2020 Assignment 5
Author: Ethan Wong
Description: Assignment 5 Guessing Program
'''

def guessing_game():
    '''
    This function accepts a user inputed word that will be guessed
    Users will then be prompted to guess letters to uncover all letters
    in the original words.
    Parameters :
        none
    Return:
        none
    '''
    # Prompt user for a guess word that will be converted to a string, make all the letters lowercase
    guess_word = str(input("Enter a guess word (blank to quit): ")).lower()
    # print(guess_word)
    if guess_word == "":
        # Quit the program if an empty input is received
        quit("Blank Input - Program Ended")
    else:
        # Create a string containing unique letters of the guess word
        letter_string = ""
        for i in guess_word:
            if i not in letter_string:
                letter_string += i
        # print(letter_string)
        # Create another string that will contain characters guessed by the user
        # and another string to track incorrect guesses
        correct_guesses = ""
        incorrect_guesses = ""
        # Initialize a count to count the number of guesses
        count = 0
        # While the correct guesses do not match the unique
        # letter string
        while len(correct_guesses) != len(letter_string):
            # Prompt user for a letter guess
            letter_guess = str(input("Enter a guess letter (blank to quit): ")).lower()
            # print(letter_guess)
            if letter_guess == "":
                # If input is blank, quit the program
                quit("Blank Input - Program Ended")
            # If the user guess matches a letter in the unique letter_string
            # Add the letter to the guesses string
            elif len(letter_guess) > 1:
                print("> Only enter a single letter")
                count += 1
            elif letter_guess in letter_string:
                # If the letter was already guessed AND found, print status
                if letter_guess in correct_guesses:
                    print(">", letter_guess, "already guessed and found")
                    count += 1
                else:
                    # If it is a correct guess and has not already been guessed,
                    # remove the letter from the letter_string
                    correct_guesses = correct_guesses + letter_guess
                    print(">", letter_guess, "found")
                    count +=1
            # Branch for incorrect guesses
            elif letter_guess not in letter_string:
                # If the guess has already been made, print relevant status
                if letter_guess in incorrect_guesses:
                    print(">", letter_guess, "already guessed and already not found")
                    count +=1
                # If guess is incorrect for the first time, add it to the
                # guesses variable, print according status
                else:
                    incorrect_guesses = incorrect_guesses + letter_guess
                    print(">", letter_guess, "not found")
                    count += 1
            # print(len(correct_guesses) == len(letter_string))
            # Print guesses and guess count
            print("Guesses so far:", correct_guesses + incorrect_guesses)
            print("Number of guesses:", count)
        # Print final results
        print("*** Results ***\n"
              "Word:\t\t" + guess_word + "\n" +
              "Matched:\t" + correct_guesses + "\n" +
              "Unmatched:\t" + incorrect_guesses + "\n" +
              "Guesses:\t" + str(count))

guessing_game()
