import sys
import os
import tkinter as tk
import tkinter.filedialog as fd
import tkinter.messagebox as mb
from pathlib import Path

def xlsx_filename():
    filename = fd.askopenfilename(filetypes=[('excel','*.xlsx')])
    if not filename:
        sys.exit(0)
    return Path(filename)

def info(msg):
    os.system(f'zenity --info --text="{msg}"')
    #mb.showinfo('Info', msg)
    
def error(msg):
    os.system(f'zenity --error --text="{msg}"')
    #mb.showerror('Error', msg)

if __name__ == "__main__":
    print(xlsx_filename())
