#!/usr/bin/python3

for x in range(0, 100):
        if (x == 99):
            print( "{0}". format(x) )
        else:
            print( "{:02d}". format(x), end= ", " )
