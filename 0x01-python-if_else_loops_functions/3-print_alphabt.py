#!/usr/bin/python3

x = ord('a')

while ( chr(x) != chr( ord('z') + 1 ) ):
    if ( chr(x) != chr( ord('q') ) and chr(x) != chr( ord('e') ) ):
        print( chr(x), end= "" )
    
    x+=1
