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

    cursor = conn.cursor()
    query = """ SELECT * FROM states
                WHERE BINARY name = '{}'
                ORDER BY id ASC
            """.format(sys.argv[4])
    
    cursor.execute(query)
    states = cursor.fetchall()
    
    for state in states:
        print(state)

    cursor.close()
    conn.close()
