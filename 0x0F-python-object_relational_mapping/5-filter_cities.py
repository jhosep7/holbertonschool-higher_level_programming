#!/usr/bin/python3
"""takes in the name of a state as an argument and lists all cities
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    Link = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
                           user=argv[1], passwd=argv[2], db=argv[3])
    Cursor = Link.cursor()
    Cursor.execute("SELECT * FROM cities JOIN states\
    ON cities.state_id = states.id\
    WHERE states.name = %s ORDER BY cities.id ASC", (argv[4], ))
    List = Cursor.fetchall()
    City = []
    for i in List:
        if i[4] == argv[4]:
            City.append(i[2])
    print(', '.join(City))
    Cursor.close()
    Link.close()
