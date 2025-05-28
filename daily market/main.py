"""
Daily Market
Ver 1.0.0
programmer : Aida Hasanzadeh

"""


from tkinter import *
from tkinter import ttk
import sqlite3 as sq
from tkinter import messagebox
import datetime
import pandas as pd


con=sq.Connection("Dailymarket.db")
cur=con.cursor()
cur.execute("create table if not exists customer (c_id integer primary key autoincrement,name text,lastname text,phone text)")
con.commit()
con.close()

con=sq.Connection("Dailymarket.db")
cur=con.cursor()
cur.execute("create table if not exists storage (s_id integer primary key autoincrement,product text,quantity integer,price integer)")
con.commit()
con.close()

con=sq.Connection("Dailymarket.db")
cur=con.cursor()
cur.execute("create table if not exists factor (f_id integer primary key autoincrement,f_name text,f_lastname text,f_product text,f_quantity integer,f_price integer,date text)")
con.commit()
con.close()


root=Tk()
root.title("Dailymarket")
root.geometry("365x270")


""" Main Page"""
title_lbl=Label(root,text="DAILY MARKET",font="bold").grid(row=0,column=1,padx=10)
table_lbl=Label(root,text="choose your table").grid(row=1,column=1,pady=30)
end_title = Label(root, text="programmed by Aida Hasanzadeh").grid(row=3, column=1,pady=40)

customer_btn=Button(root,text="Customer",width=10,bg="red",fg="white",command=lambda :customer()).grid(row=2,column=0,padx=5,pady=30)
storage_btn=Button(root,text="Storage",width=10,bg="blue",fg="white",command=lambda :storage()).grid(row=2,column=1)
factor_btn=Button(root,text="Factor",width=10,bg="green",fg="white",command=lambda :factor()).grid(row=2,column=2)
exl_btn = Button(root,text="Excel",command=lambda :excel()).grid(row=3,column=0,padx=5,pady=5)


""" Excel """
def excel() :
    conn = sq.connect("Dailymarket.db")
    query_tables = "SELECT name FROM sqlite_master WHERE type='table';"
    tables = pd.read_sql(query_tables, conn)

    for table_name in tables['name']:
        query_data = f"SELECT * FROM {table_name};"
        table_data = pd.read_sql(query_data, conn)
        table_data.to_csv(f"{table_name}.csv", index=False)

    conn.close()


def db_connection(cmd):
    column_name=[]
    con = sq.Connection("Dailymarket.db")
    cur = con.cursor()
    data=con.execute(cmd)

    all_headers=cur.description
    if all_headers != None:
        for i in all_headers:
            column_name.append(i[0])

    unpack_data=data.fetchall()

    con.commit()
    con.close()
    return unpack_data,column_name


"""customer"""
c_id_inp=StringVar()
name_inp=StringVar()
lastname_inp=StringVar()
phone_inp=StringVar()
search_inp=StringVar()
user_code_inp=StringVar()

select_customer = []
search_ml = []

