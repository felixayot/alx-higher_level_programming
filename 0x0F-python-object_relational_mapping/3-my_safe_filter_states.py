#!/usr/bin/python3
"""Takes in arguments and displays all values in the states table
   of hbtn_0e_0_usa where name matches the argument,
   ONLY, this is safe from MySQL injections!
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `states`")
    [print(state) for state in cur.fetchall() if state[1] == sys.argv[4]]
