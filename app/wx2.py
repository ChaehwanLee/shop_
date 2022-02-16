# app.py
#import itemdb
from dao.itemdb import ItemDb
from model.itemmodel import Item
from dao.shopdb import ShopDb
from model.shopmodel import Shop
def start():
    while True:
        SELECT = input('무엇을 조회할까요? (상품, 개인정보 ,종료) : ')
        if SELECT == '상품':
            startitem()
        elif SELECT == '개인정보':
            startshop()
        elif SELECT == '종료':
            print('프로그램 종료')
            break

def startitem():
    itemdb = ItemDb('shopdb')
    print('Start App');

    while True:

        cmd = input('Input CMD(q,i,s,so,u,d)')
        if cmd =='q':
            break

        elif cmd == 'i':
            print('Insert Item');
            try:
                id = int(input('ID:'));
                name = input('Name : ');
                price = int(input('price : '));
                rate = float(input('rate : '));
                item = Item(id,name,price,rate)
                itemdb.insert(item)
                print('Inserted OK');
            except:
                print('Insert Error');


        elif cmd == 's':
            print('Item select');
            try:
                datas = itemdb.select();
                for data in datas:
                    print('ID : %d 이름 : %s 가격 : %d 비율 : %f' %data);
            except:
                print('Select Error')


        elif cmd == 'so':
            print('Item selectone');
            try:
                id = int(input('Input Name....'));
                data = itemdb.selectone(id);
                print('ID : %d 이름 : %s 가격 : %d 비율 : %f' % data);
            except:
                print('Select Error')


            print('select one Item');



        elif cmd == 'u':
            print('update Item');
            try:
                id = int(input('ID : '));
                name = input('Name : ');
                price = int(input('price : '));
                rate = float(input('rate : '));
                item = Item(id, name, price, rate)
                itemdb.update(item)
            except:
                print('update Error')

        elif cmd == 'd':
            print('delete Item')
            try:
                id = int(input('Input ID:'));
                itemdb.delete(id)
            except:
                print('delete Error')



    print('End App');

def startshop():
    shopdb = ShopDb('appdb')
    print('Start App');

    while True:

        cmd = input('Input CMD(q,i,s,so,u,d)')
        if cmd =='q':
            break

        elif cmd == 'i':
            print('Insert Shop');
            try:
                id = input('ID:');
                name = input('Name : ');
                money = int(input('적립금 : '));
                rate = float(input('등급 : '));
                shop = Shop(name,money,rate,id)
                shopdb.insert(shop)
                print('Inserted OK');
            except:
                print('Insert Error');


        elif cmd == 's':
            print('Shop select');
            try:
                datas = shopdb.select();
                for data in datas:
                    print('ID:%s 이름:%s 적립금:%d 등급:%1.1f급' %data);
            except:
                print('Select Error')


        elif cmd == 'so':
            print('Shop selectone');
            try:
                id = input('Input ID....');
                data = shopdb.selectone(id);
                print('ID:%s 이름:%s 적립금:%d 등급:%1.1f급' % data);
            except:
                print('Select Error')

            print('select one Data');


        elif cmd == 'u':
            print('update Shop');
            try:
                id = input('ID:');
                name = input('Name');
                money = int(input('적립금'));
                rate = float(input('등급'));
                shop = Shop(name, money, rate,id)
                shopdb.update(shop)
            except:
                print('update Error')

        elif cmd == 'd':
            print('delete Shop')
            try:
                id = input('Input ID:');
                shopdb.delete(id)
            except:
                print('delete Error')



    print('End App');

if __name__ == '__main__':
    start()