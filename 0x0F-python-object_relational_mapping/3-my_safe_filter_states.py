#!/usr/bin/python3
"""
This module contains a script that list an item from a database
But preventing SQL Injection as well
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
    cur.execute("SELECT * FROM states \
                WHERE name = %s ORDER BY id ASC", (arg[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
