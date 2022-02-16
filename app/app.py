# app.py
#import itemdb
from dao.itemdb import ItemDb
from model.itemmodel import Item

def start():
    itemdb = ItemDb('shopdb');
    print('Start App');
    while True:


        cmd = input('Input CMD(q,i,s,so,u,d)')
        if cmd =='q':
            break

        elif cmd == 'i':
            print('Insert Item');
            try:
                id = int(input('ID:'));
                name = input('Name');
                price = int(input('price'));
                rate = float(input('Float'));
                item = Item(id,name,price,rate);
                itemdb.insert(item);
                print('Inserted OK');
            except Exception as e:
                print('Insert Error');


        elif cmd == 's':
            print('Item select');
            try:
                datas = itemdb.select();
                for data in datas:
                    print('%d %s %d %f' %data); # 받아온걸 출력했구나
            except:
                print('Select Error')


        elif cmd == 'so':
            print('Item selectone');
            try:
                name = input('Input Name....');
                #datas = itemdb.selectone(name);
                print('%d %s %d %f' % data);
            except:
                print('Select Error')


            print('select one Item');



        elif cmd == 'u':
            print('update Item');
            try:
                id = int(input('ID:')); # 수정불가
                name = input('Name');
                price = int(input('price'));
                rate = float(input('Float'));
                itemdb.update(id,name,price,rate);
            except:
                print('update Error')

        elif cmd == 'd':
            print('delete Item')
            try:
                id = input('Input name:');
                #itemdb.delete(id)
            except:
                print('delete Error')



    print('End App');

if __name__ == '__main__':
    start()
