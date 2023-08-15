#!/usr/bin/python3
"""Script that takes in an arg and displays names that match arg"""

import sys
import MySQLdb


if __name__ = "__main__":
    conn = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        host='localhost',
        port=3306
    )

    cur = conn.cursor()
    query = """ SELECT * FROM states
                WHERE name LIKE BINARY 'N%'
                ORDER BY id ASC
            """
    
    cur.execute(query, (sys.argv[4],))
    states = cur.fetchall()
    
    for state in states:
        print(state)

    cur.close()
    conn.close()
