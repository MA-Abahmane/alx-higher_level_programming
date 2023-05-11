#!/usr/bin/python3

def simple_calc(a, b):

  # process / output
  print(str(a) + " + " + str(b) + " = " + str(add(a, b)))
  print(str(a) + " - " + str(b) + " = " + str(sub(a, b)))
  print(str(a) + " * " + str(b) + " = " + str(mul(a, b)))
  print(str(a) + " / " + str(b) + " = " + str(div(a, b)))

# if file not run as main; do not run.
if __name__ == '__main__':
  from calculator_1 import add, sub, mul, div
  
  a = 10
  b = 5
  simple_calc(a, b)
