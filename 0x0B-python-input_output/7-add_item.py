#!/usr/bin/python3
from sys import argv
"""access commandline arguments"""
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
"""create object from JSON file"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
"""writes an object to text file, using JSON representation"""


""" load list from add_item.json, if list not found; creat empy one """
fileName = 'add_item.json'
try:
    list = load_from_json_file(fileName)
except Exception:
    list = []

""" append user arguments to list """
for i in range(1, len(argv)):
    list.append(argv[i])

""" overwrite the files content (update add_item.json) """
save_to_json_file(list, fileName)
