#!/usr/bin/python3

def calc_pro(argc, argv):

  a = int(argv[1])
  oper = argv[2]
  b = int(argv[3])
  
  if (argc == 4):
    if (oper == '+'):
      print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    elif (oper == '-'):
      print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    elif (oper == '*'):
      print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    elif (oper == '/'):
      print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
  else:
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)


        


if __name__ == '__main__':
  import sys
  from calculator_1 import add, sub, mul, div

  argc = len(sys.argv) - 1
  argv = sys.argv

  if (argc == 3):
    calc_pro(argc, argv)
  else:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)
