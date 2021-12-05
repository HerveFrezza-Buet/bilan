import sys
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
    mb.showinfo('Info', msg)

if __name__ == "__main__":
    print(xlsx_filename())
