#!/usr/bin/python3
"""
    a script that deletes all State objects with a name
    containing the letter a from the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    """ Creat connection """
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    newName = 'New Mexico'

    """ Set session """
    Session = sessionmaker(bind=engine)
    session = Session()

    """ get the row where with an n in it """
    rowToDelete = session.query(State).filter(State.name.like('%a%')).all()

    [session.delete(row) for row in rowToDelete]

    session.commit()
