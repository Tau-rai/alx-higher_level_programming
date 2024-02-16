#!/usr/bin/python3
"""
This script adds one state object
to the db hbtn_0e_6_usa
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

    # create object
    louisiana = State(name="Louisiana")

    # add object
    session.add(louisiana)

    session.commit()

    louis = session.query(State).filter(State.name == 'Louisiana').first()
    print(louis.id)
    session.close()
