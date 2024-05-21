from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from empgraphs import EmployeeGraphs
import pyttsx3
class employeeClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1346x493+100+255")
        self.root.title("Shoe Shop Management System |Develop By Teshav")
        self.root.config(bg="black")
        self.root.focus_force()
        self.root.resizable(False, False)

        empmenu = Frame(self.root, bd=4, relief=RIDGE, bg='black')
        empmenu.place(x=0, y=0, width=1350, height=500)
        #emplmenu = Frame(self.root, bd=4, relief=RIDGE, bg='black')
        #emplmenu.place(x=1069, y=0, width=280, height=500)
        self.icon_side = Image.open("800px_COLOURBOX11618656.jpg")
        self.icon_side = self.icon_side.resize((275, 458), Image.LANCZOS)
        self.icon_side = ImageTk.PhotoImage(self.icon_side)
        lbl_menu = Label(self.root,image=self.icon_side, bg='black').place(x=1070,y=35,width=275,height=458)
        self.line_style=ttk.Style()
        self.line_style.configure("Line.TSeparator",background="darkgrey")
        self.separator=ttk.Separator(self.root,orient='vertical',style="Line.TSeparator")
        self.separator.place(x=1066,y=4,width=3,height=493)
        # All variable======
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        # self.var_email=StringVar()
        self.var_emp_id = StringVar()
        self.var_gender = StringVar()
        self.var_contact = StringVar()
        self.var_name = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_email = StringVar()
        self.var_pass = StringVar()
        self.var_utype = StringVar()
        self.var_salary = StringVar()
        searchframe = LabelFrame(self.root, text="Search Employee", font=("goudy old style", 16, "bold"),
                                 bg='black',fg="blue")
        searchframe.place(x=300, y=10, width=600, height=70)
        # ===options====
        cmb_search = ttk.Combobox(searchframe, textvariable=self.var_searchby,
                                  values=("Select", "Name", "Email", "Contact"), state='readonly', justify=CENTER,
                                  font=("goudy old style", 15, "bold"))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)
        txt_search = Entry(searchframe, textvariable=self.var_searchtxt, font=('goudy old style', 15),
                           bg="lightyellow").place(x=200, y=10)
        # ===search button========
        # btn_search=Button(searchframe,text='Search',font=('times new roman',20,'bold'),bg='green',cursor='hand2').place(x=700,y=40,height=40,width=120)
        btn_search = Button(searchframe, text="Search", command=self.search, font=('goudy old style', 15), bg="green",
                            fg='white', cursor='hand2').place(x=430, y=5, height=30, width=120)
        # ====title======
        empl_det = Label(self.root, text="Employee Details", font=("goudy old style", 28, "bold"), bg='black',
                         fg='blue')
        empl_det.place(x=400, y=90, width=400)

        # ==========contant===========
        # ==========row 1==============
        lbl_empid = Label(self.root, text="Emp No.", font=("goudy old style", 16, "bold"), bg="black",fg="blue").place(x=50,
                                                                                                             y=150)
        lbl_gender = Label(self.root, text="Gender", font=("goudy old style", 16, "bold"), bg="black",fg="blue").place(x=400,
                                                                                                             y=150)
        lbl_contact = Label(self.root, text="Contact No.", font=("goudy old style", 16, "bold"), bg="black",fg="blue").place(
            x=750, y=150)

        txt_empid = Entry(self.root, textvariable=self.var_emp_id, font=("goudy old style", 16, "bold"),
                          bg="lightyellow",fg="black").place(x=150, y=150, width=180)
        cmb_gender = ttk.Combobox(self.root, textvariable=self.var_gender, values=("Select", "Male", "Female", "other"),
                                  state='readonly', justify=CENTER, font=("goudy old style", 15, "bold"))
        cmb_gender.place(x=490, y=150, width=180)
        cmb_gender.current(0)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 16, "bold"),
                            bg="lightyellow").place(x=870, y=150, width=180)
        # =========row 2===============
        lbl_name = Label(self.root, text="Name", font=("goudy old style", 16, "bold"), bg="black",fg="blue").place(x=50, y=190)
        lbl_dob = Label(self.root, text="D.O.B", font=("goudy old style", 16, "bold"), bg="black",fg="blue").place(x=400, y=190)
        lbl_doj = Label(self.root, text="D.O.J", font=("goudy old style", 16, "bold"), bg="black",fg="blue").place(x=750, y=190)

        txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 16, "bold"),
                         bg='lightyellow').place(x=150, y=190, width=180)
        txt_dob = Entry(self.root, textvariable=self.var_dob, font=("goudy old style", 16, "bold"),
                        bg='lightyellow').place(x=490, y=190, width=180)
        txt_doj = Entry(self.root, textvariable=self.var_doj, font=("goudy old style", 16, "bold"),
                        bg='lightyellow').place(x=870, y=190, width=180)
        # =========row 3=================
        lbl_email = Label(self.root, text="Email", font=("goudy old style", 16, "bold"), bg="black",fg="blue").place(x=50, y=230)
        lbl_password = Label(self.root, text="Password", font=("goudy old style", 16, "bold"), bg="black",fg="blue").place(x=400,
                                                                                                                 y=230)
        lbl_utype = Label(self.root, text="User Type", font=("goudy old style", 16, "bold"), bg="black",fg="blue").place(x=750,
                                                                                                               y=230)

        txt_email = Entry(self.root, textvariable=self.var_email, font=("goudy old style", 16, "bold"),
                          bg='lightyellow').place(x=150, y=230, width=180)
        txt_password = Entry(self.root, textvariable=self.var_pass, font=("goudy old style", 16, "bold"),
                             bg="lightyellow").place(x=490, y=230, width=180)
        cmb_utype = ttk.Combobox(self.root, textvariable=self.var_utype, values=("Admin", "Employee"), state='readonly',
                                 justify=CENTER, font=("goudy old style", 15, "bold"))
        cmb_utype.place(x=870, y=230, width=180)
        cmb_utype.current(0)
        # =========row 4================
        lbl_address = Label(self.root, text="Adderss", font=("goudy old style", 16, "bold"), bg="black",fg="blue").place(x=50,
                                                                                                               y=270)
        lbl_salary = Label(self.root, text="Salary", font=("goudy old style", 16, "bold"), bg="black",fg="blue").place(x=750,
                                                                                                             y=270)
        self.txt_address = Text(self.root, font=("goudy old style", 16, "bold"), bg='lightyellow')
        self.txt_address.place(x=150, y=270, width=300, height=60)
        txt_salary = Entry(self.root, textvariable=self.var_salary, font=("goudy old style", 16, "bold"),
                           bg='lightyellow').place(x=870, y=270, width=180)
        # ==========Buttons================
        btn_frm= Frame(self.root, bd=3, relief=RIDGE, bg='black')
        btn_frm.place(x=645, y=310, width=410, height=38)
        btn_add = Button(self.root, text="Save", command=self.add, font=('goudy old style', 15), bg="#2196f3",
                         fg='white', cursor='hand2').place(x=650, y=315, height=28, width=100)
        btn_update = Button(self.root, text="Update", command=self.update, font=('goudy old style', 15), bg="green",
                            fg='white', cursor='hand2').place(x=750, y=315, height=28, width=100)
        btn_delete = Button(self.root, text="Delete", command=self.delete, font=('goudy old style', 15), bg="red",
                            fg='white', cursor='hand2').place(x=850, y=315, height=28, width=100)
        btn_clear = Button(self.root, text="Clear", command=self.clear, font=('goudy old style', 15), bg="#607d8b",
                           fg='white', cursor='hand2').place(x=950, y=315, height=28, width=100)
        #==============graph button==========================
        btn_graph=Button(self.root,text="graph",command=self.graph,bd=3,bg='#2196f3',fg='black')
        btn_graph.place(x=1070,y=4,width=275,height=30)
        # ==========employee details========
        emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=5, y=350,width=1064, height=147)
        scrolly = Scrollbar(emp_frame, orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)
        self.EmployeeTable = ttk.Treeview(emp_frame, columns=(
        'eid', 'name', 'email', 'gender', 'contact', 'dob', 'doj', 'pass', 'utype', 'address', 'salary'),
                                          yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)

        self.EmployeeTable.heading('eid', text="EMP ID")
        self.EmployeeTable.heading('name', text="Name")
        self.EmployeeTable.heading('email', text="Email")
        self.EmployeeTable.heading('gender', text="Gender")
        self.EmployeeTable.heading('contact', text="Contact")
        self.EmployeeTable.heading('dob', text="D.O.B")
        self.EmployeeTable.heading('doj', text="D.O.J")
        self.EmployeeTable.heading('pass', text="Password")
        self.EmployeeTable.heading('utype', text="User Type")
        self.EmployeeTable.heading('address', text="Address")
        self.EmployeeTable.heading('salary', text="Salary")
        self.EmployeeTable["show"] = 'headings'
        self.EmployeeTable.column('eid', width=90)
        self.EmployeeTable.column('name', width=100)
        self.EmployeeTable.column('email', width=100)
        self.EmployeeTable.column('gender', width=100)
        self.EmployeeTable.column('contact', width=100)
        self.EmployeeTable.column('dob', width=100)
        self.EmployeeTable.column('doj', width=100)
        self.EmployeeTable.column('pass', width=100)
        self.EmployeeTable.column('utype', width=100)
        self.EmployeeTable.column('address', width=100)
        self.EmployeeTable.column('salary', width=100)
        self.EmployeeTable.pack(fill=BOTH, expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()
        # ===================================================================================

    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                text_speech=pyttsx3.init()
                answer="Employee ID Must be required" 
                text_speech.say(answer)
                text_speech.runAndWait()
                messagebox.showerror('Error', "Employee ID Must be required", parent=self.root)
                
            else:
                cur.execute("select * from employee where eid=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "This Employee ID already assigned,try different", parent=self.root)
                else:
                    cur.execute(
                        "Insert into employee(eid,name,email,gender,contact,dob,doj,pass,utype,address,salary) values(?,?,?,?,?,?,?,?,?,?,?)",
                        (
                            self.var_emp_id.get(),
                            self.var_name.get(),
                            self.var_email.get(),
                            self.var_gender.get(),
                            self.var_contact.get(),
                            self.var_dob.get(),
                            self.var_doj.get(),
                            self.var_pass.get(),
                            self.var_utype.get(),
                            self.txt_address.get('1.0', END),
                            self.var_salary.get()

                        ))
                    con.commit()
                    messagebox.showinfo("Success", "Employee Addedd Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to:{str(ex)}", parent=self.root)

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select * from employee")
            rows = cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to:{str(ex)}", parent=self.root)

    def get_data(self, ev):
        f = self.EmployeeTable.focus()
        content = (self.EmployeeTable.item(f))
        row = content['values']
        # print(row)
        self.var_emp_id.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_contact.set(row[4]),
        self.var_dob.set(row[5]),
        self.var_doj.set(row[6]),
        self.var_pass.set(row[7]),
        self.var_utype.set(row[8]),
        self.txt_address.delete('1.0', END),
        self.txt_address.insert(END, row[9])
        self.var_salary.set(row[10])

    def update(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror('Error', "Employee ID Must be required", parent=self.root)
            else:
                cur.execute("select * from employee where eid=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Employee ID", parent=self.root)
                else:
                    cur.execute(
                        "update employee set name=?,email=?,gender=?,contact=?,dob=?,doj=?,pass=?,utype=?,address=?,salary=? where eid=? ",
                        (

                            self.var_name.get(),
                            self.var_email.get(),
                            self.var_gender.get(),
                            self.var_contact.get(),
                            self.var_dob.get(),
                            self.var_doj.get(),
                            self.var_pass.get(),
                            self.var_utype.get(),
                            self.txt_address.get('1.0', END),
                            self.var_salary.get(),
                            self.var_emp_id.get()

                        ))
                    con.commit()
                    messagebox.showinfo("Success", "Employee Updated Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to:{str(ex)}", parent=self.root)

    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror('Error', "Employee ID Must be required", parent=self.root)
            else:
                cur.execute("select * from employee where eid=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Employee ID", parent=self.root)
                else:
                    op = messagebox.askyesno("Conform", "Do you really want to delete ?", parent=self.root)
                    if op == True:
                        cur.execute("delete from employee where  eid=?", (self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Employee Deleted Successfully", parent=self.root)
                        self.clear()



        except Exception as ex:
            messagebox.showerror("Error", f"Error due to:{str(ex)}", parent=self.root)

    def clear(self):
        self.var_emp_id.set(""),
        self.var_name.set(""),
        self.var_email.set(""),
        self.var_gender.set("Select"),
        self.var_contact.set(""),
        self.var_dob.set(""),
        self.var_doj.set(""),
        self.var_pass.set(""),
        self.var_utype.set("Admin"),
        self.txt_address.delete('1.0', END),
        self.txt_address.insert(END, "")
        self.var_salary.set("")
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
                    "select * from employee where " + self.var_searchby.get() + " LIKE '%" + self.var_searchtxt.get() + "%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                    for row in rows:
                        self.EmployeeTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found!!!", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to:{str(ex)}", parent=self.root)

    '''def graph(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()

        my_dict = {'name': ['Infant', 'child', 'young', 'old'],
                   'nos': [30, 40, 50, 50]}
        df = pd.DataFrame(data=my_dict)
        lbl = ['Infant', 'child', 'young', 'old']
        fig1 = df.plot.bar(title="population", y='nos', x='name',figsize=(3,3)).get_figure();

        plot1 = FigureCanvasTkAgg(fig1, self.root)
        plot1.get_tk_widget().grid(row=1, column=1, padx=30, pady=30)
        Q=('select name,salary from employee group by eid')
        cur.execute(Q)
        F = cur.fetchall()
        
        Df = pd.DataFrame(F, columns=[ 'name','salary'])
        fig1 = Df.plot.bar(title="Employee Salary", y='salary', x='name', figsize=(3, 3)).get_figure();

        plot1 = FigureCanvasTkAgg(fig1, self.root)
        plot1.get_tk_widget().grid(row=1, column=1, padx=30, pady=30)
        y=Df['salary']
        plt.plot(Df['name'], y,)
        #plt.ylim(0,10000)
        plt.title('EMPLOYEE SALARY', fontsize=13.0)
        plt.xlabel('EMPLOYEE NAME', fontsize=12.0)
        plt.ylabel('SALARY OF EMPLOYEE', fontsize=12.0)
        plt.show()'''
        
    def graph(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = EmployeeGraphs(self.new_win)




if __name__=="__main__":
    root = Tk()
    obj = employeeClass(root)
    root.mainloop()