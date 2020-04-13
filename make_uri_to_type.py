from parse import get_lines, parse_line, get_data
from rdf import TYPE, LABEL, RELATES, RELATED_BY, NUM_LINES, is_individual
from utils import dump_obj
from collections import defaultdict

uri_to_type = defaultdict(lambda: set())

line_count = 0
for s, p, o in map(parse_line, get_data()):
    line_count += 1
    if line_count % 100000 == 0:
        print(line_count, '/', NUM_LINES)
    
    if p == TYPE:
        uri_to_type[s].add(o)

dump_obj('uri_to_type.pkl', dict(uri_to_type))
