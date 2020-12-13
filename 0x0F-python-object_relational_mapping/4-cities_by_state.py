#!/usr/bin/python3
"""
For this script we will be combining two tables
to get cities with their states
"""

import MySQLdb
import sys

if __name__ == '__main__':
    """
    arguments will be username, password
    database name. Results will be sorted
    by city id
    """
    un = sys.argv[1]
    pw = sys.argv[2]
    dbase = sys.argv[3]
    my_host = "localhost"

    try:
        db = MySQLdb.connect(host=my_host, port=3306, user=un,
                             passwd=pw, db=dbase)
        cur = db.cursor()
        cur.execute("""SELECT cities.id, cities.name, states.name
                       FROM cities
                       INNER JOIN states ON cities.state_id = states.id
                       ORDER BY cities.id ASC""")
        result = cur.fetchall()
    except MySQLdb.Error as e:
        try:
            print("MySQLdb Error {}: {}".format(e.args[0], e.args[1]))
        except IndexError:
            print("MySQLdb Error: {}".format(str(e)))

    for city in result:
        print(city)

    cur.close()
    db.close()
