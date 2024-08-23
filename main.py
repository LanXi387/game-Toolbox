import webbrowser
import tkinter
from tkinter import ttk

import dl_steam


def open_url(url):
    """
    打开链接
    """
    webbrowser.open(url)


class MainWindow(tkinter.Frame):
    """
    主窗口
    """
    def __init__(self, master=None):
        super().__init__(master)
        self.Label_ID_0 = None
        self.Label_ID_5 = None
        self.Label_ID_7 = None
        self.top = None
        self.master.title("game工具箱v0.3.0")
        self.master.geometry("380x250")
        self.create_widgets()

    def create_widgets(self):
        self.top = self.winfo_toplevel()

        # 按钮功能
        self.create_button("EA", 262, 52, self.show_ea_tutorial)
        self.create_button("epic", 139, 10, self.show_epic_tutorial)
        self.create_button("steam", 262, 10, self.show_steam_tutorial)
        self.create_button("育碧", 139, 53, self.show_ubisoft_tutorial)
        self.create_button("watt toolkit", 20, 52, self.show_watt_tutorial)
        self.create_button("PCL", 19, 130, self.show_pcl_tutorial)
        self.create_button("HMCL", 138, 130, self.show_hmcl_tutorial)
        self.create_button("bakaXL", 262, 130, self.show_bakaxl_tutorial)

        # 其余按钮
        self.create_button("作者主页", 279, 216, "https://space.bilibili.com/1890708787", is_link=True)
        self.create_button("项目仓库", 180, 215, "https://github.com/LanXi387/game-Toolbox/", is_link=True)
        self.create_button("PCL赞助", 19, 159, "https://afdian.com/a/LTCat", is_link=True)
        self.create_button("HMCL赞助", 139, 159, "https://afdian.com/a/huanghongxun", is_link=True)
        self.create_button("bakaXL赞助", 262, 159, "https://afdian.com/a/TT702", is_link=True)

        self.Label_ID_7 = ttk.Label(self.top, text="作者：404zero（LanXi）")
        self.Label_ID_7.place(x=15, y=218, width=150, height=30)

        self.Label_ID_5 = ttk.Label(self.top, text="先下载watt加速")
        self.Label_ID_5.place(x=22, y=16, width=100, height=30)

        self.Label_ID_0 = ttk.Label(self.top, text="Minecraft")
        self.Label_ID_0.place(x=18, y=99, width=100, height=30)

        self.Label_ID_0 = ttk.Label(self.top, text="PCL提取码为pcl2")
        self.Label_ID_0.place(x=18, y=188, width=100, height=30)

    def create_button(self, text, x, y, command, is_link=False):
        """
        点击按钮
        """
        button = ttk.Button(
            self.top,
            text=text,
            command=lambda: open_url(command) if is_link else command(),
        )
        button.place(x=x, y=y, width=100, height=30)

    def show_ea_tutorial(self):
        """
        EA
        """
        # 创建教程窗口
        tutorial_window = tkinter.Toplevel(self.top)
        tutorial_window.title("EA 教程")
        tutorial_window.geometry("300x200")

        # 显示教程内容
        label = ttk.Label(tutorial_window, text="这是 EA 的教程内容。", wraplength=250)
        label.pack(pady=20)

        # 添加下载按钮
        download_button = ttk.Button(
            tutorial_window,
            text="下载",
            command=lambda: webbrowser.open(
                "https://origin-a.akamaihd.net/EA-Desktop-Client-Download/installer-releases/EAappInstaller.exe"
            ),
        )
        download_button.pack(pady=10)

        # 关闭按钮
        close_button = ttk.Button(
            tutorial_window, text="关闭", command=tutorial_window.destroy
        )
        close_button.pack(pady=10)

    def show_epic_tutorial(self):
        """
        EPIC
        """
        # 创建教程窗口
        tutorial_window = tkinter.Toplevel(self.top)
        tutorial_window.title("Epic 教程")
        tutorial_window.geometry("300x200")

        # 显示教程内容
        label = ttk.Label(tutorial_window, text="这是 Epic 的教程内容。", wraplength=250)
        label.pack(pady=20)

        # 添加下载按钮
        download_button = ttk.Button(
            tutorial_window,
            text="下载",
            command=lambda: webbrowser.open(
                "https://launcher-public-service-prod06.ol.epicgames.com/launcher/api/installer/download/EpicGamesLauncherInstaller.msi?trackingId=cea5469eb33f4dfc8a88e16cd8939df0"
            ),
        )
        download_button.pack(pady=10)

        # 关闭按钮
        close_button = ttk.Button(
            tutorial_window, text="关闭", command=tutorial_window.destroy
        )
        close_button.pack(pady=10)

    def show_steam_tutorial(self):
        """
        Steam
        """
        # 创建教程窗口
        tutorial_window = tkinter.Toplevel(self.top)
        tutorial_window.title("Steam 教程")
        tutorial_window.geometry("300x240")

        # 显示教程内容
        label = ttk.Label(
            tutorial_window, text="先点击下载按钮，等待下载完成后点击安装，之后请检查桌面", wraplength=250
        )
        label.pack(pady=20)

        # 添加下载按钮
        download_button = ttk.Button(
            tutorial_window, text="下载", command=lambda: dl_steam.download_steam()
        )
        download_button.pack(pady=10)

        # 添加安装按钮
        install_button = ttk.Button(
            tutorial_window,
            text="安装",
            command=lambda: dl_steam.install_steam("SteamSetup.exe"),
        )
        install_button.pack(pady=10)

        # 关闭按钮
        close_button = ttk.Button(
            tutorial_window, text="关闭", command=tutorial_window.destroy
        )
        close_button.pack(pady=10)

    def show_ubisoft_tutorial(self):
        """
        育碧
        """
        # 创建教程窗口
        tutorial_window = tkinter.Toplevel(self.top)
        tutorial_window.title("育碧 教程")
        tutorial_window.geometry("300x200")

        # 显示教程内容
        label = ttk.Label(tutorial_window, text="这是育碧的教程内容。", wraplength=250)
        label.pack(pady=20)

        # 添加下载按钮
        download_button = ttk.Button(
            tutorial_window,
            text="下载",
            command=lambda: webbrowser.open(
                "https://static3.cdn.ubi.com/orbit/launcher_installer/UbisoftConnectInstaller.exe"
            ),
        )
        download_button.pack(pady=10)

        # 关闭按钮
        close_button = ttk.Button(
            tutorial_window, text="关闭", command=tutorial_window.destroy
        )
        close_button.pack(pady=10)

    def show_watt_tutorial(self):
        """
        Watt
        """
        # 创建教程窗口
        tutorial_window = tkinter.Toplevel(self.top)
        tutorial_window.title("Watt Toolkit 教程")
        tutorial_window.geometry("300x200")

        # 显示教程内容
        label = ttk.Label(
            tutorial_window, text="这是 Watt Toolkit 的教程内容。", wraplength=250
        )
        label.pack(pady=20)

        # 添加下载按钮
        download_button = ttk.Button(
            tutorial_window,
            text="下载",
            command=lambda: webbrowser.open("https://steampp.net/"),
        )
        download_button.pack(pady=10)

        # 关闭按钮
        close_button = ttk.Button(
            tutorial_window, text="关闭", command=tutorial_window.destroy
        )
        close_button.pack(pady=10)

    def show_pcl_tutorial(self):
        """
        PCL
        """
        # 创建教程窗口
        tutorial_window = tkinter.Toplevel(self.top)
        tutorial_window.title("PCL 教程")
        tutorial_window.geometry("300x200")

        # 显示教程内容
        label = ttk.Label(tutorial_window, text="PCL提取码为pcl2", wraplength=250)
        label.pack(pady=20)

        # 添加下载按钮
        download_button = ttk.Button(
            tutorial_window,
            text="下载",
            command=lambda: webbrowser.open("https://ltcat.lanzouv.com/b0aj6gsid"),
        )
        download_button.pack(pady=10)

        # 关闭按钮
        close_button = ttk.Button(
            tutorial_window, text="关闭", command=tutorial_window.destroy
        )
        close_button.pack(pady=10)

    def show_hmcl_tutorial(self):
        """
        HMCL
        """
        # 创建教程窗口
        tutorial_window = tkinter.Toplevel(self.top)
        tutorial_window.title("HMCL 教程")
        tutorial_window.geometry("300x200")

        # 显示教程内容
        label = ttk.Label(tutorial_window, text="这是 HMCL 的教程内容。", wraplength=250)
        label.pack(pady=20)

        # 添加下载按钮
        download_button = ttk.Button(
            tutorial_window,
            text="下载",
            command=lambda: webbrowser.open("https://hmcl.huangyuhui.net/download/"),
        )
        download_button.pack(pady=10)

        # 关闭按钮
        close_button = ttk.Button(
            tutorial_window, text="关闭", command=tutorial_window.destroy
        )
        close_button.pack(pady=10)

    def show_bakaxl_tutorial(self):
        """
        BakaXL
        """
        # 创建教程窗口
        tutorial_window = tkinter.Toplevel(self.top)
        tutorial_window.title("BakaXL 教程")
        tutorial_window.geometry("300x200")

        # 显示教程内容
        label = ttk.Label(tutorial_window, text="这是 BakaXL 的教程内容。", wraplength=250)
        label.pack(pady=20)

        # 添加下载按钮
        download_button = ttk.Button(
            tutorial_window,
            text="下载",
            command=lambda: webbrowser.open("https://www.bakaxl.com/"),
        )
        download_button.pack(pady=10)

        # 关闭按钮
        close_button = ttk.Button(
            tutorial_window, text="关闭", command=tutorial_window.destroy
        )
        close_button.pack(pady=10)

    def show_tutorial_window(self, title, content):
        tutorial_window = tkinter.Toplevel(self.top)
        tutorial_window.title(title)
        tutorial_window.geometry("300x200")

        label = ttk.Label(tutorial_window, text=content, wraplength=250)
        label.pack(pady=20)

        close_button = ttk.Button(
            tutorial_window, text="关闭", command=tutorial_window.destroy
        )
        close_button.pack(pady=10)


if __name__ == "__main__":
    win = tkinter.Tk()
    MainWindow(win).mainloop()
