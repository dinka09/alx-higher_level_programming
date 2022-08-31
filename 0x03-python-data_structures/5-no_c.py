#!/usr/bin/python3
def no_c(my_string):
    listsofchar = list(my_string)
    for char in listsofchar:
        if char == 'c' or char == 'C':
            listsofchar.remove(char)
    return("".join(listsofchar))
