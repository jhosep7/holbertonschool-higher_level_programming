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
    Sect = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    Var = Sect().query(State).filter(State.name == argv[4]).all()
    if Var:
        for i in Var:
            if i.name == argv[4]:
                print("{}".format(i.id))
    else:
        print("Not found")
    Sect().close()
