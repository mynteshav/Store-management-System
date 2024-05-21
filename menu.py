from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from employee import employeeClass
from stock import stockClass
from category import categoryClass
from product import productClass
from sales import salesClass
class IMG:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+100+50")
        self.root.title("Shoe Shop Management System |Develop By Teshav")
        self.root.config(bg="#262626")
        self.root.resizable(False,False)
        #main_menu:-
        leftmenu = Frame(self.root, bd=2, relief=RIDGE, bg='black')
        leftmenu.place(x=0, y=0, width=1350, height=700)
        self.headingm = Label(self.root, text="  Shoe Shop Management System", font=("Angerian", 60, "bold"), fg="blue",
                              bg="black")
        self.headingm.place(x=0, y=0)
        self.show = Image.open("storeVector.png")
        self.show = self.show.resize((1350, 500), Image.LANCZOS)
        self.show = ImageTk.PhotoImage(self.show)

        l_logo = Label(self.root, image=self.show, bd=0)
        l_logo.place(x=-250, y=150)
        # ===clock===
        self.lbl_clock = Label(self.root,text="Date: DD-MM-YYYY \t\tWelcome to Shoe Shop Management System\t\tTime: HH:MM:SS",font=('times new roman', 20), bg='#4d636d', fg='white')
        self.lbl_clock.place(x=0, y=100, relwidth=1, height=40)
        #logout btn==========

        funmenu = Frame(self.root, bd=2, relief=RIDGE, bg='black')
        funmenu.place(x=0, y=141, width=1350, height=35)
        #self.icon_side = Image.open("double.png")
        #self.icon_side = self.icon_side.resize((20, 20), Image.LANCZOS)
        #self.icon_side = ImageTk.PhotoImage(self.icon_side)
        #lbl_menu = Label(funmenu, text='Menu', font=("times new roman", 20), bg='green').pack(side=TOP, fill=X)
        btn_log = Button(self.root, text="Logout", bg="yellow", fg="blue", font=("times new roman", 16, "bold"), bd=4,cursor="hand2")
        btn_log.place(x=1200, y=143, width=147, height=31)
        btn_employee = Button(self.root, text='Employee' ,command=self.employee, compound=CENTER,padx=5, font=("times new roman", 18, 'bold'),
                              bg='black',fg="blue", bd=4,cursor="hand2").place(x=0,y=143,width=200,height=31)
        btn_supplier = Button(self.root, text='Stock',command=self.stock, compound=LEFT,padx=5, font=("times new roman", 18, 'bold'),
                              bg='black',fg="blue" ,bd=4,cursor="hand2").place(x=200,y=143,width=200,height=31)
        btn_category = Button(self.root, text='Category' ,command=self.category, compound=LEFT,padx=5, font=("times new roman", 18, 'bold'),
                              bg='black', bd=4,fg="blue",cursor="hand2").place(x=400,y=143,width=200,height=31)
        btn_Products = Button(self.root, text='Products' ,command=self.products, compound=LEFT,padx=5, font=("times new roman", 18, 'bold'),
                              bg='black', bd=4,fg="blue",cursor="hand2").place(x=600,y=143,width=200,height=31)
        btn_Sales = Button(self.root, text='Sales',command=self.sales, compound=LEFT, padx=5, font=("times new roman", 18, 'bold'),
                           bg='black', bd=4,fg="blue", cursor="hand2").place(x=800,y=143,width=200,height=31)
        btn_Exit = Button(self.root, text='Exit', padx=5,font=("times new roman", 18, 'bold'),
                          bg='black', bd=4,fg="blue", cursor="hand2").place(x=1000,y=143,width=200,height=31)

#====================================================================================================
    def employee(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = employeeClass(self.new_win)
#====================================================================================================
    def stock(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = stockClass(self.new_win)
#====================================================================================================
    def category(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = categoryClass(self.new_win)
#====================================================================================================
    def products(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = productClass(self.new_win)
#====================================================================================================
    def sales(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = salesClass(self.new_win)

if __name__ == "__main__":
    root = Tk()
    obj = IMG(root)
    root.mainloop()

