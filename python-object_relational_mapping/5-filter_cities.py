#!/usr/bin/python3
"""Lists all cities of a given state from hbtn_0e_4_usa, injection safe."""
import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT cities.name "
                "FROM cities "
                "INNER JOIN states ON states.id = cities.state_id "
                "WHERE states.name = %s "
                "ORDER BY cities.id ASC", (sys.argv[4],))
    names = []
    for row in cur.fetchall():
        names.append(row[0])
    print(", ".join(names))
    cur.close()
    conn.close()
