#!/usr/bin/python3
"""
    A script that lists all cities from the database hbtn_0e_4_usa
"""


import sys
import MySQLdb


if __name__ == "__main__":
    conn = MySQLdb.connect(
        user=sys.argv[1],
        password=sys.argv[2],
        db=sys.argv[3],
        host="localhost",
        port=3306
    )
    cursor = conn.cursor()

    query = """SELECT cities.id, cities.name, states.name
          FROM cities
          INNER JOIN states
          ON cities.state_id = states.id
          ORDER BY cities.id ASC"""

    cursor.execute(query)
    states = cursor.fetchall()

    for row in states:
        print(row)

    cursor.close()
    conn.close()
