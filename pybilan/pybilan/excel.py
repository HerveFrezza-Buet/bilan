# coding: utf-8

import pandas as pd
from pathlib import Path

def read(path):
    frame  = pd.read_excel(str(path.absolute()), header=None)
    keys   = []
    data   = []
    for key_col in range(0, frame.shape[1]):
        key = frame.at[0, key_col]
        if pd.isna(key) :
            break
        keys.append(key)
    for l in range(1, frame.shape[0]):
        # we test empty line
        not_empty = False
        for c in range(0, len(keys)) :
            not_empty = pd.notna(frame.at[l,c])
            if not_empty :
                break
        if not not_empty :
            continue
        content = dict()
        for c, k in enumerate(keys) :
            value = frame.at[l, c]
            if pd.notna(value):
                content[k] = value
        data.append(content)
    
    return keys, data
    

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2 :
        print('Usage : {} <.xlsx>'.format(sys.argv[0]))
        sys.exit(1)
    path = Path(sys.argv[1])
    keys, data = read(path)
    print(data)
    
