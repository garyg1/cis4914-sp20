from utils import dump_obj, get_obj, histogram
from parse import get_lines, parse_line, get_data
from rdf import TYPE_POSITION, RELATED_BY, RELATES, TYPE_PERSON, is_individual, NUM_LINES

uritype = get_obj('uri_to_type.pkl')

positions = list(filter(lambda uri: TYPE_POSITION in uritype[uri], uritype))
print(len(positions))
# 65102

orphan_positions = set(positions)
orphan_positions_1 = set(positions)
line_count = 0
for s, p, o in map(parse_line, get_data()):
    line_count += 1
    if line_count % 100000 == 0:
        print(line_count, '/', NUM_LINES)


    if p != RELATED_BY and p != RELATES:
        continue
    if p == RELATES and s in orphan_positions and o in uritype and TYPE_PERSON in uritype[o]:
        orphan_positions.remove(s)
    if p == RELATED_BY and o in orphan_positions_1 and s in uritype and TYPE_PERSON in uritype[s]:
        orphan_positions_1.remove(o)

print(len(orphan_positions), len(orphan_positions_1))
# 0 0
dump_obj('position_without_person.pkl', list(orphan_positions))