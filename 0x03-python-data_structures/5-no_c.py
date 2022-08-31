#!/usr/bin/python3
def no_c(my_string):
    characterslist = list(my_string)
    for char in characterslist:
        if char == 'c' or char == 'C':
            characterslist.remove(char)
    return("".join(characterslist))

