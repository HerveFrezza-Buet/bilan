import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

def pie(path, pie_data):
    """
    pie_data: {'sorts'  : [sort1, sort2, ...], 
               'data'   : [nb_sort1, nb_sort2, ...],
               'legend' : True}
    """
    total = 0
    for v in pie_data['data'] :
        total += v
        
    fig = plt.figure(figsize=(6, 3))
    plt.gca().set_aspect('equal')
    wedges, texts, autotexts = plt.gca().pie(pie_data['data'] , autopct=lambda x : int(x*total*.01+.5))
    if 'legend' in pie_data and pie_data['legend']:
        plt.gca().legend(wedges, pie_data['sorts'],
                         loc="center left",
                         bbox_to_anchor=(1, 0, 0.5, 1))
    fullfigname = str(path.absolute())
    plt.savefig(fullfigname, bbox_inches='tight')
    print('File "{}" generated.'.format(fullfigname))
    plt.close(fig)

def histo(path, histo_data):
    """
    histo_data: {'categories : [cat1, cat2, ...],
                 'data'      : [nb_for_cat1, nb_for_cat2, ...]
                 'legend' : True}
    """
    nb_categories = len(histo_data['categories'])
    bottom        = np.zeros(nb_categories)
    X             = np.arange(nb_categories)
    
    fig = plt.figure(figsize=(6, 3))
    plt.xticks(X, histo_data['categories'], rotation=60, ha='right')
    plt.ylabel("Nb")
    
    p = plt.bar(X, histo_data['data'], bottom=bottom.tolist(), edgecolor='white', width=1)
    
    fullfigname = str(path.absolute())
    plt.savefig(fullfigname, bbox_inches='tight')
    print('File "{}" generated.'.format(fullfigname))
    plt.close(fig)

def bar(path, bar_data):
    """
    bar_data: {'sorts'     : [sort1, sort2, ...], 
               'categories : [cat1, cat2, ...],
               'data'      : [[nb_sort1_for_cat1, nb_sort1_for_cat2, ...],
                              [nb_sort2_for_cat1, nb_sort1_for_cat2, ...],
                              ...]
               'legend' : True}
    """
    nb_categories = len(bar_data['categories'])
    bottom        = np.zeros(nb_categories)
    X             = np.arange(nb_categories)
    
    fig = plt.figure(figsize=(6, 3))
    plt.xticks(X, bar_data['categories'], rotation=60, ha='right')
    plt.ylabel("Nb")
    
    legend_names = []
    legend_data  = []
    for sort, b in enumerate(bar_data['data']) :
        p = plt.bar(X, b, bottom=bottom.tolist(), edgecolor='white', width=1)
        legend_data.append(p[0])
        legend_names.append(bar_data['sorts'][sort])
        bottom += b
    if 'legend' in bar_data and bar_data['legend']:
        legend_data.reverse()
        legend_names.reverse()
        plt.legend(legend_data, legend_names, loc='upper right', bbox_to_anchor=(1, 1), ncol=1)
    
    fullfigname = str(path.absolute())
    plt.savefig(fullfigname, bbox_inches='tight')
    print('File "{}" generated.'.format(fullfigname))
    plt.close(fig)
    
if __name__ == '__main__':

    pie_data = {'sorts'  : ['very high', 'high', 'medium', 'low', 'very low'], 
                'data'   : [         20,      5,       50,    15,         35],
                'legend' : True}
    pie(Path('./pie_demo.pdf'), pie_data)
    
    bar_data = {'sorts'      : ['very high', 'high', 'medium', 'low', 'very low'],
                'categories' : ['mathematics', 'physics', 'chemestry'],
                'data'       : [[ 2,  5, 10],
                                [ 3,  7,  0],
                                [ 0, 10,  9],
                                [ 0,  2, 11],
                                [10,  5, 10]], 
                'legend'     : True}
    bar(Path('./bar_demo.pdf'), bar_data)
                
