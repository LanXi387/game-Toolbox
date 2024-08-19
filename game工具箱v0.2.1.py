import os
import sys
import webbrowser
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Main_Window(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title('game工具箱v0.2.1')
        self.master.geometry('380x250')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        # Button actions
        self.createButton("EA", 262, 52, "https://www.ea.com")
        self.createButton("epic", 139, 10, "https://www.epicgames.com")
        self.createButton("steam", 262, 10, "https://www.steampowered.com")
        self.createButton("育碧", 139, 53, "https://www.ubisoft.com")
        self.createButton("watt toolkit", 20, 52, "https://steampp.net/")
        self.createButton("PCL", 19, 130, "https://ltcat.lanzouv.com/b0aj6gsid")
        self.createButton("HMCL", 138, 130, "https://hmcl.huangyuhui.net/")
        self.createButton("bakaXL", 262, 130, "https://www.bakaxl.com/")
        self.createButton("作者主页", 279, 216, "https://space.bilibili.com/1890708787")
        self.createButton("项目仓库", 180, 215, "https://github.com/LanXi387/game-Toolbox/")
        self.createButton("PCL赞助", 19, 159, "https://afdian.com/a/LTCat")
        self.createButton("HMCL赞助", 139, 159, "https://afdian.com/a/huanghongxun")
        self.createButton("bakaXL赞助", 262, 159, "https://afdian.com/a/TT702")

        self.Label_ID_7 = ttk.Label(self.top, text="作者：404zero（LanXi）")
        self.Label_ID_7.place(x=15, y=218, width=150, height=30)

        self.Label_ID_5 = ttk.Label(self.top, text="先下载watt加速")
        self.Label_ID_5.place(x=22, y=16, width=100, height=30)

        self.Label_ID_0 = ttk.Label(self.top, text="Minecraft")
        self.Label_ID_0.place(x=18, y=99, width=100, height=30)

        self.Label_ID_0 = ttk.Label(self.top, text="PCL提取码为pcl2")
        self.Label_ID_0.place(x=18, y=188, width=100, height=30)

    def createButton(self, text, x, y, url, command=None):
        button = ttk.Button(self.top, text=text, command=lambda: self.openUrl(url) if command is None else command)
        button.place(x=x, y=y, width=100, height=30)

    def openUrl(self, url):
        webbrowser.open(url)



if __name__ == '__main__':
    win = Tk()
    Main_Window(win).mainloop()