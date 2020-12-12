#!/usr/bin/python3
''' A script to get all the states from a table '''

import MySQLdb
import sys

if __name__ == '__main__':
	''' Connects to a DB and gets info '''

	my_user = sys.argv[1]
	my_pass = sys.argv[2]
	my_db = sys.argv[3]
	passedname = sys.argv[4]
	localhost = "localhost"

	try:
		db = MySQLdb.connect(host=localhost, port=3306, user=my_user,
							 passwd=my_pass, db=my_db)
		cur = db.cursor()
		cur.execute("""SELECT * FROM states
					   WHERE name = %s
					   ORDER BY 'id' ASC""", (passedname,))
		states = cur.fetchall()
	except MySQLdb.Error as e:
		try:
			print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
		except IndexError:
			print("MySQL Error: {}".format(str(e)))

	for state in states:
		print(state)

	cur.close()
	db.close()

