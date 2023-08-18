#!/usr/bin/python3
"""
    a script 14-model_city_fetch_by_state.py that prints
    all City objects from the database hbtn_0e_14_usa:
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import Base, City


if __name__ == "__main__":
    """ Creat connection """
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    """ Set session """
    Session = sessionmaker(bind=engine)
    session = Session()

    """
        display Information from the two table `city` and `state`
        Information structure: (<state name>: (<city id>) <city name>)
    """
    [print(f"{state.name}: ({city.id}) {city.name}") for city,
     state in session.query(City, State)
     .filter(City.state_id == State.id).order_by(City.id)]
