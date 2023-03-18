#!/usr/bin/python3
"""
This script list all states that start with 'N'
from the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Connects to database and fetches only names starting with 'N' in states
    """
    conn = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE NAME LIKE 'N%' ORDER BY states.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
