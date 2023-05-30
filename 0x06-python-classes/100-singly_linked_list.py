#!/usr/bin/python3
"""The class Node"""


class Node:
    """inside class Square"""

    def __init__(self, data, next_node=None):
        """initialise squares.

        Args:
            data (int): ssquare size.
            next_node (node): given space indexs
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ data property  """
        return (self.__data)

    @data.setter
    def data(self, value): 
        """ data setter """
        if (type(value) != int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """ data property  """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value): 
        """ data setter """
        if (type(value) != Node and value is not None):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

    def my_print(self):
        """ printing function """
        value = self.size

""" The class SinglyLinkedList """


class SinglyLinkedList:
    """ Inside SinglyLinkedList """

    def __init__(self):
        self.head = None
