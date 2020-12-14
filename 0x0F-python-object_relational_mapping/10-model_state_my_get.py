#!/usr/bin/python3
"""Get a state by name from the table states"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def get_a_state():
    """get a state by name"""
    user = argv[1]
    pw = argv[2]
    db = argv[3]
    astate = argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, pw, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter_by(name == astate).first()

    if state is not None:
        print("{}".format(state.id))
    else:
        print("Not Found")

    session.close()

if __name__ == '__main__':
    get_a_state()
