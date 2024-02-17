#!/usr/bin/python3
"""
This script creates the State "California" with the City
"San Franciso" from the database
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    args = sys.argv
    DB_URI = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        args[1], args[2], args[3]
    )
    engine = create_engine(DB_URI, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # create a session
    session = Session(engine)

    # create new State and City objects
    new_state = State(name="California")
    new_city = City(name="San Francisco", state=new_state)

    # add and commit the new objects to the database
    session.add(new_state)
    session.add(new_city)
    session.commit()

    session.close()
