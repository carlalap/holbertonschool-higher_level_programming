#!/usr/bin/python3
"""
script prints the State object id
with the name passed as argument
from the database hbtn_0e_6_usa.
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

    # Retrieve all State objects and sort by id
    states = session.query(State).filter(State.name == argv[4]).first()

    # Display the results
    if states is None:
        print("Not found")
    else:
        print(f"{}: {states.id}")
