#!/usr/bin/python3
"""
A simple scriupt to connect to a MySQLdb and pull states whose names
start with the letter n.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    un = sys.argv[1]
    p = sys.argv[2]
    d = sys.argv[3]
    my_host = "localhost"

    try:
        db = MySQLdb.connect(host=my_host, port=3306,
                             user=un, passwd=p, db=d)
        cur = db.cursor()
        cur.execute("""SELECT * FROM states
                       WHERE name LIKE BINARY 'N%'
                       ORDER BY 'id' ASC""")
        states = cur.fetchall()

    except MySQLdb.Error as e:
        try:
            print("MySQL Error [%d]: %s", e.args[0], e.args[1])
        except IndexError:
            print("MySQL Error: %s", str(e))

    for state in states:
        print(state)

    cur.close()
    db.close()
