#!/usr/bin/python3

x = ord('a')

while (chr(x) != chr( ord('z') + 1 )):
    print("{}".format(chr(x)), end= "")
    x+=1
