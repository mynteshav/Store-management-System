from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



class stockClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x500+100+255")
        self.root.title("Shoe Shop Management System |Develop By Teshav")
        self.root.config(bg="white")
        self.root.focus_force()
        self.root.resizable(False, False)
        supmenu = Frame(self.root, bd=4, relief=RIDGE, bg='black')
        supmenu.place(x=0, y=0, width=1350, height=500)
        self.lbl_st=Label(self.root,text="Stock Details",font=("goudy old style",28,"bold"),bg="black",fg="blue")
        self.lbl_st.place(x=470,y=15,width=400,height=50)
        self.icon_side = Image.open("shoe.png")
        self.icon_side = self.icon_side.resize((283, 492), Image.LANCZOS)
        self.icon_side = ImageTk.PhotoImage(self.icon_side)
        lbl_menu = Label(self.root,image=self.icon_side, bg='black').place(x=4,y=4,width=283,height=492)
        self.line_style = ttk.Style()
        self.line_style.configure("Line.TSeparator", background="darkgrey")
        self.separator = ttk.Separator(self.root, orient='vertical', style="Line.TSeparator")
        self.separator.place(x=1066, y=4, width=3, height=493)
        self.line_style = ttk.Style()
        self.line_style.configure("Line.TSeparator", background="darkgrey")
        self.separator = ttk.Separator(self.root, orient='vertical', style="Line.TSeparator")
        self.separator.place(x=286, y=4, width=3, height=493)
        self.line_style = ttk.Style()
        self.line_style.configure("Line.TSeparator", background="darkgrey")
        self.separator = ttk.Separator(self.root, orient='horizontal', style="Line.TSeparator")
        self.separator.place(x=287, y=360, width=780, height=3)

        # All variable======
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        self.var_shoe_id = StringVar()
        self.var_type = StringVar()
        self.var_brand = StringVar()
        self.var_product_for = StringVar()
        self.var_price = StringVar()
        self.var_size = StringVar()
        self.var_qty = StringVar()
        #===========================================|search stock|===========================
        searchframe = LabelFrame(self.root, text="Search Stock", font=("goudy old style", 16, "bold"),
                                 bg='black', fg="blue")
        searchframe.place(x=370, y=70, width=600, height=90)
        # ===options====
        cmb_search = ttk.Combobox(searchframe, textvariable=self.var_searchby,
                                  values=("Select", "Brand", "price"), state='readonly', justify=CENTER,
                                  font=("goudy old style", 15, "bold"))
        cmb_search.place(x=10, y=8, width=180)
        cmb_search.current(0)
        txt_search = Entry(searchframe, textvariable=self.var_searchtxt, font=('goudy old style', 15),
                           bg="lightyellow").place(x=200, y=8)
        btn_search = Button(searchframe, text="Search",command=self.search, font=('goudy old style', 15), bg="green",
                            fg='white', cursor='hand2').place(x=430, y=8, height=30, width=120)
        #=========row1======================================
        lbl_shoeid = Label(self.root, text="Shoe ID.", font=("goudy old style", 16, "bold"), bg="black", fg="blue").place(
            x=300,
            y=200)
        lbl_productfor = Label(self.root, text="Gender", font=("goudy old style", 16, "bold"), bg="black", fg="blue").place(
            x=560,
            y=200)
        lbl_brand = Label(self.root, text="Brand", font=("goudy old style", 16, "bold"), bg="black",
                            fg="blue").place(x=820, y=200)

        txt_shoeid = Entry(self.root, textvariable=self.var_shoe_id, font=("goudy old style", 16, "bold"),
                          bg="lightyellow", fg="black").place(x=400, y=200, width=150)
        cmb_productfor = ttk.Combobox(self.root, textvariable=self.var_product_for, values=("Select", "Male", "Female","Boys","Girls", "kids"),
                                  state='readonly', justify=CENTER, font=("goudy old style", 15, "bold"))
        cmb_productfor.place(x=640, y=200, width=150)
        cmb_productfor.current(0)
        cmb_brand =ttk.Combobox(self.root, textvariable=self.var_brand, values=("Select", "Adidas", "Nike","Puma","Rebook", "Jordan"),
                                  state='readonly', justify=CENTER, font=("goudy old style", 15, "bold"))
        cmb_brand.place(x=900, y=200, width=150)
        cmb_brand.current(0)

        #====================row2===========
        lbl_stype = Label(self.root, text="Shoe Type.", font=("goudy old style", 16, "bold"), bg="black",
                           fg="blue").place(
            x=300,
            y=250)
        lbl_price = Label(self.root, text="Price", font=("goudy old style", 16, "bold"), bg="black",
                               fg="blue").place(
            x=570,
            y=250)
        lbl_size = Label(self.root, text="Shoe Size", font=("goudy old style", 16, "bold"), bg="black",
                          fg="blue").place(x=820, y=250)

        cmb_productfor = ttk.Combobox(self.root, textvariable=self.var_type,
                                      values=("Select", "Loafer", "Sneakers", "Boots", "Sandal", "Ballet flats","Sports Shoe"),
                                      state='readonly', justify=CENTER, font=("goudy old style", 15, "bold"))
        cmb_productfor.place(x=400, y=250, width=150)
        cmb_productfor.current(0)

        txt_price = Entry(self.root, textvariable=self.var_price, font=("goudy old style", 16, "bold"),
                           bg="lightyellow", fg="black").place(x=640, y=250, width=150)

        txt_ssize = Entry(self.root, textvariable=self.var_size, font=("goudy old style", 16, "bold"),
                           bg="lightyellow", fg="black").place(x=910, y=250, width=140)
        #=============row 3=====================================
        lbl_qty = Label(self.root, text="Quantity.", font=("goudy old style", 16, "bold"), bg="black",
                          fg="blue").place(
            x=300,
            y=300)
        txt_qty = Entry(self.root, textvariable=self.var_qty, font=("goudy old style", 16, "bold"),
                          bg="lightyellow", fg="black").place(x=400, y=300, width=150)
        #===========buttons====================
        btn_frm = Frame(self.root, bd=3, relief=RIDGE, bg='black')
        btn_frm.place(x=645, y=310, width=410, height=38)
        btn_add = Button(self.root, text="Save",command=self.add, font=('goudy old style', 15), bg="#2196f3",
                         fg='white', cursor='hand2').place(x=650, y=315, height=28, width=100)
        btn_update = Button(self.root, text="Update",command=self.update, font=('goudy old style', 15), bg="green",
                            fg='white', cursor='hand2').place(x=750, y=315, height=28, width=100)
        btn_delete = Button(self.root, text="Delete",command=self.delete, font=('goudy old style', 15), bg="red",
                            fg='white', cursor='hand2').place(x=850, y=315, height=28, width=100)
        btn_clear = Button(self.root, text="Clear", font=('goudy old style', 15), bg="#607d8b",
                           fg='white', cursor='hand2').place(x=950, y=315, height=28, width=100)
        #============images=========================
        self.icon_side1 = Image.open("se.jfif")
        self.icon_side1 = self.icon_side1.resize((150, 132), Image.LANCZOS)
        self.icon_side1 = ImageTk.PhotoImage(self.icon_side1)
        lbl_menu1 = Label(self.root, image=self.icon_side1, bg='black').place(x=290, y=364, width=150, height=132)
        self.icon_side2 = Image.open("re.jfif")
        self.icon_side2 = self.icon_side2.resize((150, 132), Image.LANCZOS)
        self.icon_side2 = ImageTk.PhotoImage(self.icon_side2)
        lbl_menu2 = Label(self.root, image=self.icon_side2, bg='black').place(x=440, y=364, width=150, height=132)
        self.icon_side3 = Image.open("nike.jfif")
        self.icon_side3 = self.icon_side3.resize((150, 132), Image.LANCZOS)
        self.icon_side3 = ImageTk.PhotoImage(self.icon_side3)
        lbl_menu3 = Label(self.root, image=self.icon_side3, bg='black').place(x=590, y=364, width=150, height=132)
        self.icon_side4 = Image.open("Logo Puma.jpg")
        self.icon_side4 = self.icon_side4.resize((150, 132), Image.LANCZOS)
        self.icon_side4 = ImageTk.PhotoImage(self.icon_side4)
        lbl_menu4 = Label(self.root, image=self.icon_side4, bg='black').place(x=740, y=364, width=150, height=132)
        self.icon_side5 = Image.open("the-4th-logo-1024x862.jpg")
        self.icon_side5 = self.icon_side5.resize((175, 132), Image.LANCZOS)
        self.icon_side5 = ImageTk.PhotoImage(self.icon_side5)
        lbl_menu4 = Label(self.root, image=self.icon_side5, bg='black').place(x=890, y=364, width=175, height=132)
        #==============graph button==========================
        btn_graph=Button(self.root,text="graph",command=self.graph)
        btn_graph.place(x=1070,y=4,width=276,height=26)
        #=================stock Details============
        stock_frame = Frame(self.root, bd=3, relief=RIDGE)
        stock_frame.place(x=1070, y=30, width=276, height=467)
        scrolly = Scrollbar(stock_frame, orient=VERTICAL)
        scrollx = Scrollbar(stock_frame, orient=HORIZONTAL)
        self.StockTable = ttk.Treeview(stock_frame, columns=(
            'shoe_id', 'Type', 'Brand', 'product_for', 'price', 'size', 'Quantity'),
                                          yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.StockTable.xview)
        scrolly.config(command=self.StockTable.yview)
        self.StockTable.heading('shoe_id', text="SHOE ID")
        self.StockTable.heading('Type', text="Type of Shoe")
        self.StockTable.heading('Brand', text="Brand")
        self.StockTable.heading('product_for', text="Gender")
        self.StockTable.heading('price', text="Price")
        self.StockTable.heading('size', text="Size")
        self.StockTable.heading('Quantity', text="Quantity")
        self.StockTable["show"] = 'headings'
        self.StockTable.column('shoe_id', width=90)
        self.StockTable.column('Type', width=100)
        self.StockTable.column('Brand', width=100)
        self.StockTable.column('product_for', width=100)
        self.StockTable.column('price', width=100)
        self.StockTable.column('size', width=100)
        self.StockTable.column('Quantity', width=100)
        self.StockTable.pack(fill=BOTH, expand=1)
        self.StockTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()

    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_shoe_id.get() == "":
                messagebox.showerror('Error', "Shoe ID Must be required", parent=self.root)
            else:
                cur.execute("select * from stock where shoe_id=?", (self.var_shoe_id.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "This Shoe ID already assigned,try different", parent=self.root)
                else:
                    cur.execute(
                        "Insert into stock(shoe_id,type,brand,product_for,price,ssize,sqty) values(?,?,?,?,?,?,?)",
                        (
                            self.var_shoe_id.get(),
                            self.var_type.get(),
                            self.var_brand.get(),
                            self.var_product_for.get(),
                            self.var_price.get(),
                            self.var_size.get(),
                            self.var_qty.get(),

                        ))
                    con.commit()
                    messagebox.showinfo("Success", "Stock Addedd Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to:{str(ex)}", parent=self.root)

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select * from stock")
            rows = cur.fetchall()
            self.StockTable.delete(*self.StockTable.get_children())
            for row in rows:
                self.StockTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to:{str(ex)}", parent=self.root)

    def get_data(self, ev):
        f = self.StockTable.focus()
        content = (self.StockTable.item(f))
        row = content['values']
        # print(row)
        self.var_shoe_id.set(row[0]),
        self.var_type.set(row[1]),
        self.var_brand.set(row[2]),
        self.var_product_for.set(row[3]),
        self.var_price.set(row[4]),
        self.var_size.set(row[5]),
        self.var_qty.set(row[6]),
    def update(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_shoe_id.get() == "":
                messagebox.showerror('Error', "Shoe ID Must be required", parent=self.root)
            else:
                cur.execute("select * from stock where shoe_id=?", (self.var_shoe_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Shoe ID", parent=self.root)
                else:
                    cur.execute(
                        "update employee set type=?,brand=?,product_for=?,price=?,size=?,qty=? where shoe_id=? ",
                        (

                            self.var_type.get(),
                            self.var_brand.get(),
                            self.var_product_for.get(),
                            self.var_price.get(),
                            self.var_size.get(),
                            self.var_qty.get(),

                        ))
                    con.commit()
                    messagebox.showinfo("Success", "Stock Updated Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to:{str(ex)}", parent=self.root)
    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_shoe_id.get() == "":
                messagebox.showerror('Error', "Shoe ID Must be required", parent=self.root)
            else:
                cur.execute("select * from stock where shoe_id=?", (self.var_shoe_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Shoe ID", parent=self.root)
                else:
                    op = messagebox.askyesno("Conform", "Do you really want to delete ?", parent=self.root)
                    if op == True:
                        cur.execute("delete from stock where  shoe_id=?", (self.var_shoe_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Stock Deleted Successfully", parent=self.root)
                        self.clear()



        except Exception as ex:
            messagebox.showerror("Error", f"Error due to:{str(ex)}", parent=self.root)
    def clear(self):
        self.var_shoe_id.set(""),
        self.var_type.set(""),
        self.var_brand.set(""),
        self.var_product_for.set("Select"),
        self.var_price.set(""),
        self.var_size.set(""),
        self.var_qty.set(""),
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show()
    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_searchby.get() == "Select":
                messagebox.showerror("Error", "Select Search By option", parent=self.root)
            elif self.var_searchtxt.get() == "":
                messagebox.showerror("Error", "Search input should be required", parent=self.root)

            else:
                cur.execute(
                    "select * from stock where " + self.var_searchby.get() + " LIKE '%" + self.var_searchtxt.get() + "%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.StockTable.delete(*self.StockTable.get_children())
                    for row in rows:
                        self.StockTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found!!!", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to:{str(ex)}", parent=self.root)

    def graph(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        Q=('select brand,price from stock group by brand')
        cur.execute(Q)
        F = cur.fetchall()
        Df = pd.DataFrame(F, columns=[ 'brand','price'])
        plt.pie(Df['price'],labels=Df['brand'],colors=['r','b','g','c','k'],
                autopct='%1.f%%',shadow=True,startangle=140)
        plt.axis('equal')
        plt.legend(Df['brand'],loc='best')
        plt.title('WHICH BRAND WAS MORE PURCHASE', fontsize=13.0)
        plt.show()
           

if __name__ == "__main__":
    root = Tk()
    obj = stockClass(root)
    root.mainloop()
