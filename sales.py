from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
class salesClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x500+100+255")
        self.root.title("Shoe Shop Management System |Develop By Teshav")
        self.root.config(bg="white")
        self.root.focus_force()
        salmenu = Frame(self.root, bd=4, relief=RIDGE, bg='black')
        salmenu.place(x=0, y=0, width=1350, height=500)
        #====tittle========
        

if __name__=="__main__":
    root = Tk()
    obj = salesClass(root)
    root.mainloop()