def customer():
    top=Toplevel()
    top.geometry("900x450")
    top.title("customer management")
    style = ttk.Style()
    style.theme_use("default")
    style.configure("Treeview", rowheight=20)
    style.map([("selected", "#347083")])


    """frames"""
    frame=LabelFrame(top,text="customer management",bg="lightblue")
    frame.grid(row=1,column=0,ipady=50,ipadx=15,padx=20)
    tree_view_frame = LabelFrame(top,text="chart",bg="lightblue")
    tree_view_frame.grid(row=1, column=2,padx=5, ipady=35,ipadx=6)


    """customer treeview"""
    c_treeview = ttk.Treeview(tree_view_frame)
    c_treeview["columns"] = ("c_id", "name", "lastname", "phone")
    c_treeview.column("#0", width=1, minwidth=25, stretch=NO)
    c_treeview.column("c_id", width=40, anchor=CENTER)
    c_treeview.column("name", anchor=W, width=90)
    c_treeview.column("lastname", anchor=W, width=110)
    c_treeview.column("phone", anchor=W, width=90)


    c_treeview.heading("#0", text="LABEL", anchor=W)
    c_treeview.heading("c_id", text="ID", anchor=CENTER)
    c_treeview.heading("name", text="Name", anchor=W)
    c_treeview.heading("lastname", text="Last name", anchor=W)
    c_treeview.heading("phone", text="Phone", anchor=W)


    """labels and entries"""
    id_lbl=Label(frame,text="ID",width=8,bg="lightblue").grid(row=1,column=0,padx=5,pady=10)
    id_entry=Entry(frame,textvariable=c_id_inp).grid(row=1,column=1)

    name_lbl = Label(frame,text="Name",bg="lightblue").grid(row=2, column=0,padx=5,pady=10)
    name_entey = Entry(frame,textvariable=name_inp).grid(row=2, column=1)

    lastname_lbl = Label(frame,text="Last Name",bg="lightblue",width=10).grid(row=3, column=0,padx=5,pady=10)
    lastname_entry = Entry(frame,textvariable=lastname_inp).grid(row=3, column=1)

    phone_lbl = Label(frame,text="Phone",width=10,bg="lightblue").grid(row=4, column=0,padx=5,pady=10)
    phone_entry = Entry(frame,textvariable=phone_inp).grid(row=4, column=1)

    search_lbl = Label(tree_view_frame, text="Search Customer", bg="lightblue").grid(row=0, column=0,padx=10, pady=30)
    search_entry = Entry(tree_view_frame,textvariable=search_inp).grid(row=0, column=2,ipadx=30)


    """buttons"""
    add_btn=Button(frame,text="Add",width=8,activebackground="blue",bd=3,command=lambda :c_add()).grid(row=8,column=0,padx=5,pady=15)
    edite_btn=Button(frame,text="Edite",width=8,activebackground="blue",bd=3,command=lambda :c_update()).grid(row=8,column=1)
    delete_btn=Button(frame,text="Delete",width=8,activebackground="blue",bd=3,command=lambda:c_delete()).grid(row=9,column=0,padx=7)
    search_lbl = Label(frame, bg="lightblue").grid(row=6, column=0,padx=10, pady=20)
    search_btn=Button(tree_view_frame,text="Search",activebackground="blue",bd=3,command=lambda :c_search()).grid(row=0,column=3)
    showall_btn=Button(tree_view_frame,text="Show All",activebackground="blue",bd=3,command=lambda :c_show_all()).grid(row=0,column=4,padx=8)


    def c_show_all():
        clear(None)
        c_select()
        count = 0
        for i in select_customer:
            c_treeview.insert(parent="", index="end", iid=str(count), values=(i[0], i[1], i[2], i[3]))
            count += 1


    def c_add():
        try:
            name = name_inp.get()
            lastname = lastname_inp.get()
            phone = phone_inp.get()

            cmd = f"""insert into customer (name,lastname,phone) values('{name}','{lastname}','{phone}') """
            db_connection(cmd)
            c_show_all()
        except:
            pass

    def c_delete():
        try:
            phone = phone_inp.get()

            cmd = f"""delete from customer where phone='{phone}' """
            db_connection(cmd)
            c_show_all()
        except:
            messagebox.showinfo("ERROR","There is no customer with this ID")


    def c_update():
        try:
            id = int(c_id_inp.get())
            name = name_inp.get()
            lastname = lastname_inp.get()
            phone = phone_inp.get()

            cmd = f"""update customer set name='{name}',lastname='{lastname}',phone='{phone}' where c_id={id} """
            db_connection(cmd)
            c_show_all()
        except:
            pass


    def c_search():
        try:
            clear(None)
            c_main_search()
            count = 0
            for i in search_ml:
                c_treeview.insert(parent="", index="end", iid=str(count), values=(i[0], i[1], i[2], i[3]))
                count += 1
        except:
            messagebox.showinfo("ERROR", "There is no customer with this phone number")


    def clear(index):
        if index == None:
            select_customer.clear()
            for i in c_treeview.get_children():
                c_treeview.delete(i)
        else:
            c_treeview.delete(index)
            select_customer.remove(index)

    c_treeview.grid(row=1, column=2,pady=20)
    top.mainloop()


def c_select():
    cmd = """ SELECT * FROM customer """
    cmd = db_connection(cmd)
    for i in cmd:
        select_customer.extend(i)


