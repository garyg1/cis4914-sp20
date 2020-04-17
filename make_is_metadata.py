from parse import get_lines, parse_line, get_data
from utils import dump_obj
from collections import defaultdict
from rdf import *

metadata_uris = set()

line_count = 0
for s, p, o in map(parse_line, get_data()):
    line_count += 1
    if line_count % 100000 == 0:
        print(line_count, '/', NUM_LINES)
    
    if p == TYPE and (o == TYPE_FOAF_ORGANIZATION or o == TYPE_CONCEPT):
        metadata_uris.add(s)

dump_obj('saved/metadata_uris.pkl', metadata_uris)
