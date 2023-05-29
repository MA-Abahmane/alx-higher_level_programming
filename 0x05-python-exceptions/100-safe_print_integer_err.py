#!/usr/bin/python3

def safe_print_integer_err(value):
    from sys import atderr
    try:
        print("{:d}".format(value))
    except Exception as error:
        print("Exception: {}".format(error), file=stderr)
        return (False)
    else:
        return (True)
