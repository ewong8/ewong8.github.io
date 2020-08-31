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

# Define the main function to accumulate the stats

def word_stats(file_name):
    fin = open(file_name)
    # Initialize counts for all variables:
    word_count = 0
    palindrome_count = 0
    a_count = 0
    b_count = 0
    c_count = 0
    d_count = 0
    e_count = 0
    f_count = 0
    g_count = 0
    h_count = 0
    i_count = 0
    j_count = 0
    k_count = 0
    l_count = 0
    m_count = 0
    n_count = 0
    o_count = 0
    p_count = 0
    q_count = 0
    r_count = 0
    s_count = 0
    t_count = 0
    u_count = 0
    v_count = 0
    w_count = 0
    x_count = 0
    y_count = 0
    z_count = 0
    other_count = 0
    longest = ""
    shortest = "abcdefg"
    # Iterate through lines of file:
    for line in fin:
        word_count += 1
        line = line.strip() # remove excess whitespace
        if len(line) > len(longest):
            longest = line
        if len(line) < len(shortest):
            shortest = line
        if palindrome(line):
            palindrome_count += 1
        if line[0] != "":
            if line[0].lower() == "a":
                a_count += 1
            elif line[0].lower() == "b":
                b_count += 1
            elif line[0].lower() == "c":
                c_count += 1
            elif line[0].lower() == "d":
                d_count += 1
            elif line[0].lower() == "e":
                e_count += 1
            elif line[0].lower() == "f":
                f_count += 1
            elif line[0].lower() == "g":
                g_count += 1
            elif line[0].lower() == "h":
                h_count += 1
            elif line[0].lower() == "i":
                i_count += 1
            elif line[0].lower() == "j":
                j_count += 1
            elif line[0].lower() == "k":
                k_count += 1
            elif line[0].lower() == "l":
                l_count += 1
            elif line[0].lower() == "m":
                m_count += 1
            elif line[0].lower() == "n":
                n_count += 1
            elif line[0].lower() == "o":
                o_count += 1
            elif line[0].lower() == "p":
                p_count += 1
            elif line[0].lower() == "q":
                q_count += 1
            elif line[0].lower() == "r":
                r_count += 1
            elif line[0].lower() == "s":
                s_count += 1
            elif line[0].lower() == "t":
                t_count += 1
            elif line[0].lower() == "u":
                u_count += 1
            elif line[0].lower() == "v":
                v_count += 1
            elif line[0].lower() == "w":
                w_count += 1
            elif line[0].lower() == "x":
                x_count += 1
            elif line[0].lower() == "y":
                y_count += 1
            elif line[0].lower() == "z":
                z_count += 1
            else:
                other_count += 1
    palindrome_pct = round(palindrome_count/word_count * 100, 2)
    a_pct = round(a_count / word_count * 100, 2)
    b_pct = round(b_count / word_count * 100, 2)
    c_pct = round(c_count / word_count * 100, 2)
    d_pct = round(d_count / word_count * 100, 2)
    e_pct = round(e_count / word_count * 100, 2)
    f_pct = round(f_count / word_count * 100, 2)
    g_pct = round(g_count / word_count * 100, 2)
    h_pct = round(h_count / word_count * 100, 2)
    i_pct = round(i_count / word_count * 100, 2)
    j_pct = round(j_count / word_count * 100, 2)
    k_pct = round(k_count / word_count * 100, 2)
    l_pct = round(l_count / word_count * 100, 2)
    m_pct = round(m_count / word_count * 100, 2)
    n_pct = round(n_count / word_count * 100, 2)
    o_pct = round(o_count / word_count * 100, 2)
    p_pct = round(p_count / word_count * 100, 2)
    q_pct = round(q_count / word_count * 100, 2)
    r_pct = round(r_count / word_count * 100, 2)
    s_pct = round(s_count / word_count * 100, 2)
    t_pct = round(t_count / word_count * 100, 2)
    u_pct = round(u_count / word_count * 100, 2)
    v_pct = round(v_count / word_count * 100, 2)
    w_pct = round(w_count / word_count * 100, 2)
    x_pct = round(x_count / word_count * 100, 2)
    y_pct = round(y_count / word_count * 100, 2)
    z_pct = round(z_count / word_count * 100, 2)
    other_pct = round(other_count / word_count * 100, 2)
    print("Count:", word_count)
    print("Longest word is " + longest, "(" + str(len(longest)) + "%)")
    print("Shortest word is " + shortest, "(" + str(len(shortest)) + "%)")
    print("Palindromes:", palindrome_count, "(" + str(palindrome_pct) + "%)")
    print("A:", a_count, "(" + str(a_pct) + "%)")
    print("B:", b_count, "(" + str(b_pct) + "%)")
    print("C:", c_count, "(" + str(c_pct) + "%)")
    print("D:", d_count, "(" + str(d_pct) + "%)")
    print("E:", e_count, "(" + str(e_pct) + "%)")
    print("F:", f_count, "(" + str(f_pct) + "%)")
    print("G:", g_count, "(" + str(g_pct) + "%)")
    print("H:", h_count, "(" + str(h_pct) + "%)")
    print("I:", i_count, "(" + str(i_pct) + "%)")
    print("J:", j_count, "(" + str(j_pct) + "%)")
    print("K:", k_count, "(" + str(k_pct) + "%)")
    print("L:", l_count, "(" + str(l_pct) + "%)")
    print("M:", m_count, "(" + str(m_pct) + "%)")
    print("N:", n_count, "(" + str(n_pct) + "%)")
    print("O:", o_count, "(" + str(o_pct) + "%)")
    print("P:", p_count, "(" + str(p_pct) + "%)")
    print("Q:", q_count, "(" + str(q_pct) + "%)")
    print("R:", r_count, "(" + str(r_pct) + "%)")
    print("S:", s_count, "(" + str(s_pct) + "%)")
    print("T:", t_count, "(" + str(t_pct) + "%)")
    print("U:", u_count, "(" + str(u_pct) + "%)")
    print("V:", v_count, "(" + str(v_pct) + "%)")
    print("W:", w_count, "(" + str(w_pct) + "%)")
    print("X:", x_count, "(" + str(x_pct) + "%)")
    print("Y:", y_count, "(" + str(y_pct) + "%)")
    print("Z:", z_count, "(" + str(z_pct) + "%)")
    print("Other:", other_count, "(" + str(other_pct) + "%)")

# Test the function
word_stats("words_alpha.txt")

























