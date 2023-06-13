#!/usr/bin/python3
from sys import argv

"""
    a script that adds all arguments to a Python list,
    and then save them to a file:
"""

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


""" load list from add_item.json, if list not found; creat empy one """
fileName = "add_item.json"
try:
    list = load_from_json_file(fileName)
except:
    list = []

""" append user arguments to list """
for i in range(1, len(argv)):
    list.append(argv[i])

""" overwrite the files content (update add_item.json) """
save_to_json_file(list, fileName)
