import sys
from tkinter.filedialog import askopenfilename
from pathlib import Path

def xlsx_filename():
    filename = askopenfilename(filetypes=[('excel','*.xlsx')])
    if not filename:
        sys.exit(0)
    return Path(filename)

if __name__ == "__main__":
    print(xlsx_filename())
