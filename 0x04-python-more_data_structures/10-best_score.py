#!/usr/bin/python3

def best_score(a_dictionary):
    if (a_dictionary is None):
        return None

    score = 0
    # get each key value from dict then multiply its value
    for i in a_dictionary:
        if (a_dictionary[i] > score):
            score = a_dictionary[i]
            winner_name = i
    if (score <= 0):
        return None

    return (winner_name)
