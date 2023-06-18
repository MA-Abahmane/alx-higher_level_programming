#!/usr/bin/python3
""" the first class Base: """

import csv
import json as js
from os import path


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

    @classmethod
    def load_from_file(cls):
        """ 
            Used to load string from file and dejonsify
            return a list of instances 
        """
        Fname = f"{cls.__name__}.json"
        strn = []

        # check is file exists
        if (not path.isfile(Fname)):
            return (strn)
        
        # reading, updating, dejonsify and saving file content
        with open(Fname, 'r', encoding='utf-8') as fl:

            for l in cls.from_json_string(fl.read()):
                strn.append(cls.create(**l))

        return (strn)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ 
            Used to set all objects of a given instance
            and save in a list that is in a row of a csv file
            serializes in CSV:
        """
        from models.square import Square
        from models.rectangle import Rectangle

        Fname = f'{cls.__name__}.csv'

        # setting object tribute values
        if (list_objs is not None):
            if (cls is Square):
                list_objs = [[obj.id, obj.size, obj.x, obj.y]
                            for obj in list_objs]

            else:
                list_objs = [[obj.id, obj.width, obj.height, obj.x, obj.y]
                            for obj in list_objs]

        # writhing to csv file
        with open(Fname, 'w', newline='', encoding='utf-8') as fl:
            wt = csv.writer(fl)
            # each object list should be saved in a row 
            wt.writerows(list_objs)


    @classmethod
    def load_from_file_csv(cls):
        """ 
            Now we read from the csv file each value,
            convert each to an intiger and set the values to the
            instance attributes and save all in a dictionary
            deserializes in CSV:
        """
        from models.square import Square
        from models.rectangle import Rectangle

        Fname = f'{cls.__name__}.csv'
        Finfo = []

        # read from csv file
        with open(Fname, 'r', newline='', encoding='utf-8') as fl: # type: ignore
            # read the csv file and get the values of its rows
            rd = csv.reader(fl)
            for rw in rd:
                # convert row values to digits
                rw = [int(n) for n in rw]
                # setting values read from file
                if (cls is Square):
                    list_objs = {"size": rw[1], "x": rw[2], "y": rw[3], "id": rw[0]}

                else:
                    list_objs = {"width": rw[1], "height": rw[2], "x": rw[3], "y": rw[4], "id": rw[0]}

                # update/set atributes
                Finfo.append(cls.create(**list_objs))

        return (Finfo)
    
    @staticmethod
    def draw(list_rectangles, list_squares):
        """ Turtle Draw """
        import turtle

        win = turtle.Screen()
        win.bgcolor("blue")

        for i in list_rectangles + list_squares:
            x = turtle.Turtle()
            x.color(100, 100, 100)
            x.pensize(1)
            x.pendown()
            x.setpos(i.x + x.pos()[0], i.x - x.pos()[1])
            x.pensize(10)
            x.forward(i.width)
            x.right(90)
            x.forward(i.hight)
            x.right(90)
            x.forward(i.width)
            x.right(90)
            x.forward(i.hight)
            x.right(90)
            x.penup()
            x.end_fill()