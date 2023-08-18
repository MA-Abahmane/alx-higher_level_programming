#!/usr/bin/python3
"""
    a script that prints the State object with the name
    passed as argument from the database hbtn_0e_6_usa
"""

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    searched = sys.argv[4]

    Session = sessionmaker(bind=engine)
    session = Session()

    """
        seach for given state; if found print out its id
        else; print 'not found'
    """
    flag = False
    for state in session.query(State).order_by(State.id):
        if (state.name == searched):
            flag = True
            print("{0}".format(state.id))
            break

    if (not flag):
        print('Not found')
