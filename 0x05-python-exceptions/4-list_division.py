#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):

    i = 0
    rzlt = 0
    rzlt_list = []
    for i in range(0, list_length):
        try:
            rzlt = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("out of range")
            rzlt = 0
        except ZeroDivisionError:
            print("division by 0")
            rzlt = 0
        except TypeError:
            print("wrong type")
            rzlt = 0
        finally:
           rzlt_list.append(rzlt)

    return (rzlt_list)
