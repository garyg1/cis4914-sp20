from parse import get_lines, parse_line, get_data
from rdf import TYPE, LABEL, RELATES, RELATED_BY, NUM_LINES
from utils import get_obj, transpose_dict

edges = get_obj('regex_orphans_edges.pkl')

frequency = transpose_dict(edges)

keys = sorted([k for k in frequency])
vals = [frequency[k] for k in keys]

bands = [[0, 0], [1, 9], [10, 99], [100, 999], [1000, 9999], [10000, 999999]]
vals2 = [sum(frequency[k] for k in keys if band[0] <= k <= band[1]) for band in bands]

print(list(zip(bands, vals2)))
# [([0, 0], 102823), ([1, 9], 2646681), ([10, 99], 146754), ([100, 999], 8612), ([1000, 9999], 225), ([10000, 999999], 13)]
