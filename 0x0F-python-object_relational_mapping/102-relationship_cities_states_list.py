#!/usr/bin/python3
""" lists all City objects from the database hbtn_0e_101_usa"""
from relationship_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from relationship_city import City
from sys import argv


if __name__ == "__main__":
    engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost:3306/{}'
                .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Sect1 = sessionmaker(bind=engine)
    Sect2 = Sect1()
    Var = Sect2.query(City).order_by(City.id).all()
    for city in Var:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
    Sect2.commit()
    Sect2.close()
