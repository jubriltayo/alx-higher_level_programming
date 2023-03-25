#!/usr/bin/python3
"""
Lists all State objects and corresponding City objects
contained in the database hbtn_0e_101_usa
"""

import sys
from relationship_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # create a new session instance bound to the create engine
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query State objects
    states = session.query(State).order_by(State.id)

    # Print
    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
