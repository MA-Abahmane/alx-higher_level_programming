#!/usr/bin/python3

def best_score(a_dictionary):
    if (a_dictionary == None):
        return None
    
    score = 0
    #get each key/value from dict, then multiply its value
    for i in a_dictionary:
        if (a_dictionary[i] > score):
            score = a_dictionary[i]
            winner_name = i
    
    return (winner_name)
