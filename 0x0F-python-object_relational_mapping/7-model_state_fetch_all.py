#!/usr/bin/python3
"""Use SQL alchemy to get all states from the states table"""


import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State


def get_states():
    engine = sqlalchemy.create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                                      .format(argv[1],
                                              argv[2],
                                              argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))

    session.close()

if __name__ == '__main__':
    get_states()
