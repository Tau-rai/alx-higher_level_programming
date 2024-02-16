#!/usr/bin/python3
"""
This module contains a script that lists all the cities
in a state from the database
"""


import MySQLdb
import sys

if __name__ == "__main__":
    arg = sys.argv
    params = {
        'host': "localhost",
        'port': 3306,
        'user': arg[1],
        'passwd': arg[2],
        'db': arg[3],
        'charset': "utf8"
    }
    conn = MySQLdb.connect(**params)
    cur = conn.cursor()
    cur.execute("SELECT cities.name FROM cities \
                    JOIN states ON cities.state_id = states.id \
                    WHERE states.name = %s ORDER BY cities.id ASC", (arg[4],))
    rows = cur.fetchall()
    print(", ".join(city[0] for city in rows))
cur.close()
conn.close()
