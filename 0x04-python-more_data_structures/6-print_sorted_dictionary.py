#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    # sort the dictionarys keys then
    # iterate through the dict and print its keys and values
    for i in sorted(a_dictionary):
        print("{:s}: {}".format(i, a_dictionary[i]))
