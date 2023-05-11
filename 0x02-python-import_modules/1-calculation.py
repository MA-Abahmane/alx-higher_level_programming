#!/usr/bin/python3

def simple_calc(a, b):

  # process
  add_result = add(a, b)
  sub_result = sub(a, b)
  mul_result = mul(a, b)
  div_result = div(a, b)

  # output
  print(str(a) + " + " + str(b) + " = " + str(add_result))
  print(str(a) + " - " + str(b) + " = " + str(sub_result))
  print(str(a) + " * " + str(b) + " = " + str(mul_result))
  print(str(a) + " / " + str(b) + " = " + str(div_result))

# if file not run as main; do not run.
if __name__ == '__main__':
  from calculator_1 import add, sub, mul, div
  
  a = 10
  b = 5
  simple_calc(a, b)
