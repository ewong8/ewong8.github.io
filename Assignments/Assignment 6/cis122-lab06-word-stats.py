'''
CIS 14 Summer 4040 Lab 6
Author: Ethan Wong
Description: Lab 6 - accumulate stats on contents of a text file
'''

'''
Program goals:
Count total number of words
Find the longest word, with length
Find shortest word, with length
# of palindroms, with % of total words
First letter counts, # and % of total words
Round percentages with round() function'''

# define a palindrome function to find palindromes:

def palindrome(word):
    """
    This boolean function returns true if
    the string is a palindrome
    """
    if word == word[::-1]:
        return True

def count_first_letter(file_name):
    '''
    This function counts the occurrences of each letter in the alphabet
    Arguments:

        file_name -> should be a file name as string type
    Returns:
        count_list -> list of counts for each letter
    '''
    fin = open(file_name)
    count_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    for line in fin:
        line = line.strip()
        if line[0] not in alphabet:
            count_list[len(count_list)-1] += 1
        else:
            count_list[alphabet.index(line[0])] += 1
    return count_list

def calc_pct(file_name, word_count):
    '''
    This function calculates the percentage of occurrence for each letter in the alphabet
    Arguments:
        file_name -> should be a file name as string type
        word_count -> the total number of words in the file
    Returns:
        pct_list -> list of percentage of the whole for each letter
    '''
    count_list = count_first_letter(file_name)
    pct_list = []
    for count in count_list:
        pct = round((count/word_count) * 100, 2)
        pct_list.append(pct)
    return pct_list

def word_stats(file_name):
    '''
    This is the main function that accumulates all stats desired by the program
    Arguments:
        file_name -> should be a file name as string type
    Returns:
        None -> void function
    '''
    fin = open(file_name)
    # Initialize counts for all variables:
    word_count = 0
    palindrome_count = 0
    longest = ""
    shortest = "abcdefg"
    # Iterate through lines of file to find longest and shortest word, and palindromes
    for line in fin:
        word_count += 1
        line = line.strip() # remove excess whitespace
        if len(line) > len(longest):
            longest = line
        if len(line) < len(shortest):
            shortest = line
        if palindrome(line):
            palindrome_count += 1

    alphabet = "abcdefghijklmnopqrstuvwxyz "
    # retrieve count_list and pct_list from previous function
    count_list = count_first_letter(file_name)
    pct_list = calc_pct(file_name, word_count)
    palindrome_pct = round(palindrome_count/word_count * 100, 2)
    # Print output
    print("Count:", word_count)
    print("Longest word is " + longest, "(" + str(len(longest)) + ")")
    print("Shortest word is " + shortest, "(" + str(len(shortest)) + ")")
    print("Palindromes:", palindrome_count, "(" + str(palindrome_pct) + "%)")
    # Print counts and percentages for each letter of the alphabet, and other
    for i in range(len(alphabet) - 1):
        print("{}:".format(alphabet[i].upper()) , count_list[i], "(" + str(pct_list[i]) + "%)")
    print("Other:", count_list[len(count_list) - 1], "(" + str(pct_list[len(pct_list) - 1]) + "%)")

# Test the function
word_stats("words_alpha.txt")

























