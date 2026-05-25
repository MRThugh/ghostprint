import os
import platform


def clear():
    os.system("cls" if platform.system() == "Windows" else "clear")


def center(text, width=80):
    return text.center(width)