#!/usr/bin/python3
"""deletes all State objects with a name """
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
    Base.metadata.create_all(engine)
    Var = Sect2.query(State).filter(State.name.like('%a%')).all()
    if Var:
        for i in Var:
            Sect2.delete(i)
        Sect2.commit()
    Sect2.close()
