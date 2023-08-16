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
    cur.execute("SELECT * FROM states
                WHERE states.name = %s
                ORDER BY states.id ASC".format(sys.argv[4])
    )
    states = cur.fetchall()

    for row in states:
        print(row)
