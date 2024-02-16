#!/usr/bin/python3
""" This module contains a script that list items from a database
"""


import MySQLdb
import sys

if __name__ == "__main__":
    args = sys.argv
params = {
    'host': "localhost",
    'port': 3306,
    'user': args[1],
    'passwd': args[2],
    'db': args[3],
    'charset': "utf8"
}
conn = MySQLdb.connect(**params)
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
rows = cur.fetchall()
for row in rows:
    print(row)
cur.close()
conn.close()
