#!/usr/bin/python3
"""Script to list all states with a name starting with N in db"""

import sys
import MySQLdb


if __name__ ="__main__":
    db_conn = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        host='localhost',
        port=3306
    )

    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    
    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    conn.close()
