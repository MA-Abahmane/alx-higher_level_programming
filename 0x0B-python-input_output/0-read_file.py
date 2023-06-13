#!/usr/bin/python3
""" a function that reads a text file (UTF8) and prints it to stdout: """


def read_file(filename=""):
    """ open file and read its content """
    with open(filename) as fl:
        for line in fl:
            print(line, end='')
