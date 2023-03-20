#!/usr/bin/python3
"""
This script list argument-specified states and cities
from the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Connects to database and fetches all information in states and cities
    """
    conn = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name FROM cities\
            INNER JOIN states ON cities.state_id = states.id\
            WHERE states.name = %s", (argv[4],))
    rows = cur.fetchall()

    print(", ".join([row[1] for row in rows]))

    cur.close()
    conn.close()
