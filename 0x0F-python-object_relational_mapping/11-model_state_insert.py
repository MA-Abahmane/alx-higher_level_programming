#!/usr/bin/python3
"""
    a script that adds the State object “Louisiana” to the
    database hbtn_0e_6_usa
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

    """ Set session """
    Session = sessionmaker(bind=engine)
    session = Session()

    """
        add row values to database and print its id
    """
    newState = State(name='Louisiana')
    session.add(newState)
    session.commit()

    print(newState.id)
