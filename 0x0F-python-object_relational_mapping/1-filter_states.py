#!/usr/bin/python
"""Script lists all states from database hbtn_0e_0_usa
Takes three arguments:
    mysql username
    mysql password
    database name
Connects to default host (localhost) and port (3306)
"""

if __name__== "__main__":
    """lists the value by sorting"""
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("""SELECT * FROM states WhERE name like 'N%'\ORDER BY states.id ASC""")
    names = c.fetchall()
    for name in names:
        print(name)
    c.close()
    db.close()
