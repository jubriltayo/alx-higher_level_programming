#!/usr/bin/python3
"""
This module defines a child class(State) inherited from
a parent class(Base) which subsequently links to mySQL
table(states)
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Class State represents a state columns for mySQL table

    __tablename__: name of table
    id: state id
    name: state name
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
