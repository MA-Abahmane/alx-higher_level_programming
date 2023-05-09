#!/usr/bin/python3

def print_last_digit(number):
   if (number < 0):
      number *= -1

   last_dig = number % 10

   print("{0}".format(last_dig), end="")
   return (last_dig)
