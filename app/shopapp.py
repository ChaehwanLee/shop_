import wx;

from dao.itemdb import ItemDb
from model.itemmodel import Item
from dao.shopdb import ShopDb
from model.shopmodel import Shop

app = wx.App();
frame = wx.Frame(None, 0, 'Test');

p1 = wx.Panel(frame);
bt1 = wx.Button(p1,label='상품');
bt2 = wx.Button(p1,label='개인정보');
#bt3 = wx.Button(p1,label='Button3');
ps = wx.BoxSizer(wx.HORIZONTAL);
ps.Add(bt1);
ps.Add(bt2);
#ps.Add(bt3);
p1.SetSizer(ps);

p2 = wx.Panel(frame);
names = ['상품:상품 정보 조회, \n' '개인정보: 개인정보 조회'];
list = wx.ListBox(p2,choices = names);
list.SetSize(wx.Size(300,200))


p3 = wx.Panel(frame);
bt_add = wx.Button(p3,label='상품 정보 추가');

text1 = wx.TextCtrl(p3)
text2 = wx.TextCtrl(p3)
text3 = wx.TextCtrl(p3)
text4 = wx.TextCtrl(p3)
ps3 = wx.BoxSizer(wx.VERTICAL);
ps3.Add(bt_add);
ps3.Add(text1);
ps3.Add(text2);
ps3.Add(text3);
ps3.Add(text4);
p3.SetSizer(ps3);

p4 = wx.Panel(frame);
bt2_add = wx.Button(p4,label='개인 정보 추가');
text5 = wx.TextCtrl(p4)
text6 = wx.TextCtrl(p4)
text7 = wx.TextCtrl(p4)
text8 = wx.TextCtrl(p4)
ps4 = wx.BoxSizer(wx.VERTICAL);
ps4.Add(bt2_add);
ps4.Add(text5);
ps4.Add(text6);
ps4.Add(text7);
ps4.Add(text8);
p4.SetSizer(ps4);


def clickadd(event):
    itemdb = ItemDb('shopdb')
    id = int(text1.GetValue());
    name = text2.GetValue();
    price = int(text3.GetValue());
    rate = float(text4.GetValue());
    shops = Item(id,name,price,rate)
    try:
        itemdb = ItemDb('shopdb')
        id = int(text1.GetValue());
        name = text2.GetValue();
        price = int(text3.GetValue());
        rate = float(text4.GetValue());
        shops = Item(id, name, price, rate)
    except:
        wx.MessageBox('Fill in the blanks and press the button.', 'Alert', wx.OK)
    try:
        itemdb.insert(shops)
        text1.SetLabelText('');
        text2.SetLabelText('');
        text3.SetLabelText('');
        text4.SetLabelText('');

    except:
        wx.MessageBox('Insert Error','Alert',wx.OK)

def clickadd2(event):
    try:
        shopdb = ShopDb('appdb')
        id = text5.GetValue();
        name = text6.GetValue();
        money = int(text7.GetValue());
        rate = float(text8.GetValue());
        shops = Shop(id, name, money, rate)
    except:
        wx.MessageBox('Fill in the blanks and press the button.', 'Alert', wx.OK)
    try:
        shopdb.insert(shops)
        text5.SetLabelText('');
        text6.SetLabelText('');
        text7.SetLabelText('');
        text8.SetLabelText('');

    except:
        wx.MessageBox('Insert Error','Alert',wx.OK)
bt_add.Bind(wx.EVT_BUTTON, clickadd)
bt2_add.Bind(wx.EVT_BUTTON, clickadd2)
box = wx.BoxSizer(wx.VERTICAL);
frame.SetSizer(box);
box.Add(p1,border=10,flag=wx.DOWN);
box.Add(p2,border=10,flag=wx.UP);
box.Add(p3,border=10,flag=wx.UP);
box.Add(p4,border=10,flag=wx.UP);

def clickbt1(event):
    try:
        itemdb = ItemDb('shopdb')
        list.Clear();
        items = itemdb.selectui();
        list.AppendItems(items)
    except:
        print("No attribute")

def clickbt2(event):
    shopdb = ShopDb('appdb')
    list.Clear();
    items = shopdb.selectui();
    list.AppendItems(items)
# def clickbt3(event):
#     list.Clear();
#     items = ['999', '000', '111', '222']
#     list.AppendItems(items)

bt1.Bind(wx.EVT_BUTTON, clickbt1)
bt2.Bind(wx.EVT_BUTTON, clickbt2)
#bt3.Bind(wx.EVT_BUTTON, clickbt3)
frame.Show(True);
app.MainLoop()