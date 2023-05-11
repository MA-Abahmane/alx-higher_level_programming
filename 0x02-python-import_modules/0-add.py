#!/usr/bin/python3

def add_ab():
  a = 1
  b = 2
  result = add(a, b)

  print("{0} + {1} = {2}".format(a , b, result))

# if file not run as main; do not run.
if __name__ == '__main__':
  from add_0 import add
  add_ab
