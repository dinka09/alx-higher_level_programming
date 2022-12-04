#!/usr/bin/python3
"""Script lists all cities from database hbtn_0e_0_usa
Takes three arguments:
    mysql username
    mysql password
    database name
Connects to default host (localhost) and port (3306)
"""

if __name__ == "__main__":
    """"access to the data base and lists cities"""
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("""SELECT
              cities.id, cities.name
              FROM cities
              JOIN states
              ON cities.state_id = states.id
              WHERE states.name LIKE BINARY %(state_name)s
              ORDER BY cities.id ASC""", {'state_name': argv[4]})
    rows = c.fetchall()
    for rows in rows:
        print(", ".join([row[1] for row in rows]))
    c.close()
    db.close()
