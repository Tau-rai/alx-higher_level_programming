#!/usr/bin/python3
"""
This script lists all state objects from the db hbtn_0e_6_usa
"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == "__main__":
    args = sys.argv
    DB_URI = f'mysql+mysqldb://{args[1]}:{args[2]}@localhost:3306/{args[3]}'
    engine = create_engine(DB_URI, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # create a session
    session = Session(engine)
    for state in session.query(State).order_by(State.id).all():
        print(f"{state.id}: {state.name}")
    session.close()
