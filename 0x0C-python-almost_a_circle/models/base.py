#!/usr/bin/python3
""" the first class Base: """

import json as js


class Base:
    """ class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ class constructor """
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """ 
            Used to convert a Python dictionary to a JSON string
            return the JSON string representation of list_dictionaries:
        """
        if(list_dictionaries is None):
            return []
        return (js.dumps(list_dictionaries))
    
    @classmethod
    def save_to_file(cls, list_objs):
        """ 
            write the JSON string representation of list_objs to a file
        """
        fl_name = f'{cls.__name__}.json'

        if (list_objs is not None):
            # saving all objects in a list
            list_objs = [obj.to_dictionary() for obj in list_objs]

        with open(fl_name, "w", encoding="utf-8") as fl:
            fl.write(cls.to_json_string(list_objs)) # type: ignore
    
    @staticmethod
    def from_json_string(json_string):
        """ 
            Used to convert from JSON string to Python dictionary:
            return the list of the JSON string representation json_string 
        """
        if (json_string is None or not json_string):
            return []
        return (js.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set: """
        # Importing modules
        from models.rectangle import Rectangle
        from models.square  import Square

        if (cls is not None):
            if (cls is Square):
                dummy = Square(1, 2, 3, 4)
                dummy.update(**dictionary)
            elif (cls is Rectangle):
                dummy = Rectangle(1, 2, 3, 4, 5)
                dummy.update(**dictionary)
            else:
                dummy = None

            return (dummy)
