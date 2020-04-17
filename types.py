from collections import defaultdict
import pickle
from parse import get_lines, parse_line

"""
return number of instances of each type in UF VIVO.
"""

f = open('data/content.nq', 'r')
lines = get_lines(f)

types = defaultdict(int)

for i, line in enumerate(lines):
    if i % 1000000 == 0:
        print(i)
    s, p, o = parse_line(line)
    
    if p == "<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>":
        types[o] += 1

with open('types2.pkl', 'wb') as outfile:
    pickle.dump(dict(types), outfile)