#!/usr/bin/python3
"""
Lists one State objects from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
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

    # Query all State objects from database
    first_state = session.query(State).first()

    # Print State object in specified format
    if first_state is None:
        print("Nothing")
    else:
        print("{}: {}".format(first_state.id, first_state.name))

    # close session created
    session.close()
