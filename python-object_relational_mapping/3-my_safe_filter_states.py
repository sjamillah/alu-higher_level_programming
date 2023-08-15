#!/usr/bin/python3
"""
Prints out all values in the states tables of a database
where name matches the argument in a safe way
"""

import sys
import MySQLdb


if __name__ = "__main__":
    db_conn = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        host='localhost',
        port=3306
    )

    cur = db_conn.cursor()
    query = """ SELECT * FROM states
                WHERE name = %s
                ORDER BY id ASC
            """

    cur.execute(query, (sys.argv[4],))
    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db_conn.close()