def c_main_search():
    search=search_inp.get()

    cmd=f"""select * from customer where phone='{search}' """
    cmd=db_connection(cmd)
    for i in cmd:
        search_ml.extend(i)






"""""storage"""""
s_id_inp=StringVar()
product_inp=StringVar()
quantity_inp=StringVar()
price_inp=StringVar()
s_search_inp = StringVar()

select_storage = []
search_storage_ml = []

def storage():
    top = Toplevel()
    top.geometry("900x450")
    top.title("Storage Management")
    style = ttk.Style()
    style.theme_use("default")
    style.configure("Treeview", rowheight=20)
    style.map([("selected", "#347083")])


    """frames"""
    frame = LabelFrame(top, text="storage management", bg="lightblue")
    frame.grid(row=1, column=0, ipady=40, ipadx=25, padx=20)
    tree_view_frame = LabelFrame(top, text="chart", bg="lightblue")
    tree_view_frame.grid(row=1, column=2, padx=5, ipady=35, ipadx=8)


    """storage treeview"""
    s_treeview = ttk.Treeview(tree_view_frame)
    s_treeview["columns"] = ("s_id", "product", "quantity", "price")
    s_treeview.column("#0", width=1, minwidth=25, stretch=NO)
    s_treeview.column("s_id", width=40, anchor=CENTER)
    s_treeview.column("product", anchor=W, width=90)
    s_treeview.column("quantity", anchor=W, width=90)
    s_treeview.column("price", anchor=W, width=90)

    s_treeview.heading("#0", text="LABEL", anchor=W)
    s_treeview.heading("s_id", text="ID", anchor=CENTER)
    s_treeview.heading("product", text="Product", anchor=W)
    s_treeview.heading("quantity", text="Quantity", anchor=W)
    s_treeview.heading("price", text="Price", anchor=W)


    """labels and entries"""
    id_lbl = Label(frame, text="ID",bg="lightblue").grid(row=1, column=0,padx=5,pady=10)
    id_entery = Entry(frame,textvariable=s_id_inp).grid(row=1, column=1,padx=5)

    product_lbl = Label(frame, text="Product",bg="lightblue").grid(row=2, column=0,padx=5,pady=10)
    product_entery = Entry(frame,textvariable=product_inp).grid(row=2, column=1,padx=5)

    quantity_lbl = Label(frame, text="Quantity", bg="lightblue").grid(row=4, column=0,padx=5,pady=10)
    quantity_entery = Entry(frame,textvariable=quantity_inp).grid(row=4, column=1,padx=5)

    price_lbl = Label(frame, text="Price", bg="lightblue").grid(row=5, column=0,padx=5,pady=10)
    price_entery = Entry(frame,textvariable=price_inp).grid(row=5, column=1,padx=5)

    search_lbl = Label(tree_view_frame, text="Search Product", bg="lightblue").grid(row=0, column=0, padx=10, pady=30)
    search_entry = Entry(tree_view_frame,textvariable=s_search_inp).grid(row=0, column=2, ipadx=30)


    """buttons"""
    add_btn = Button(frame, text="Add", width=8, activebackground="blue", bd=3, command=lambda: s_add()).grid(row=8,column=0,padx=5,pady=15)
    edite_btn = Button(frame, text="Edite", width=8, activebackground="blue", bd=3, command=lambda: s_update()).grid(row=8, column=1)
    delete_btn = Button(frame, text="Delete", width=8, activebackground="blue", bd=3, command=lambda: s_delete()).grid(row=9, column=0, padx=7)
    search_lbl = Label(frame, bg="lightblue").grid(row=6, column=0, padx=10, pady=30)
    search_btn = Button(tree_view_frame, text="Search", activebackground="blue", bd=3, command=lambda: s_search()).grid(row=0, column=3)
    showall_btn = Button(tree_view_frame, text="Show All", activebackground="blue", bd=3,command=lambda: s_show_all()).grid(row=0, column=4, padx=8)


    def s_show_all() :
        s_clear(None)
        s_select()
        count = 0
        for i in select_storage :
            s_treeview.insert(parent="", index="end", iid=str(count), values=(i[0],i[1],i[2],i[3]))
            count += 1


    def s_add():
        try:
            product=product_inp.get()
            quantity=int(quantity_inp.get())
            price=int(price_inp.get())

            cmd = f"""insert into storage (product,quantity,price) values('{product}',{quantity},{price}) """
            db_connection(cmd)
            s_show_all()
        except:
            pass


    def s_delete():
        try:
            id = int(s_id_inp.get())

            cmd = f"""delete from storage where s_id={id}"""
            db_connection(cmd)
            s_show_all()
        except:
            messagebox.showinfo("Error", "There is no one with this ID")


    def s_update():
        try:
            id=int(s_id_inp.get())
            product=product_inp.get()
            quantity=int(quantity_inp.get())
            price=int(price_inp.get())

            cmd=f"""update storage set product='{product}',quantity={quantity},price={price} where s_id={id}"""
            db_connection(cmd)
            s_show_all()
        except:
            pass


    def s_search() :
        try:
            s_clear(None)
            s_main_search()
            count = 0
            for i in search_storage_ml:
                s_treeview.insert(parent="", index="end", iid=str(count), values=(i[0], i[1], i[2], i[3]))
                count += 1
        except:
            messagebox.showinfo("Error", "There is no product with this ID")


    def s_clear(index):
        if index == None:
            select_storage.clear()
            for i in s_treeview.get_children():
                s_treeview.delete(i)
        else:
            s_treeview.delete(index)
            select_storage.remove(index)

    s_treeview.grid(row=1, column=2,pady=20)
    top.mainloop()


