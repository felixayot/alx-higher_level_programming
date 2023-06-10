#!/usr/bin/python3
def no_c(my_string):
    cpy = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(cpy))
