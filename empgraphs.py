from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
class EmployeeGraphs:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1065x317+100+288")
        self.root.title("Shoe Shop Management System |Develop By Teshav")
        self.root.config(bg="black")
        self.root.focus_force()
        self.root.resizable(False, False)
        supmenu = Frame(self.root, bd=4, relief=RIDGE, bg='black')
        supmenu.place(x=0, y=0, width=1100, height=330)
        
if __name__=="__main__":
    root = Tk()
    obj = EmployeeGraphs(root)
    root.mainloop()
