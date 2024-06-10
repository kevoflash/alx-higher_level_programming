#!//usr/bin/pyhon3
"""
a script that lists all states from the database
"""

import sys
import mySQLdb

if _name_ =='_main':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states;")
    states = cur.fetchall()

    for state in states:
        print(state)
