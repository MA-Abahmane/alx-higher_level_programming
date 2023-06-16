#!/usr/bin/python3
""" the class Square that inherits from Rectangle: """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square """

    def __str__(self):
        """ class printer """
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}")

    def __init__(self, size, x=0, y=0, id=None):
        """ class constructor """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ size set """
        return (self.width)

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def updater(self, id=None ,size=None, x=None, y=None):
        # Update size
        if (size is not None):
            self.size = size
        # Update x
        if (x is not None):
            self.x = x
        # Update y
        if (y is not None):
            self.y = y
        # Update id
        if (id is not None):
            self.id = id

    def update(self, *args, **kwargs):
        """ 
        assigns an argument to each attribute
        **This method can update variable is 2 ways:
            - args mode (given args)
            - kwargs mode (given kwargs)
        """
        if (args):
            self.updater(*args)
        elif (kwargs):
            self.updater(**kwargs)

    def to_dictionary(self):
        """ return the dictionary representation of a Square """
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}