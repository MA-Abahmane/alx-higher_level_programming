#!/usr/bin/python3

def islower(c):
   
    x = ord('a')
    if (type(c) == int or c == ''):
        print("Traceback (most recent call last):")
    
    while (chr(x) != chr(ord('z') + 1)):
        if (chr(x) == c):
            return True
        x += 1

    return False
