#!/usr/bin/python3
"""
Gets states from the states table prints based on contains letter 'a'
"""

from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """ Import guard """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for astate in session.query(State).order_by(State.id).filter(
            State.name.like('%a%')):
        print("{}: {}".format(astate.id, astate.name))

    session.close()