def s_select() :
    cmd = """ select * from storage """
    cmd = db_connection(cmd)
    for i in cmd :
        select_storage.extend(i)


def s_main_search():
    s_search=int(s_search_inp.get())

    cmd=f"""select * from storage where s_id={s_search} """
    cmd=db_connection(cmd)
    for i in cmd:
        search_storage_ml.extend(i)




"""factor"""
f_id_inp = StringVar()
f_name_inp = StringVar()
f_lastname_inp = StringVar()
f_product_inp = StringVar()
f_quantity_inp = StringVar()
f_price_inp = StringVar()
date_inp = StringVar()
print_id_factor = StringVar()
print_factor_inp = StringVar()

select_ml = []
search_factor_ml = []
join_ml = []
factor_time = datetime.datetime.now().strftime("%Y-%m-%d")

def factor():
    top = Toplevel()
    top.geometry("1143x500")
    top.title("factor management")
    style = ttk.Style()
    style.theme_use("default")
    style.configure("Treeview", rowheight=20)
    style.map([("selected", "#347083")])


    """frames"""
    f_frame = LabelFrame(top, text="factor management", bg="lightblue")
    f_frame.grid(row=1, column=0, ipady=40, ipadx=25, padx=20)
    f_treeview_frame = LabelFrame(top, text="chart", bg="lightblue")
    f_treeview_frame.grid(row=1, column=2, padx=5, ipady=40, ipadx=3)


    """factor treeview"""
    f_treeview = ttk.Treeview(f_treeview_frame)
    f_treeview["columns"] = ("f_id", "name", "lastname", "product", "quantity", "price", "date")
    f_treeview.column("#0", width=1, minwidth=25, stretch=NO)
    f_treeview.column("f_id", width=40, anchor=CENTER)
    f_treeview.column("name", anchor=W, width=70)
    f_treeview.column("lastname", anchor=W, width=100)
    f_treeview.column("product", anchor=W, width=90)
    f_treeview.column("quantity", anchor=CENTER, width=70)
    f_treeview.column("price", anchor=W, width=70)
    f_treeview.column("date", anchor=W, width=100)

    f_treeview.heading("#0", text="LABEL", anchor=W)
    f_treeview.heading("f_id", text="ID", anchor=CENTER)
    f_treeview.heading("name", text="name", anchor=W)
    f_treeview.heading("lastname", text="lastname", anchor=W)
    f_treeview.heading("product", text="Product", anchor=W)
    f_treeview.heading("quantity", text="quantity", anchor=W)
    f_treeview.heading("price", text="Price", anchor=W)
    f_treeview.heading("date", text="date", anchor=W)


    """labels and entries"""
    id_lbl = Label(f_frame, text="ID", bg="lightblue").grid(row=1, column=0, padx=5, pady=10)
    id_entery = Entry(f_frame, textvariable=f_id_inp).grid(row=1, column=1, padx=5)

    product_lbl = Label(f_frame, text="Name", bg="lightblue").grid(row=2, column=0, padx=5, pady=10)
    product_entery = Entry(f_frame, textvariable=f_name_inp).grid(row=2, column=1, padx=5)

    product_lbl = Label(f_frame, text="Lastname", bg="lightblue").grid(row=3, column=0, padx=5, pady=10)
    product_entery = Entry(f_frame, textvariable=f_lastname_inp).grid(row=3, column=1, padx=5)

    product_lbl = Label(f_frame, text="Product", bg="lightblue").grid(row=4, column=0, padx=5, pady=10)
    product_entery = Entry(f_frame, textvariable=f_product_inp).grid(row=4, column=1, padx=5)

    quantity_lbl = Label(f_frame, text="Quantity", bg="lightblue").grid(row=5, column=0, padx=5, pady=10)
    quantity_entery = Entry(f_frame, textvariable=f_quantity_inp).grid(row=5, column=1, padx=5)

    price_lbl = Label(f_frame, text="Price", bg="lightblue").grid(row=6, column=0, padx=5, pady=10)
    pricet_entery = Entry(f_frame, textvariable=f_price_inp).grid(row=6, column=1, padx=5)

    search_lbl = Label(f_treeview_frame, text="Search Factor", bg="lightblue").grid(row=0, column=0, padx=10, pady=20)
    search_entry = Entry(f_treeview_frame,width=30, textvariable=date_inp).grid(row=0, column=1, ipadx=20)

    factor_id_label = Label(f_treeview_frame, text="insert factor ID", bg="lightblue").grid(row=2, column=0, padx=10,pady=30)
    factor_id_entry = Entry(f_treeview_frame, width=30, textvariable=print_factor_inp).grid(row=2, column=1, pady=20,ipadx=20)


    """buttons"""
    add_btn = Button(f_frame, text="Add", width=8, activebackground="blue", bd=3, command=lambda: f_add()).grid(row=8, column=0, padx=5, pady=40)
    edite_btn = Button(f_frame, text="Edite", width=8, activebackground="blue", bd=3, command=lambda:f_update()).grid(row=8, column=1)
    delete_btn = Button(f_frame, text="Delete", width=8, activebackground="blue", bd=3, command=lambda: f_delete()).grid(row=9, column=0, padx=7)
    search_btn = Button(f_treeview_frame,text="Search", activebackground="blue", bd=3,width=7, command=lambda: f_search()).grid(row=0, column=3)
    showall_btn = Button(f_treeview_frame, text="Show All", activebackground="blue", bd=3,width=7,command=lambda: f_show_all()).grid(row=0, column=4,padx=5)
    print_btn = Button(f_treeview_frame,text="print factor",activebackground="blue",bd=3,width=9,command=lambda :print_factor()).grid(row=2,column=3)


    def f_show_all() :
        f_clear(None)
        select_factor()
        count = 0
        for i in select_ml :
            f_treeview.insert(parent="", index="end", iid=str(count), values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
            count += 1


    def f_add() :
        try:
            name = f_name_inp.get()
            lastname = f_lastname_inp.get()
            product = f_product_inp.get()
            quantity = f_quantity_inp.get()
            price = f_price_inp.get()

            cmd = f""" insert into factor (f_name , f_lastname , f_product ,f_quantity ,f_price ,date ) values('{name}','{lastname}','{product}',{quantity},{price},'{factor_time}')   """
            db_connection(cmd)
            f_show_all()
        except:
            pass


    def f_delete() :
        try:
            id = int(f_id_inp.get())

            cmd = f""" delete from factor where f_id = {id}  """
            db_connection(cmd)
            f_show_all()
        except:
            messagebox.showinfo("Error", "There is no factor with this ID")



    def f_update() :
        try:
            name = f_name_inp.get()
            lastname = f_lastname_inp.get()
            product = f_product_inp.get()
            quantity = f_quantity_inp.get()
            price = f_price_inp.get()
            id = int(f_id_inp.get())

            cmd = f""" update factor set f_name='{name}',f_lastname='{lastname}',f_product='{product}',f_quantity={quantity},f_price={price} where f_id={id} """
            db_connection(cmd)
            f_show_all()
        except:
            pass


    def f_search():
        try:
            f_clear(None)
            f_main_search()
            count = 0
            for i in search_factor_ml:
                f_treeview.insert(parent="", index="end", iid=str(count), values=(i[0], i[1], i[2], i[3],i[4],i[5],i[6]))
                count += 1
        except:
            messagebox.showinfo("Error", "There is no factor on this date")


    def f_select():
        id = int(print_id_factor.get())

        cmd = f""" select f_id ,  name , "_" , product ,f_quantity ,f_price ,date FROM factor where  f_id={id}   """
        cmd = db_connection(cmd)
        for i in cmd:
            join_ml.extend(i)


    def f_clear(index):
        if index == None:
            select_ml.clear()
            for i in f_treeview.get_children():
                f_treeview.delete(i)
        else:
            f_treeview.delete(index)
            select_ml.remove(index)


    f_treeview.grid(row=1, column=1,pady=10)
    top.mainloop()


def select_factor() :
    cmd = f""" select * from factor """
    cmd = db_connection(cmd)
    for i in cmd :
        select_ml.extend(i)


def f_main_search():
    date=date_inp.get()

    cmd = f""" select  f_id ,f_name ,f_lastname ,f_product ,f_quantity ,f_price ,date  from factor where  date='{date}' """
    cmd = db_connection(cmd)
    for i in cmd:
        search_factor_ml.extend(i)


"""print factor"""
print_factor_ml=[]

def print_factor():
    top2 = Toplevel()
    top2.geometry("550x240")
    top2.title("factor")
    style = ttk.Style()
    style.theme_use("default")
    style.configure("Treeview", rowheight=20)
    style.map([("selected", "#347083")])

    """print factor treeview"""
    fc_treeview = ttk.Treeview(top2)
    fc_treeview["columns"] = ("name", "lastname", "product", "quantity", "price", "date")
    fc_treeview.column("#0", width=1, minwidth=25, stretch=NO)
    fc_treeview.column("name", anchor=W, width=70)
    fc_treeview.column("lastname", anchor=W, width=100)
    fc_treeview.column("product", anchor=W, width=90)
    fc_treeview.column("quantity", anchor=CENTER, width=70)
    fc_treeview.column("price", anchor=W, width=70)
    fc_treeview.column("date", anchor=W, width=100)

    fc_treeview.heading("#0", text="LABEL", anchor=W)
    fc_treeview.heading("name", text="name", anchor=W)
    fc_treeview.heading("lastname", text="lastname", anchor=W)
    fc_treeview.heading("product", text="Product", anchor=W)
    fc_treeview.heading("quantity", text="quantity", anchor=W)
    fc_treeview.heading("price", text="Price", anchor=W)
    fc_treeview.heading("date", text="date", anchor=W)


    def print_select_factor():
        try:
            id=int(print_factor_inp.get())

            cmd=f""" select name,lastname,f_product,f_quantity,f_price,date from factor join storage on factor.f_product = storage.product join customer on factor.f_name = customer.name where f_id={id}"""
            cmd=db_connection(cmd)
            for i in cmd:
                print_factor_ml.extend(i)
        except:
            messagebox.showinfo("Error", "Re check your entries")


    def fc_clear(index):
        if index == None:
            print_factor_ml.clear()
            for i in fc_treeview.get_children():
                fc_treeview.delete(i)
        else:
            fc_treeview.delete(index)
            print_factor_ml.remove(index)


    fc_clear(None)
    print_select_factor()
    count = 0
    for i in print_factor_ml:
        fc_treeview.insert(parent="", index="end", iid=str(count), values=(i[0], i[1], i[2], i[3], i[4], i[5]))
        count += 1



    fc_treeview.grid(row=0, column=0, padx=21)
    top2.mainloop()

root.mainloop()
