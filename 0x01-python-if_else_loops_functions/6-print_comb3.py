#!/usr/bin/python3

for x in range(0, 11):
    for y in range(0, 10):
        if ( x == 8 and y == 9 ):
            print( "{0}{1}".format(x ,y) )
        if ( y > x ):
            print( "{0}{1}".format(x ,y), end= ", " )
