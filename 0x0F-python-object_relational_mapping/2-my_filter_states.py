#!/usr/bin/python3
"""
This script takes in an argument and prints
the states that matches the argument
from the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Connects to database and fetches information from states
    """
    conn = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM states\
            WHERE name LIKE BINARY '{argv[4]}'\
            ORDER BY states.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
