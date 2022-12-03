#!/usr/bin/python3
"""Script lists all states from database hbtn_0e_0_usa
Takes three arguments:
    mysql username
    mysql password
    database name
Connects to default host (localhost) and port (3306)
"""

import MySQLdb
from sys import argv

def query_table():
    db=MySQLdb.connect(host="localhost",port=3306,user=argv[1],password=argv[2],database="hbtn_0e_0_usa")
    print(db.query("select * from states group by id"))
if __name__ == '__main__':
    query_table()
