#!/usr/bin/python3
"""Improve model_state.py as relationship_state.py"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class State(Base):
    """Class State"""
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete-orphan",
        backref=backref("state", cascade="all"),
        single_parent=True)
