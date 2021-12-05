#!/usr/bin/env python
# coding : utf8

from pathlib import Path
from pybilan import *

root_dir   = Path('.')
data_path  = gui.xlsx_filename()
keys, acts = excel.read(data_path)
document = report.Document(data_path.stem,                # file prefix
                           'Maintenance report for 2021', # title or None
                           '(figures only)',              # sub title or None
                           'John Doe',                    # name or None
                           'Dec 21th 2021')               # date or None (for today).

document.output_dir = root_dir / 'outputs'

codes    = config.read_codes(root_dir / 'code.txt')
groups   = config.read_groups(root_dir / 'groups.txt')

# We get the column titles
col_computers, col_activities, col_dates = keys

# Let us make a pie chart, counting the kinds of maintenance acts. We replace the acts by their full description, for nice legends.
activities = data.decode_values(acts, col_activities, codes)
total = document.make_pie(activities, col_activities)
document.caption('Summary of maintenance kinds ({} acts realized).'.format(total))

# Let us make a pie chart as well, counting the location (cluster) of the maintenance.
activities = data.group_values_dict_keep(acts, col_computers, groups)
activities = data.decode_values(activities, col_computers, codes)
total      = document.make_pie(activities, col_computers)
document.caption('Summary of maintenance location ({} acts realized).'.format(total))

# Let us make a bar chart, counting for each cluster the maintenance acts.
activities = data.group_values_dict_keep(acts,   col_computers, groups)
activities = data.decode_values(activities, col_computers, codes)
activities = data.decode_values(activities, col_activities, codes)
total      = document.make_histo(activities, col_computers)
document.caption('Activities by cluster ({} acts realized).'.format(total))
total      = document.make_bars(activities, col_computers, col_activities)
document.caption('Activities by cluster ({} acts realized).'.format(total))

# We build the latex file for the report.
document.generate()

gui.info('generation done.')



