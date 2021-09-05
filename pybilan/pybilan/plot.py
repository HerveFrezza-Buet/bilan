import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

def pie(path, pie_data):
    """
    pie_data: {'labels' : [sort1, sort2, ...], 
               'fracs' : [nb_sort1, nb_sort2, ...],
               'legend' : True}
    """
    total = 0
    for v in pie_data['fracs'] :
        total += v
        
    fig = plt.figure(figsize=(6, 3))
    plt.gca().set_aspect('equal')
    wedges, texts, autotexts = plt.gca().pie(pie_data['fracs'] , autopct=lambda x : int(x*total*.01+.5))
    if 'legend' in pie_data and pie_data['legend']:
        plt.gca().legend(wedges, pie_data['labels'],
                         loc="center left",
                         bbox_to_anchor=(1, 0, 0.5, 1))
    fullfigname = str(path.absolute())
    plt.savefig(fullfigname, bbox_inches='tight')
    print('File "{}" generated.'.format(fullfigname))
    plt.close(fig)

if __name__ == '__main__':

    pie_data = {'labels' : ['very high', 'high', 'medium', 'low', 'very low'], 
                'fracs'  : [         20,      5,       50,    15,         35],
                'legend' : True}
    pie(Path('./pie_demo.pdf'), pie_data)
                
