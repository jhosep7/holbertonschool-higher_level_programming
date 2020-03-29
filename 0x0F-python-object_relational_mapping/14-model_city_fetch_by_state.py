#!/usr/bin/python3
"""prints all City objects from the database hbtn_0e_14_usa"""
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost:3306/{}'
                .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Sect1 = sessionmaker(bind=engine)
    Sect2 = Sect1()
    Var = Sect2.query(City, State).\
        filter(City.state_id == State.id).all()
    for i, j in Var:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    Sect2.commit()
    Sect2.close()
