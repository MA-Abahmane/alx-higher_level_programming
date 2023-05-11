#!/usr/bin/python3

def main_calc():
	argc = len(sys.argv)
	argv = sys.argv


	if (argc > 1):
  
	  i = 1
	  sum = 0
	  while (i < argc):
	    num = int(argv[i])
	    sum += num
    
	    i += 1

	  print(sum)

	else:
	    print("{0}".format(0))

if __name__ == '__main__':
	import sys  
	main_calc()
