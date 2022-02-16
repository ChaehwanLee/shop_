# db.py
import sqlite3

class Db:
    def __init__(self, dbname):
        self.__dbname = dbname;

    def connect(self):
        con = sqlite3.connect(self.__dbname);
        return con;

    def close(self, *cs):
        for c in cs:
            if c is not None:
                c.close();
