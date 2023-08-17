#!/usr/bin/python3
"""
    a script that takes in the name of a state
    as an argument and lists all cities of that
    state, using the database hbtn_0e_4_usa
"""

import sys
import MySQLdb as DB


if __name__ == '__main__':
    storage = DB.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    srch_state = sys.argv[4]

    crs = storage.cursor()
    crs.execute("SELECT cy.id, cy.name, st.name \
                FROM `cities` AS `cy` \
                INNER JOIN \
                `states` AS `st` \
                ON cy.state_id = st.id \
                ORDER BY cy.id ASC")
    print(', '.join([cy[1] for cy in crs.fetchall() if cy[2] == srch_state]))
