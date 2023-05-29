#!/usr/bin/python3

def safe_function(fct, *args):
    rzlt = None
    try:
        rzlt = fct(args[0], args[1])
    except Exception as ex:
        print("Exception: {}".format(ex))
        return (rzlt)
    else:
        return (rzlt)
