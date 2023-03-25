#!/usr/bin/python3
"""
This module defines a child class(State) inherited from
a parent class(Base) which subsequently links to mySQL
table(states)
"""

from sqlalchemy import Column, Integer, String
from relationship_city import Base, City
from sqlalchemy.orm import relationship


class State(Base):
    """
    Class State represents a state columns for mySQL table

    __tablename__: name of table
    id: state id
    name: state name
    cities: defines relationship of State with City model class
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
