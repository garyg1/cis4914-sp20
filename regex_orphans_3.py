from parse import get_lines, parse_line, get_data
from rdf import TYPE, LABEL, RELATES, RELATED_BY, NUM_LINES
from utils import get_obj, transpose_dict, dump_obj

edges = get_obj('regex_orphans_edges.pkl')
orphans = [key for key in edges if edges[key] == 0]
orphans = filter(lambda s: s[:2] != '_:', orphans)

dump_obj('regex_orphans_orphans.pkl', set(orphans))