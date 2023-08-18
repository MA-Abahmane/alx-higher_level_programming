#!/usr/bin/python3
"""
    a script that lists all cities from the database hbtn_0e_4_usa
"""

import sys
import MySQLdb as DB


if __name__ == '__main__':
    storage = DB.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    crs = storage.cursor()
    crs.execute("SELECT cy.id, cy.name, st.name \
                FROM `cities` AS `cy` \
                INNER JOIN \
                `states` AS `st` \
                ON cy.state_id = st.id \
                ORDER BY cy.id ASC")
    [print(city) for city in crs.fetchall()]
