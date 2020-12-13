#!/usr/bin/python3
"""
For this script we will be combining two tables
to get cities with their states
"""

import MySQLdb
import sys


def get_cities_by_state():
    """
    arguments will be username, password
    database name. Results will be sorted
    by city id
    """
    un = sys.argv[1]
    pw = sys.argv[2]
    dbase = sys.argv[3]
    astate = sys.argv[4]
    my_host = "localhost"
    query = """SELECT cities.name
                FROM cities
                INNER JOIN states ON cities.state_id = states.id
                WHERE states.name = %s
                ORDER BY cities.id ASC"""

    try:
        db = MySQLdb.connect(host=my_host, port=3306,
                             user=un, passwd=pw, db=dbase)
        cur = db.cursor()
        cur.execute(query, (astate,))
        result = cur.fetchall()
    except MySQLdb.Error as e:
        try:
            print("MySQLdb Error {}: {}".format(e.args[0], e.args[1]))
        except IndexError:
            print("MySQLdb Error: {}".format(str(e)))

    oput = ""
    count = 0
    for city in result:
        oput = oput + city[0]
        count += 1
        if count < len(result):
            oput = oput + ", "
    print(oput)

    cur.close()
    db.close()

if __name__ == '__main__':
    get_cities_by_state()
