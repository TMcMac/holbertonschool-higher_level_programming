#!/usr/bin/python3
"""
This script will connect to a specific database using supplied credentials
and then pull a list of states from the table states and print them in order
"""

import MySQLdb
import sys
""" MySQLdb for the SQLobviously and sys for arguments"""

if __name__ == '__main__':
    """
    Our script will take in username, dbpassword, db name
    and we will connect to localhost.
    """
    name = sys.argv[1]
    passw = sys.argv[2]
    datab = sys.argv[3]
    my_host = "localhost"

    try:
        db = MySQLdb.connect(host=my_host, port=3306,
                             user=name, passwd=passw, db=datab)
        """db will be our database object, our connection to our sql"""
        cur = db.cursor()
        """cur or cursor is how we actually execute queries and do work"""
        cur.execute("SELECT * FROM states ORDER BY 'id' ASC")
        states = cur.fetchall()
        """
        As we are grabing everything from the states table, states receives
        all the output from our query above
        """
    except MySQLdb.Error as e:
        try:
            print("MySQL Error [%d]: %s", e.args[0], e.args[1])
        except IndexError:
            print("MySQL Error: %s", str(e))

    for state in states:
        print(state)
        """This isto print out the results from our query"""

    """Closing up our cursor and db connection when done"""
    cur.close()
    db.close()
