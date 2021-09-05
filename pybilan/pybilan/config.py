
from pathlib import Path


def read_codes(path):
    data = {}
    for l in path.open():
        words = l.split()
        if len(words) > 1 and words[0][0] != '#':
            data[words[0]] = ' '.join(words[1:])
    return data

def read_groups(path):
    data = {}
    for l in path.open():
        words = l.split()
        if len(words) > 1 and words[0][0] != '#':
            data[words[0]] = words[1:]
    return data
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2 :
        print('Usage : {} <.xlsx>'.format(sys.argv[0]))
        sys.exit(1)
    path = Path(sys.argv[1])
    data = read_codes(path)
    print(data)
