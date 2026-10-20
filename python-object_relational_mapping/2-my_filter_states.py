#!/usr/bin/python3
"""Displays all states from hbtn_0e_0_usa where name matches the argument."""
import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name = BINARY '{}' "
                "ORDER BY id ASC".format(sys.argv[4]))
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()
