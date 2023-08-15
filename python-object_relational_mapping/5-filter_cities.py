#!/usr/bin/python3
'''
    A script that takes in the name of a state as an
    argument and lists all cities of that state, using
    the database hbtn_0e_4_usa
'''


import sys
import MySQLdb


if __name__ == "__main__":
    conn = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        host="localhost",
        port=3306
    )

    state_name = sys.argv[4]

    cursor = conn.cursor()

    sql_com = """SELECT cities.name
          FROM cities
          INNER JOIN states ON states.id = cities.state_id
          WHERE states.name = %s
          ORDER BY cities.id ASC"""

    cursor.execute(query, (state_name,))
    data = cursor.fetchall()

    print(", ".join([state[1] for state in states]))

    cursor.close()
    conn.close()
