#!/usr/bin/python3
"""contains the class definition of a City"""
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationshipg
from model_state import Base, State


class City(Base):
    """Inheritance from State"""
    __tablename__ = 'cities'
    id = Column('id', Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
