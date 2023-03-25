#!/usr/bin/python3
"""
This module defines a child class(City) inherited
from a parent class(Base) and links to MYSQL table cities
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, String, ForeignKey

Base = declarative_base()


class City(Base):
    """
    Class City represents a city columns for mySQL table

    __tablename__: name of table
    id: city id
    name: city name
    state_id: reference to states.id(Foreign Key)
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
