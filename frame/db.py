# db.py
import sqlite3

from frame import itemsql


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

    def makeTableitem(self):
        cs = None;
        con = None;
        try:
            con = self.connect();
            cs = con.cursor();
            cs.execute(itemsql.MAKE_TABLE);
            con.commit();
        except:
            print('Make Table Error');
        finally:
            self.close(cs, con);