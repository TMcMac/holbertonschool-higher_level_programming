#!/usr/bin/env python3
"""Get all cities from the cities table"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def state_cities():
    """Get all cities with id by state"""

    un = argv[1]
    pw = argv[2]
    db = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(un, pw, db), pool_pre_ping = True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(City, State).join(State, State.id == City.state_id).all()

    for res in results:
        print("{}: ({}) {}".format(res[1].name, res[0].id, res[0].name))
    session.close()

if __name__ == '__main__':
    state_cities()
