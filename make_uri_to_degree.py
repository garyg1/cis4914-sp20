from parse import parse_line, get_data
from rdf import *
from utils import dump_obj, get_obj
from collections import defaultdict

uri_to_degree = defaultdict(int)

line_count = 0
for s, p, o in map(parse_line, get_data()):
    line_count += 1
    if line_count % 100000 == 0:
        print(line_count, '/', NUM_LINES)

    if is_individual(s) and is_individual(o):
        uri_to_degree[s] += 1
        uri_to_degree[o] += 1

dump_obj('uri_to_degree.pkl', dict(uri_to_degree))
