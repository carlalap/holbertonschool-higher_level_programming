#!/usr/bin/python3
"""lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

try:
    """connect to MySQL server"""
    conn = MySQLdb.connect(
        host='localhost', port=3306,
        user=username, passwd=password, db=database)
    cursor = conn.cursor()

    """ Execute the query to retrieve states starting with N"""
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    # Fetch all the rows
    rows = cursor.fetchall()
    # Display the results
    for row in rows:
        print(row)
except MySQLdb.Error as e:
    print("Error connecting to MySQL:", e)
finally:
    # Close the database connection
    if conn:
        conn.close()
