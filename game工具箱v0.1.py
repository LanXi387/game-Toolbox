import os
import sys
import webbrowser
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from PIL import Image, ImageTk

class Main_Window(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title('game工具箱v0.1')
        self.master.geometry('400x300')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()
        
        # Button for EA
        self.Button_ID_1 = ttk.Button(self.top, text="EA", command=lambda: self.open_url('https://www.ea.com'))
        self.Button_ID_1.place(x=262, y=52, width=100, height=30)
        
        # Button for Epic
        self.Button_ID_3 = ttk.Button(self.top, text="epic", command=lambda: self.open_url('https://www.epicgames.com'))
        self.Button_ID_3.place(x=139, y=10, width=100, height=30)
        
        # Button for Ubisoft
        self.Button_ID_4 = ttk.Button(self.top, text="育碧", command=lambda: self.open_url('https://www.ubisoft.com'))
        self.Button_ID_4.place(x=139, y=53, width=100, height=30)
        
        # Label for Watt Toolkit
        self.Label_ID_5 = ttk.Label(self.top, text="请先下载watt toolkit进行加速")
        self.Label_ID_5.place(x=264, y=95, width=100, height=30)
        
        # Button for Watt Toolkit
        self.Button_ID_6 = ttk.Button(self.top, text="watt toolkit", command=lambda: self.open_url('https://steampp.net/'))
        self.Button_ID_6.place(x=262, y=129, width=100, height=30)
        
        # Button for Watt Toolkit
        self.Button_ID_8 = ttk.Button(self.top, text="steam", command=lambda: self.open_url('https://www.steampowered.com'))
        self.Button_ID_8.place(x=262, y=10, width=100, height=30)

        # Author Label
        self.Label_ID_7 = ttk.Label(self.top, text="作者：404zero")
        self.Label_ID_7.place(x=15, y=218, width=100, height=30)

    def open_url(self, url):
        webbrowser.open(url)

if __name__ == '__main__':
    win = Tk()
    Main_Window(win).mainloop()
