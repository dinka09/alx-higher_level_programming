#!/usr/bin/python3
"""Script lists all states with a name starting with N from database
Takes three arguments:
    mysql username
    mysql password
    database name
Connects to default host (localhost) and port (3306)
"""

if __name__ == "__main__":
    """Filters the file"""
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("""SELECT * FROM states WHERE name LIKE BINART '{}'
              ORDER BY states.id ASC""".format(argv[4]))
    rows = c.fetchall()
    for row in rows:
        print(row)
