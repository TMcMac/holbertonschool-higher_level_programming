#!/usr/bin/python3
"""
Gets only the first row in the states table
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import State, Base


def get_first_state():
    """Get the first state in the table"""
    user_name = argv[1]
    password = argv[2]
    db_name = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(user_name, password, db_name))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).first():
        print("{}: {}".format(state.id, state.name))

    session.close()

if __name__ == '__main__':
    get_first_state()
