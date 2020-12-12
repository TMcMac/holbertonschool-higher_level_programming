#!/usr/bin/python3
"""
A simple script to connect to MySQL and pull all states that match
user supplied name
"""

import MySQLdb
import sys

if __name__ == '__main__':
	un = sys.argv[1]
	pw = sys.argv[2]
	dbase = sys.argv[3]
	state = sys.argv[4]
	lhost = "localhost"

	try:
		db = MySQLdb.connect(host=lhost, port=3306, user=un, passwd=pw, db=dbase)
		cur = db.cursor()
		cur.execute("""SELECT * FROM states WHERE name = '{}' ORDER BY id ASC""".format(state))
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
