from utils import get_obj, histogram, dump_obj
import ast

"""
builds a mapping from component size to a histogram of type compositions
d[component_size] = [
    (
        [comp1_node1_types_list, comp1_node2_types_list, ...],
        comp1_count
    ),
    (
        [comp2_node1_types_list, comp2_node2_types_list, ...],
        comp2_count
    ),
    ...
]
"""

components = get_obj('components.pkl')
h = histogram(map(len, components))

uritype = get_obj('uri_to_type.pkl')
def get_types(comps):
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
    return list(map(lambda x: (ast.literal_eval(x[0]), x[1]), histogram(types).items()))


MAX_SIZE = 10000
cn = [list(filter(lambda x: len(x) == n, components)) for n in sorted(h.keys()) if n < MAX_SIZE]
tn = [get_types(comps) for comps in cn]
hn = [get_histogram(types) for types in tn]

size_to_type_histogram = dict(zip(sorted(h.keys()), hn))
dump_obj('size_to_type_histogram.pkl', size_to_type_histogram)
