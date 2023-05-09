#!/usr/bin/python3

def uppercase(str):

    uppered = ""

    for c in str:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            uppered += chr(ord(c) - 32)
        else:
            uppered += c

    print("{0}".format(uppered))
