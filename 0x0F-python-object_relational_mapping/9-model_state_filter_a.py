#!/usr/bin/python3
"""
This script prints state objects from the db hbtn_0e_6_usa
that have the letter a in the name
"""


import sys
from model_state import Base, State
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

    # querying the state objects and displaying the results
    states_with_a = session.query(State).filter(State.name.like('%a%')).all()
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))
    session.close()
