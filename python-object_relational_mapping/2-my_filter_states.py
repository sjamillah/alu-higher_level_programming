#!/usr/bin/python3
"""Script that takes in an arg and displays names that match arg"""

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
                WHERE states.name = '{:s}'
                ORDER BY states.id ASC".format(sys.argv[4])
    )

    states = cur.fetchall()
    for row in states:
        if row[1] == sys.argv[4]:
        print(row)

    cur.close()
    db_conn.close()
