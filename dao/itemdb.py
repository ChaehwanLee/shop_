# itemdb.py
from dao import itemsql
from frame.db import Db
from model.itemmodel import Item

class ItemDb(Db):
    def __init__(self,dbname):
        super().__init__(dbname); # 기능이 없어서 상속받음 super().
        self.makeTable(); # 내 자신을 요청해라

    def makeTable(self):
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

    def insert(self, item):
        cs = None;
        con = None;
        try:
            con = super().connect();
            cs = con.cursor();
            cs.execute(item.getsql().strip());
            con.commit();
        except:
            raise Exception;
        finally:
            super().close(cs, con);

    def select(self):
        con = None;
        cs = None;
        results = None;
        try:
            con = super().connect();
            cs = con.cursor();
            cs.execute(itemsql.ITEM_SELECT);
            results = cs.fetchall(); # SELECT 문에서 여러개를 가져와서 fetch + all
        except:
            raise Exception;
        finally:
            super().close(cs, con);
        return results;

    def delete(self, id):
        con = None;
        cs = None;
        results = None;
        try:
            con = super().connect();
            cs = con.cursor();
            cs.execute(itemsql.ITEM_DELETE % (id));
            con.commit();
        except:
            raise Exception;
        finally:
            super().close(cs, con);
        return results;

    def update(self):
        con = None;
        cs = None;
        results = None;
        try:
            con = super().connect();
            cs = con.cursor();
            cs.execute(itemsql.ITEM_UPDATE);
            results = cs.fetchall();
        except:
            raise Exception;
        finally:
            super().close(cs, con);
        return results;

    def selectone(self, id):
        con = None;
        cs = None;
        results = None;
        try:
            con = super().connect();
            cs = con.cursor();
            cs.execute(itemsql.ITEM_SELECT_ONE % (id));
            results = cs.fetchone(); # SELECT 문에서 하나를 가져와서 fetch + one
        except:
            raise Exception;
        finally:
            super().close(cs, con);
        return results;


if __name__ == '__main__':
    itemdb = ItemDb('shopdb');
    try:
        item = Item(100,'pants',10000,3.3);
        itemdb.insert(item);
    except:
        print('Insert Error')

    try:
        results = itemdb.select();
        for data in results:
            print('%d %s %d %f' % data);

    except:
        print('Error')