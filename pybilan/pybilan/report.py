
from pathlib import Path

from . import data
from . import plot
from . import excel
from . import config
from . import latex
import subprocess

class Document:
    def __init__(self, prefix, title, subtitle, author, date):
        self.prefix = prefix
        self.title = title
        self.subtitle = subtitle
        self.author = author
        self.date = date
        self.captions = []
        self.tmp_dir = Path('/tmp')
        self.output_dir = Path('.')
        self.tables = {}

    def make_table(self, col_format, print_lines, rows):
        ident = len(self.captions)
        self.tables[ident] = (col_format, print_lines, rows)
        caption = 'To be specified...'
        self.captions.append(caption)
        
        
    def make_pie(self, rows, attr, order_hint = None, legend = True):
        filename = 'fig-{:06d}.pdf'.format(len(self.captions))
        plot_data, total = data.pie_data(rows, attr, order_hint)
        plot_data['legend'] = legend
        caption = '{} elements, gathered by {}'.format(total, attr)
        self.captions.append(caption)
        plot.pie(self.tmp_dir / filename, plot_data)
        return total
        
    def make_histo(self, rows, category_attr, order_hint = None, legend = True):
        filename = 'fig-{:06d}.pdf'.format(len(self.captions))
        plot_data, total = data.histo_data(rows, category_attr, order_hint)
        plot_data['legend'] = legend
        caption = '{} elements, categorized by {}.'.format(total, category_attr)
        self.captions.append(caption)
        plot.histo(self.tmp_dir / filename, plot_data)
        return total
    
    def make_bars(self, rows, category_attr, sort_attr, category_order_hint = None, sort_order_hint = None, legend = True, display_values = False):
        filename = 'fig-{:06d}.pdf'.format(len(self.captions))
        plot_data, total = data.bar_data(rows, category_attr, sort_attr, category_order_hint, sort_order_hint)
        plot_data['legend'] = legend
        caption = '{} elements, categorized by {}, colored by {}.'.format(total, category_attr, sort_attr)
        self.captions.append(caption)
        plot.bar(self.tmp_dir / filename, plot_data, display_values)
        return total

    def caption(self, caption):
        self.captions[-1] = caption

    def generate(self):
        texname = self.prefix + '.tex'
        pdfname = self.prefix + '.pdf'
        path = self.tmp_dir / texname
        f = path.open('w')
        latex.begin_document(f)
        latex.title(f, self.title, self.subtitle, self.author, self.date)
        for idx, caption in enumerate(self.captions):
            if idx in self.tables:
                col_format, print_lines, rows = self.tables[idx]
                latex.table(f, col_format, print_lines, rows, caption, idx)
            else:
                latex.fig(f, self.tmp_dir / 'fig-{:06d}.pdf'.format(idx), caption, idx)
        latex.end_document(f)
        f.close()
        print('File "{}" generated.'.format(str(path.absolute())))
        cmd = 'pdflatex {}'.format(texname)
        print(cmd)
        subprocess.run(cmd.split(), cwd = self.tmp_dir)
        cmd = 'cp {} {}'.format(pdfname, self.output_dir.absolute())
        subprocess.run(cmd.split(), cwd = self.tmp_dir)
        print()
        print()
        print()
        print('File "{}" generated.'.format((self.output_dir / pdfname).absolute()))
        
        
        
