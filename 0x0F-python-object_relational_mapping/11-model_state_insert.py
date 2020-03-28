#!/usr/bin/python3
"""adds the State object “Louisiana” to the database"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Sect1 = sessionmaker()
    Sect2 = Sect1(bind=engine)
    Base.metadata.create_all(engine)
    Var = State(name="Louisiana")
    Sect2.add(Var)
    Sect2.commit()
    print(Var.id)
    Sect2.close()
