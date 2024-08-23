import subprocess
import os
import requests
import tkinter as tk
from tkinter import messagebox

STEAM_SETUP = "SteamSetup.exe"


def download_file(url, local_filename):
    """
    从指定 URL 下载文件并保存到本地文件
    """
    response = requests.get(url, stream=True)
    response.raise_for_status()

    with open(local_filename, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    show_message("下载完成", f"下载完成：{local_filename}")


def download_steam(local_filename=STEAM_SETUP):
    """
    下载 Steam 客户端并保存到指定文件名
    """
    steam_download_url = (
        "https://media.cdn.queniuqe.com/client/installer/SteamSetup.exe"
    )

    download_file(steam_download_url, local_filename)


def install_steam(installer_path):
    """
    安装 Steam 客户端
    """
    if not os.path.isfile(installer_path):
        show_message("安装失败", f"安装程序 {installer_path} 不存在。")
        return

    try:
        subprocess.run([installer_path, "/S"], check=True)
        show_message("安装完成", "Steam 客户端安装成功。")
    except subprocess.CalledProcessError as e:
        show_message("安装失败", f"安装失败：{e}")


def show_message(title, message):
    """
    显示 Tkinter 消息框
    """
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    messagebox.showinfo(title, message)
    root.destroy()  # 关闭主窗口


if __name__ == "__main__":
    download_steam(STEAM_SETUP)
    install_steam(STEAM_SETUP)
