from parse import get_lines, parse_line, get_data
from rdf import TYPE, LABEL, RELATES, RELATED_BY, NUM_LINES, is_individual, is_datetime, TYPE_UNIVERSITY, TYPE_CONCEPT
from utils import dump_obj
from collections import defaultdict

metadata_uris = set()

line_count = 0
for s, p, o in map(parse_line, get_data()):
    line_count += 1
    if line_count % 100000 == 0:
        print(line_count, '/', NUM_LINES)
    
    if p == TYPE and (is_datetime(o) or o == TYPE_UNIVERSITY or o == TYPE_CONCEPT):
        metadata_uris.add(s)

dump_obj('metadata_uris_2.pkl', metadata_uris)
