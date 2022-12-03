#!/usr/bin/python3
"""Write a script that lists all states from the database hbtn_0e_0_usa """

from MySQLdb import _mysql
def query_table():
    db=_mysql.connect(host="localhost",port=3306,user="mysql",passwd="mysql",db="hbtn_0e_0_usa")
    print(db.query("select * from states group by id"))
if __name__ == '__main__':
    query_table()
