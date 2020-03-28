#!/usr/bin/python3
"""prints the State object with the name passed as argument"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Sect1 = sessionmaker(bind=engine)
    Sect2 = Sect1()
    Var = Sect2.query(State).filter(State.id == 2).all()
    if Var:
        Var[0].name = "New Mexico"
    Sect2.commit()
    Sect2.close()
