import webbrowser
import tkinter as tk
from tkinter import ttk, Toplevel, Label

class Main_Window(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title('game工具箱v0.2')
        self.master.geometry('380x250')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()
        
        self.Button_ID_1 = ttk.Button(self.top, text="EA", command=lambda: webbrowser.open('http://www.ea.com'))
        self.Button_ID_1.place(x=262, y=52, width=100, height=30)

        self.Button_ID_3 = ttk.Button(self.top, text="epic", command=lambda: webbrowser.open('http://www.epicgames.com'))
        self.Button_ID_3.place(x=139, y=10, width=100, height=30)

        self.Button_ID_4 = ttk.Button(self.top, text="育碧", command=lambda: webbrowser.open('http://www.ubisoft.com'))
        self.Button_ID_4.place(x=139, y=53, width=100, height=30)

        self.Label_ID_7 = ttk.Label(self.top, text="作者：404zero")
        self.Label_ID_7.place(x=15, y=218, width=100, height=30)

        self.Button_ID_6 = ttk.Button(self.top, text="watt toolkit", command=lambda: webbrowser.open('https://steampp.net/'))
        self.Button_ID_6.place(x=20, y=52, width=100, height=30)

        self.Label_ID_5 = ttk.Label(self.top, text="先下载watt加速")
        self.Label_ID_5.place(x=22, y=16, width=100, height=30)

        self.Label_ID_0 = ttk.Label(self.top, text="Minecraft")
        self.Label_ID_0.place(x=18, y=99, width=100, height=30)

        self.Button_ID_0_1 = ttk.Button(self.top, text="PCL", command=self.open_pcl)
        self.Button_ID_0_1.place(x=19, y=130, width=100, height=30)

        self.Button_ID_0_2 = ttk.Button(self.top, text="HMCL", command=lambda: webbrowser.open('https://hmcl.huangyuhui.net/'))
        self.Button_ID_0_2.place(x=138, y=130, width=100, height=30)

        self.Button_ID_0_3 = ttk.Button(self.top, text="bakaXL", command=lambda: webbrowser.open('https://www.bakaxl.com/'))
        self.Button_ID_0_3.place(x=262, y=130, width=100, height=30)

        self.Button_ID_8 = ttk.Button(self.top, text="steam", command=lambda: self.open_url('https://www.steampowered.com'))
        self.Button_ID_8.place(x=262, y=10, width=100, height=30)

    def open_pcl(self):
        webbrowser.open('https://ltcat.lanzouv.com/b0aj6gsid')
        self.show_code_window()

    def show_code_window(self):
        code_window = Toplevel(self)
        code_window.title("提取码")
        code_window.geometry("200x100")
        label = Label(code_window, text="提取码: pcl2")
        label.pack(pady=20, padx=20)

if __name__ == '__main__':
    win = tk.Tk()
    Main_Window(win).mainloop()
