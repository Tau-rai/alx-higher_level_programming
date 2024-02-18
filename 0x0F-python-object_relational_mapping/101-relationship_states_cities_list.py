#!/usr/bin/python3
"""
This script lists all State objects and corresponding City objects,
in the database hbtn_0e_101_usa
"""


import sys
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == "__main__":
    args = sys.argv
    DB_URI = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            args[1], args[2], args[3]
            )
    engine = create_engine(DB_URI, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # create a session
    session = Session(engine)

    # query the state/city objects and displaying the results
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
        for city in sorted(state.cities, key=lambda x: x.id):
            print("\t{}: {}".format(city.id, city.name))

    session.close()
