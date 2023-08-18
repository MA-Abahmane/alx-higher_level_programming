#!/usr/bin/python3
"""
    a script that takes in an argument and displays
    all values in the states table of hbtn_0e_0_usa
    where name matches the argument. This version is
    safe from MySQL injections!
"""

import sys
import MySQLdb as DB


if __name__ == '__main__':
    storage = DB.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    Seached = sys.argv[4]

    crs = storage.cursor()
    crs.execute("SELECT * FROM `states` ORDER BY `id` ASC")
    [print(state) for state in crs.fetchall() if (state[1] == Seached)]
