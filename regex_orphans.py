from parse import get_lines, parse_line, get_data
from rdf import TYPE, LABEL, RELATES, RELATED_BY, NUM_LINES, is_individual
from utils import dump_obj

edges = dict()

line_count = 0
for s, p, o in map(parse_line, get_data()):
    line_count += 1
    if line_count % 100000 == 0:
        print(line_count, '/', NUM_LINES)

    if not s in edges:
        edges[s] = 0

    if is_individual(o):
        edges[s] += 1

dump_obj('regex_orphans_edges.pkl', edges)