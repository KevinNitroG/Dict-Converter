import os
import sys
import shutil

from .pr import *


def clear_screen():
    if os.name == 'nt':  # for Windows
        os.system('cls')
    else:  # for Linux and Mac
        os.system('clear')


def wait_for_pressed_key():
    print()
    os.system('pause')
    clear_screen()


def exit_program(msg = "Unkown", exit_code = 0):
    print(prBold(prLightBlue("KẾT THÚC".center(40, '-'))), end= '\n\n')
    if exit_code == 0:
        print(prCyan(msg))
    else:
        print(prRed(msg))
    print()
    os.system('pause')
    exit(exit_code)


# def install_requirements():
#     import subprocess
#     import sys
#     try:
#         subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
#     except subprocess.CalledProcessError:
#         exit_program("Lỗi khi cài đặt requirements. Hãy dùng cmd và nhập lệnh" + prBold("pip install -r requirements.txt"), 1)


def switch_pwd(pwd):
    try:
        os.chdir(pwd)
    except FileNotFoundError:
        os.makedirs(pwd)
        os.chdir(pwd)


def delete_dir(d):
    try:
        shutil.rmtree(d)
    except FileNotFoundError:
        pass