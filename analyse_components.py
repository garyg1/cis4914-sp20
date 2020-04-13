from utils import get_obj, histogram, dump_obj
import ast
import pprint

components = get_obj('components_no_high_degree.pkl')
uritype = get_obj('uri_to_type.pkl')
h = histogram(map(len, components))
print('histogram:', h)
# {2503312: 1, 33: 11, 2: 8630, 1: 77925, 49: 8, 5: 1829, 4: 1017, 201: 26, 3: 3613, 6: 631, 77: 2, 19: 10, 27: 4, 101: 3, 57: 2, 17: 31, 89: 3, 129: 1, 8: 15, 21: 26, 41: 3, 25: 18, 40: 1, 29: 12, 53: 5, 13: 30, 34: 3, 32: 1, 9: 51, 61: 1, 37: 9, 66: 1, 51: 1, 69: 2, 52: 2, 105: 1, 126: 1, 131: 1, 45: 2, 104: 1, 10: 7, 15: 13, 68: 2, 67: 1, 11: 13, 65: 2, 46: 1, 39: 1, 20: 3, 73: 1, 168: 1, 54: 1, 28: 3, 74: 1, 18: 4, 7: 22, 12: 1, 26: 2, 22: 2, 30: 3, 44: 1, 23: 1, 14: 3, 38: 1, 36: 1, 16: 2, 24: 1}

def get_types(comps):
    print("types")
    all_types = []
    for comp in comps:
        str_types = []
        for x in comp:
            str_type = str(sorted(list(uritype[x]))) if x in uritype else "None"
            str_types.append(str_type)
        str_str_types = str(sorted(str_types))
        all_types.append(str_str_types)
    return all_types

def get_histogram(types):
    print("histogram:", len(types))
    return list(map(lambda x: (ast.literal_eval(x[0]), x[1]), histogram(types).items()))


MAX_SIZE = 10000
cn = [list(filter(lambda x: len(x) == n, components)) for n in sorted(h.keys()) if n < MAX_SIZE]
tn = [get_types(comps) for comps in cn]
hn = [get_histogram(types) for types in tn]
size_to_type_histogram = dict(zip(sorted(h.keys()), hn))
dump_obj('size_to_type_histogram_2.pkl', size_to_type_histogram)
