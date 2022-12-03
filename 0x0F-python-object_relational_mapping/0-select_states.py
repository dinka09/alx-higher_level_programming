#!/usr/bin/python3
"""Write a script that lists all states from the database hbtn_0e_0_usa """

import MySQLdb
from sys import argv

def query_table():
    db=MySQLdb.connect(host="localhost",port=3306,user=argv[1],password=argv[2],db="hbtn_0e_0_usa")
    print(db.query("select * from states group by id"))
if __name__ == '__main__':
    query_table()
