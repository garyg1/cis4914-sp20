from parse import get_lines, parse_line, get_data
from rdf import TYPE, LABEL, RELATES, RELATED_BY, NUM_LINES
from utils import dump_obj

relates = dict()
related_by = dict()

line_count = 0
for s, p, o in map(parse_line, get_data()):
    line_count += 1
    if line_count % 100000 == 0:
        print(line_count, '/', NUM_LINES)

    if not s in relates:
        relates[s] = 0
    if not s in related_by:
        related_by[s] = 0

    if p == RELATES:
        relates[s] += 1
    elif p == RELATED_BY:
        related_by[s] += 1

dump_obj('naive_orphans_relates.pkl', relates)
dump_obj('naive_orphans_related_by.pkl', related_by)