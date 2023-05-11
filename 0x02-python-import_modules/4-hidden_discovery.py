#!/usr/bin/python3
import hidden_4

def name_finder():
  # getting file names
  names = dir(hidden_4)

  # print the wanted names (not starting with '__')
  for name in names:
    if (name.startswith('__') == False):
      print("{0}".format(name))

# if the file name is set to 'main'; run file
if __name__ == '__main__':
  name_finder()
