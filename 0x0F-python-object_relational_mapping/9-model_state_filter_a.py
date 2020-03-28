#!/usr/bin/python3
"""lists all State objects that contain the letter a"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Sect = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    Var = Sect().query(State).filter(State.name.like('%a%')).order_by(
        State.id).all()
    if Var:
        for i in Var:
            if 'a' in i.name:
                print("{}: {}".format(i.id, i.name))
    Sect().close()
