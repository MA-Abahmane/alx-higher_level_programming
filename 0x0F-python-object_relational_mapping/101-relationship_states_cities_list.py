#!/usr/bin/python3
"""
    a script that lists all State objects,
    and corresponding City objects, contained
    in the database hbtn_0e_101_usa
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
        <state id>: <state name>
            <tabulation><city id>: <city name>
    """
    # print States
    for state in session.query(State).order_by(State.id):
        print(f"{state.id}: {state.name}")
        # print State Cities
        for city in state.cities:
            print(f"    {city.id}: {city.name}")
