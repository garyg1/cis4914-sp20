import pickle
from collections import defaultdict

SAVE_DIR_PREFIX = 'saved/'


def dump_obj(name, obj):
    with open(SAVE_DIR_PREFIX + name, 'wb') as outfile:
        pickle.dump(obj, outfile)


def get_obj(name):
    with open(SAVE_DIR_PREFIX + name, 'rb') as infile:
        return pickle.load(infile)


def transpose_dict(d):
    transposed = defaultdict(int)
    for k in d:
        transposed[d[k]] += 1
    return dict(transposed)


def histogram(int_iter):
    count = defaultdict(int)
    for i in int_iter:
        count[i] += 1
    return dict(count)