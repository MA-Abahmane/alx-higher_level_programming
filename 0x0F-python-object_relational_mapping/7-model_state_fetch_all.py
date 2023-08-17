#!/usr/bin/python3
"""
    a script that lists all State objects from the database hbtn_0e_6_usa
"""

import sys

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import State


if __name__ == "__main__":
    """ Load engine """
    engine = create_engine('mysql+mysqldb://{0}:{1}@localhost/{2}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    """ create session """
    Session = sessionmaker(bind=engine)
    session = Session()

    """ print from table """
    [print("{0}: {1}".format(state.id, state.name)) for state in session
     .query(State).order_by(State.id)]
