#!/usr/bin/python3
"""
    a script that lists all City objects from the database hbtn_0e_101_usa
"""


if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from relationship_city import Base, City
    from relationship_state import Base, State

    """ Creat connection """
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    """ Set session """
    Session = sessionmaker(bind=engine)
    session = Session()

    """
        display Information from the two table `state` and `city`
        Information structure:
        <city id>: <city name> -> <state name>
    """
    # City name, order by id and print its corecponding
    for city in session.query(City).order_by(City.id):
        state = city.state.name
        print(f"{city.id}: {city.name} -> {state}")
