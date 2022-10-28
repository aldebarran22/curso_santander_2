"""
Consultas a la BD
"""

import sqlite3 as dbapi
from os.path import isfile

path = "../BD/empresa3.db"

con = None
cur = None
try:
    if not isfile(path):
        raise ValueError("El fichero "+path+" no existe")

    con = dbapi.connect(path)
    cur = con.cursor()

    while True:
        sql = input("SQL> ")
        cur.execute(sql)

        cab = [t[0] for t in cur.description]
        print(*cab, end="\t\t")
        print()

        for t in cur.fetchall():
            print(*t, end="\t\t")
            print()
            
except Exception as e:
    print(e)

finally:
    if cur: cur.close()
    if con: con.close()


