#!/usr/bin/python3
"""
    Improve the files model_city.py and model_state.py, and
    save them as relationship_city.py and relationship_state.py:
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from relationship_city import Base, City


class State(Base):
    """
        Class state:
        -' __tablename__' links to the MySQL table states

        - class attribute id that represents
        a column of an auto-generated, unique
        integer, can’t be null and is a primary key

        - class attribute name that represents
        a column of a string with maximum 128
        characters and can’t be null
    """

    """ relationship with state """
    cities = relationship('City', backref='state', cascade='all, delete')

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
