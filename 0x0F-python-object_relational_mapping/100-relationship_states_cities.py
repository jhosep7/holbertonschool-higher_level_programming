#!/usr/bin/python3
"""Create state California"""
from sys import argv
from relationship_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from relationship_city import City


if __name__ == "__main__":
    engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost:3306/{}'
                .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Sect1 = sessionmaker(bind=engine)
    Sect2 = Sect1()
    new_state = State(name="California")
    Sect2.add(new_state)
    Sect2.commit()
    new_city = City(name="San Francisco", state_id=new_state.id)
    Sect2.add(new_city)
    Sect2.commit()
    Sect2.close()
