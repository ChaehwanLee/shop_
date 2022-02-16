#shopmodel.py
from dao import shopsql


class Shop:
    def __init__(self,id,name,money,rate): # 들어오는 데이터 저장
        self.__id = id;
        self.__name = name;
        self.__money = money;
        self.__rate = rate;

    def getid(self):
        return self.__id;
    def setid(self,id):
        self.__id = id;
    def getname(self):
        return self.__name;
    def setname(self,name):
        self.__name = name;
    def getmoney(self):
        return self.__money;
    def setmoney(self,money):
        self.__money = money;
    def getrate(self):
        return self.__rate;
    def setrate(self,rate):
        self.__rate = rate;

    def insertsql(self):
        return (shopsql.SHOP_INSERT % (self.__id,self.__name,self.__money,self.__rate))
    def updatesql(self):
        return (shopsql.SHOP_UPDATE % (self.__name,self.__money,self.__rate,self.__id))

    def __str__(self):
        return self.__id+' '+self.__name+' '+str(self.__money)+' '+str(self.__rate)