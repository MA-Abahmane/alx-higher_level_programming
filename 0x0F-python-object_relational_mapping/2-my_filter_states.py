#!/usr/bin/python3
"""
    a script that takes in an argument and displays
    all values in the states table of hbtn_0e_0_usa
    where name matches the argument.
"""

import sys
import MySQLdb as DB


if __name__ == '__main__':
    storage = DB.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    toSeach = sys.argv[4]

    crs = storage.cursor()
    crs.execute("SELECT * FROM `states` WHERE `name` = '{0}'\
                ORDER BY `id` ASC".format(toSeach))
    [print(state) for state in crs.fetchall()]
