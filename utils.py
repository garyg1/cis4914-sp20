import pickle
from collections import defaultdict

def dump_obj(name, obj):
    with open(name, 'wb') as outfile:
        pickle.dump(obj, outfile)


def get_obj(name):
    with open(name, 'rb') as infile:
        return pickle.load(infile)


def transpose_dict(d):
    transposed = defaultdict(lambda: 0)
    for k in d:
        transposed[d[k]] += 1
    return dict(transposed)
