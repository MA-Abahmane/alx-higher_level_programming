#!/usr/bin/python3

def safe_print_integer_err(value):
    from sys import stderr as err
    try:
        print("{:d}".format(value))
    except Exception as error:
        print("Exception: {}".format(error), file=err)
        return (False)
    else:
        return (True)
