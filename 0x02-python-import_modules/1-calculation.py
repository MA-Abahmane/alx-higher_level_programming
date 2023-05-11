#!/usr/bin/python3

def simple_calc(a, b):

  # process / output
  print('%d + %d = %d' % (a, b, add(a, b)))
  print('%d - %d = %d' % (a, b, sub(a, b)))
  print('%d * %d = %d' % (a, b, mul(a, b)))
  print('%d / %d = %d' % (a, b, div(a, b)))

# if file not run as main; do not run.
if __name__ == '__main__':
  from calculator_1 import add, sub, mul, div
  
  a = 10
  b = 5
  simple_calc(a, b)
