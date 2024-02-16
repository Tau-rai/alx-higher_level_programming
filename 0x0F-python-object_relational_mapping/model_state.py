"""
This module contains the class definition of a State
and an instance of the sqlalchemy declarative_base
"""


from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# connect to the database
DB_URI = 'mysql+mysqldb://root:root@localhost:3306/hbtn_0e_6_usa'
engine = create_engine(DB_URI, pool_pre_ping=True)

# create a declarative base for mapping classes to db tables
Base = declarative_base()


class State(Base):
    """A class that inherits from Base
    """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)


# create the tables in the database
Base.metadata.create_all(engine)
