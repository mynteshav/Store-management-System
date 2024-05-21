import sqlite3
def create_db():
    con=sqlite3.connect(database=r'ims.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,gender text,contact text,dob text,doj text,pass text,utype text,address text,salary text)")
    #.execute('create table if not exists stock(Shoe_Id char(10) primary key , type char(30), brand varchar(10),product_for varchar(20),price int(5),ssize int(6),sqty int(5));')
    cur.execute("CREATE TABLE IF NOT EXISTS stock(shoe_id INTEGER PRIMARY KEY AUTOINCREMENT,type text,brand text,product_for text,price text,ssize text,sqty text)")

    con.commit()



create_db()