#!/usr/bin/python3
"""
Creates State "California" with the City "San Francisco"
from the database hbtn_0e_100_usa
"""

import sys
from relationship_state import State
from relationship_city import Base, City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # creates all table associated with Base metadata
    Base.metadata.create_all(engine)

    # create a new session instance bound to the create engine
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to add info to both State and City objects at the same time
    session.add(City(name="San Francisco", state=State(name="California")))
    session.commit()
