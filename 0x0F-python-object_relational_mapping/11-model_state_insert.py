#!/usr/bin/python3
"""
Add a new State object to the existiong one
in the database hbtn_0e_6_usa
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

    # Add new State object
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Print State object in specified format
    print(new_state.id)

    # close session created
    session.close()
