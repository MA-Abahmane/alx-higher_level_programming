#!/usr/bin/python3

def safe_print_integer_err(value):

    try:
        print("{:d}".format(value))
    except Exception as ex:
        print(f"Exception: {ex}")
        return (False)
    else:
        return (True)
