#!/usr/bin/python3
"""
Script that contains the class State
and an instance Base = declarative_base(),
works with MySQLAlchemy ORM.
"""


from sqlalchemy import Colum, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
   """
    Class State inherits from Base Tips
    """
    __tablename__ = 'states'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
