#!/usr/bin/python3
"""
This script will connect to a specific database using supplied credentials
and then pull a list of states from the table states and print them in order
"""

import MySQLdb
import sys

if __name__ == '__main__':
    name = sys.argv[1]
    passw = sys.argv[2]
    datab = sys.argv[3]
    my_host = "localhost"

    try:
        db = MySQLdb.connect(host=my_host, port=3306,
                             user=name, passwd=passw, db=datab)
        cur = db.cursor()
        cur.execute("SELECT * FROM states ORDER BY 'id' ASC")
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
