#!/usr/bin/python3
"""
This module contains the class definition of a City
and an instance of the sqlalchemy declarative_base
"""


from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from relationship_state import Base
from sqlalchemy.orm import relationship


class City(Base):
    """A class that inherits from Base
    """
    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'),  nullable=False)
    state = relationship("State", back_populates="cities")


if __name__ == "__main__":
    # connect to the database
    DB_URI = 'mysql+mysqldb://Tau:Changamire#97@localhost:3306/hbtn_0e_6_usa'
    engine = create_engine(DB_URI, pool_pre_ping=True)
    Base.metadata.create_all(engine)
