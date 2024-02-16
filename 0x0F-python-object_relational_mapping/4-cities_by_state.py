#!/usr/bin/python3
"""
This module contains a script that lists
states and cities from a database
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
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities \
                    JOIN states ON cities.state_id = states.id \
                    ORDER BY cities.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
