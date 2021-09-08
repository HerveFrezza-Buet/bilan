import sys
from tkinter.filedialog import askopenfilename

def xlsx_filename():
    filename = askopenfilename(filetypes=[('excel','*.xlsx')])
    if not filename:
        sys.exit(0)

if __name__ == "__main__":
    print(xlsx_filename())
