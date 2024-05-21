from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

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
        #self.show = Image.open("storeVector.png")
        #self.show = self.show.resize((1350, 500), Image.LANCZOS)
        #self.show = ImageTk.PhotoImage(self.show)

        #l_logo = Label(self.root, image=self.show, bd=0)
        #l_logo.place(x=-250, y=150)
        # ===clock===
        self.lbl_clock = Label(self.root,text="Date: DD-MM-YYYY \t\tWelcome to Shoe Shop Management System\t\tTime: HH:MM:SS",font=('times new roman', 20), bg='#4d636d', fg='white')
        self.lbl_clock.place(x=0, y=100, relwidth=1, height=40)
        funmenu = Frame(self.root, bd=2, relief=RIDGE, bg='black')
        funmenu.place(x=0, y=141, width=1350, height=35)
        btn_log = Button(self.root, text="Logout", bg="yellow", fg="blue", font=("times new roman", 16, "bold"), bd=4,cursor="hand2")
        btn_log.place(x=1200, y=143, width=147, height=31)



if __name__ == "__main__":
    root = Tk()
    obj = IMG(root)
    root.mainloop()

