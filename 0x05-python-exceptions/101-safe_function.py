#!/usr/bin/python3

def safe_function(fct, *args):
    from sys import stderr as err
    try:
        rzlt = fct(*args)
    except Exception as error:
        print("Exception: {}".format(error), file=err)
        return (None)
    else:
        return (rzlt)
