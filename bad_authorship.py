from parse import get_lines, parse_line, get_data
from rdf import TYPE, LABEL, RELATES, NUM_LINES
from utils import dump_obj
from collections import defaultdict


with open('samples/related-to-bad-authorship.txt', 'r') as f:
    authorships = set([o for s, p, o in map(parse_line, get_lines(f))])

authorships_to_authors = defaultdict(lambda: 0)

authors = set()
line_count = 0
for line in get_data():
    line_count += 1
    if line_count % 100000 == 0:
        print(line_count, '/', NUM_LINES)

    s, p, o = parse_line(line)
    if p == RELATES and s in authorships:
        authors.add(o)
        authorships_to_authors[s] += 1
        print('found author', len(authors), o)

print('finished searching for authors')

dump_obj('bad_authorship_authors.pkl', authors)
dump_obj('bad_authorship_authorships.pkl', dict(authorships_to_authors))
