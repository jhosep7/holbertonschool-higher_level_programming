#!/usr/bin/python3
"""lists all State objects, and corresponding City objects, contained in the database hbtn_0e_101_usa
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost:3306/{}'
                .format(argv[1], argv[2],
                        argv[3]),pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Sect1 = sessionmaker(bind=engine)
    Sect2 = Sect1()
    Var = Sect2.query(State).order_by(State.id).all()
    for i in Var:
        print("{}: {}".format(i.id, i.name))
        for j in i.cities:
            print("\t{}: {}".format(j.id, j.name))
    Sect2.commit()
    Sect2.close()
