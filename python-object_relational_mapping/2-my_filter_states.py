#!/usr/bin/python3
"""
This script takes in an argument and displays all
values in the states table of hbtn_0e_0_usa where
name matches the argument.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """This line checks if the script is being
    executed directly (not imported as a module).
    """

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])
    # fetch results from the database
    cursor = db.cursor()
    """ Execute the query to retrieve the state name"""

    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' \
                    ORDER BY states.id ASC".format(argv[4]))
    # fetches all the rows returned by the SQL
    # query and stores them in the rows variable.
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)
