from collections import defaultdict
import pickle
from parse import get_lines, parse_line

f = open('data/content.nq', 'r')
lines = get_lines(f)

things = set()

for i, line in enumerate(lines):
    if i % 1000000 == 0:
        print(i, len(things))
    s, p, o = parse_line(line)

    things.add(s)

print('number of unique subjects', len(things))
with open('things.pkl', 'wb') as outfile:
    pickle.dump(things, outfile)

