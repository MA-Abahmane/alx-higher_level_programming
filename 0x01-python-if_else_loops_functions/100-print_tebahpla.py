#!/usr/bin/python3

count = 0
x = ord('z')
y = ord('Z')

while (count < 26):
    
    if count % 2 == 0:
        print(chr(x), end='')
    if count % 2 != 0:
        print(chr(y), end='')

    count += 1
    x -= 1
    y -= 1
