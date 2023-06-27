#!/usr/bin/python3
"""
script prints the State object with the name
passed as argument from the database hbtn_0e_6_usa
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

    chg_name = session.query(State).get(2)
    chg_name.name = "New Mexico"
    session.commit()
