#!/usr/bin/python3
"""
Module to instantiate Base and create a class State
that inherits from Base
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """ defines state with inheritance from base from SQLalchemy """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
