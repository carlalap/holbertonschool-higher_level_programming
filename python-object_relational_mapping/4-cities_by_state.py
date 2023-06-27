#!/usr/bin/python3
"""
this script lists all cities from
the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """ Access to the database and get the cities
    from the database.
    """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])
    # fetch results from the database
    cursor = db.cursor()
    """ Execute the query to retrieve the records from db"""
    cursor.execute("SELECT city.id, city.name, states.name FROM  cities \
                    JOIN states ON cities.state_id = states.id \
                    ORDER BY cities.id ASC")
    # fetches all the rows returned by the SQL
    # query and stores them in the rows variable.
    rows = cursor.fetchall()

    # Display the results
    if rows is not None:
        for row in rows:
            print(row)
