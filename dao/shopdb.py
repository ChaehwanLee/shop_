#shopdb.py

from dao import shopsql
from frame.db import Db



class ShopDb(Db):
    def __init__(self,dbname): # 초기화
        super().__init__(dbname);
        self.makeTable();# 자신의 테이블 생성 함수 호출

    def makeTable(self): # 테이블 생성 함수
        cs = None;
        con = None;
        try:
            con = self.connect();
            cs = con.cursor();
            cs.execute(shopsql.MAKE_TABLE); # 테이블 만드는 명령어 실행
            con.commit();
        except:
            print('Make Table Error');
        finally:
            self.close(cs, con);

    def insert(self, shop): # 테이블에 데이터 집어넣는 함수
        cs = None
        con = None
        try:
            con = super().connect();
            cs = con.cursor();
            cs.execute(shop.insertsql());
            con.commit();
        except:
            raise Exception;
        finally:
            super().close(cs, con);

    def select(self):
        cs = None;
        con = None;
        try:
            con = super().connect();
            cs = con.cursor();
            cs.execute(shopsql.SHOP_SELECT);
            results = cs.fetchall();
        except:
            raise Exception;
        finally:
            super().close(cs, con);
        return results

    def selectone(self,id):
        cs = None;
        con = None
        try:
            con = super().connect();
            cs = con.cursor();
            cs.execute(shopsql.SHOP_SELECT_ONE % id);
            result = cs.fetchone();
        except:
            raise Exception;
        finally:
            super().close(cs, con);
        return result

    def selectui(self):
        list = [];  # 빈 리스트 생성
        try:
            con = super().connect();
            cs = con.cursor();
            cs.execute(shopsql.SHOP_SELECT);
            results = cs.fetchall();
            for result in results:  # 각 튜플을 넣어주면서 반복
                st = '%s %s %d %1.1f'
                list.append(st % result)  # 리스트 생성
        except:
            raise Exception;
        finally:
            super().close(cs, con);
        return list

    def update(self, shop):
        cs = None;
        con = None;
        try:
            con = super().connect();
            cs = con.cursor();
            cs.execute(shop.updatesql());
            con.commit();
        except:
            raise Exception;
        finally:
            super().close(cs, con);
        return None

    def delete(self,id):
        try:
            con = super().connect();
            cs = con.cursor();
            cs.execute(shopsql.SHOP_DELETE % id);
            con.commit();
        except:
            raise Exception;
        finally:
            super().close(cs, con);
        return None

if __name__ == '__main__': # 테스트용
    shopdb = ShopDb('shopdb');

    # try:
    #     shop = Shop('101','pants',20000,3.3);
    #     shopdb.insert(shop)
    # except:
    #     print('Insert Error');
    try:
        results = shopdb.select();
        for data in results:
            print('%s %s %d %f' % data);
    except:
        print('Error')