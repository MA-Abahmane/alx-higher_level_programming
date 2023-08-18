#!/usr/bin/python3
"""
    a script that changes the name of a State object from the
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
    newName = 'New Mexico'

    """ Set session """
    Session = sessionmaker(bind=engine)
    session = Session()

    """ get the row where is equal to 2 """
    row = session.query(State)
    row = row.filter(State.id == 2)

    """ update the rows name value to the given one """
    record = row.one()
    record.name = newName

    session.commit()
