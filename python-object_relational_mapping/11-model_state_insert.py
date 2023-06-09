#!/usr/bin/python3
"""
script that that changes the name of a 
State object from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the database and get the states
    from the database.
    """

    # Create engine and bind session
    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.\
             format(argv[1], argv[2], argv[3])
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    session = Session()

    state_name = State(name="Louisiana")
    session.add(state_name)
    session.commit()
    print(state_name.id)
