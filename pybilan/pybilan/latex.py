from pathlib import Path

def table(f, col_format, print_lines, rows, caption, num):
    res  = '\n\\begin{table}[htbp]\n'
    res += '  \\centerline{\\begin{tabular}{' + col_format + '}\n'
    for row in rows:
        res += '    \\hline\n'
        res += '    ' + ' & '.join([str(c) for c in row]) + '\\\\\n'
    res += '    \\hline\n'
    res += '  \\end{tabular}}\n'
    res += '\\caption{' + caption + ' \\label{tab:' + '{:06d}'.format(num) + '}}\n'
    res += '\\end{table}\n'
    f.write(res)
    
def fig(f, filepath, caption, num) :
    res  = '\n\\begin{figure}[htbp]\n'
    res += '\\centerline{\\includegraphics[width=.8\\textwidth]{' + str(filepath.absolute()) + '}}\n'
    res += '\\caption{' + caption + ' \\label{fig:' + '{:06d}'.format(num) + '}}\n'
    res += '\\end{figure}\n'
    f.write(res)

def title(f, title, subtitle, author, date) :
    if date is None:
        date = '\\today'
    f.write("\\hrule\n")
    f.write("\\vspace{5mm}\n")
    f.write("\\centerline{\Large\sc ")
    f.write(title)
    f.write("}\n")
    f.write("\\vspace{3mm}\n")
    f.write("\\centerline{\em ")
    f.write(subtitle)
    f.write("}\n")
    f.write("\\vspace{3mm}\n")
    f.write("\\centerline{")
    f.write(author)
    f.write("}\n")
    f.write("\\vspace{5mm}\n")
    f.write("\\hrule\n")
    f.write("\\vspace{2mm}\n")
    f.write("\\centerline{\\footnotesize \hfill ")
    f.write(date)
    f.write("}\n")
    f.write("\\vspace{5mm}\n")

def begin_document(f):
    f.write("\\documentclass[a4paper,10pt]{article}\n")
    f.write("\\usepackage[utf8]{inputenc}\n")
    f.write("\\usepackage[french]{babel}\n")
    f.write("\\usepackage{color}\n")
    f.write("\\usepackage{graphicx}\n")
    f.write("\\usepackage[margin=2cm]{geometry}\n")
    f.write("\\usepackage{ae}\n")
    f.write("\\usepackage{aeguill}\n")
    f.write("\\usepackage[colorlinks=true, linkcolor=blue, anchorcolor=blue, citecolor=blue, filecolor=blue, menucolor=blue, urlcolor=blue]{hyperref}\n")
    f.write("\n")
    f.write("\\begin{document}")
    f.write("\n")

def end_document(f):
    f.write("\n")
    f.write("\\end{document}")

if __name__ == "__main__":
    
    f = open('demo.tex', 'w')
    begin_document(f)
    title(f, 'Demo of document', '(this is an example)', 'John Doe', None)
    fig(f, Path('.') / 'figure.pdf', 'Some nice text', 1)
    table(f, '|lcr|', True, [['toto', 'titi', 'tutu'], ['foo', 'bar', 367], [1, 2, 3]], 'A nice table', 2)
    end_document(f)
    f.close()
    
