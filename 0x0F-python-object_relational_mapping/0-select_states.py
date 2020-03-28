#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    Link = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
                           user=argv[1], passwd=argv[2], db=argv[3])
    Cursor = Link.cursor()
    Cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    List = Cursor.fetchall()
    for i in List:
        print(i)
    Cursor.close()
    Link.close()
