from parse import parse_line, get_data
from utils import dump_obj, get_obj, histogram
from rdf import *
from union_find import UnionFind

sets = UnionFind()

line_count = 0
for s, p, o in map(parse_line, get_data()):
    line_count += 1
    if line_count % 100000 == 0:
        print(line_count, '/', NUM_LINES)

    is_subject_individual = is_individual(s)
    is_object_individual = is_individual(o)

    if is_subject_individual:
        sets.add(s)
    if is_object_individual:
        sets.add(o)

    if is_subject_individual and is_object_individual:
        sets.union(s, o)

dump_obj('components.pkl', sets.components())
