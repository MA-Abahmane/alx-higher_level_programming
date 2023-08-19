#!/usr/bin/python3
"""
    a script that adds the State object “Louisiana” to the
    database hbtn_0e_6_usa
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

    """
        Create the database tables that correspond to the SQLAlchemy
        model classes defined using the declarative base pattern.
    """
    Base.metadata.create_all(engine)

    """ Set session """
    Session = sessionmaker(bind=engine)
    session = Session()

    """
        create/add row to databases from 'City' only using relationship
    """
    newRow = City(name='San Francisco', state=State(name='California'))
    session.add(newRow)

    session.commit()
