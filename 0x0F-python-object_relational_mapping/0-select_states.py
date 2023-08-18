#!/usr/bin/python3
"""
    a script that lists all states from the database hbtn_0e_0_usa:
    The script takes 3 arguments: mysql username, mysql password
    and database name (no argument validation needed).
"""

import sys
import MySQLdb as DB


if __name__ == '__main__':
    storage = DB.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    crs = storage.cursor()
    crs.execute("SELECT * FROM `states` ORDER BY `id` ASC")
    [print(state) for state in crs.fetchall()]
