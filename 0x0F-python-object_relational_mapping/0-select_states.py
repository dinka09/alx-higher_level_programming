#!/usr/bin/python3
"""Write a script that lists all states from the database hbtn_0e_0_usa """

import MySQLdb
from sys import argv

def query_table():
    db=MySQLdb.connect(host="localhost",user=argv[1],password=argv[2],port=3306,database=argv[3])
    print(db.query("select * from states group by id"))
if __name__ == '__main__':
    """Access to the database and get the state from it"""
    query_table()
