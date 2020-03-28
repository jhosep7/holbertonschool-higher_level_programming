#!/usr/bin/python3
"""SQL injection"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    Link = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
                           user=argv[1], passwd=argv[2], db=argv[3])
    Cursor = Link.cursor()
    Cursor.execute("SELECT * FROM states WHERE name = %s\
    ORDER BY states.id ASC", (argv[4], ))
    List = Cursor.fetchall()
    for i in List:
        print(i)
    Cursor.close()
    Link.close()
