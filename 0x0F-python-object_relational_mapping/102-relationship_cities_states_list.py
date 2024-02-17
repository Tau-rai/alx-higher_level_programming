#!/usr/bin/python3
"""
This script prints all city objects from the
database hbtn_0e_101_usa
"""


import sys
from model_city import City
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

    # querying the state/city objects and displaying the results
    for city in session.query(City).join(State).order_by(City.id):
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
    session.close()
