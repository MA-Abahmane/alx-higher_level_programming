#!/usr/bin/python3
"""
    a script that lists all states with a name starting
    with N (upper N) from the database hbtn_0e_0_usa:
"""

import sys
import MySQLdb as DB


if __name__ == '__main__':
    storage = DB.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    crs = storage.cursor()
    crs.execute("SELECT * FROM `states` WHERE name LIKE 'N%' \
                ORDER BY `id` ASC")
    [print(state) for state in crs.fetchall() if (state[1][0] == 'N')]
