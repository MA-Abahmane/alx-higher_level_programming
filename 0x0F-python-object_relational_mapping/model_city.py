#!/usr/bin/python3
"""
    a Python file similar to model_state.py named
    model_city.py that contains the class definition of a City.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
        Class state:
        -' __tablename__' links to the MySQL table cities

        - class attribute id that represents a column
        of an auto-generated, unique integer, can’t be
        null and is a primary key

        - class attribute name that represents a column
        of a string of 128 characters and can’t be null

        - class attribute state_id that represents a column
        of an integer, can’t be null and is a foreign key
        to states.id
    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
