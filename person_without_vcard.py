from utils import dump_obj, get_obj, histogram
from parse import get_lines, parse_line, get_data
from rdf import TYPE_INDIVIDUAL, HAS_CONTACT_INFO, CONTACT_INFO_FOR, TYPE_PERSON, is_individual, NUM_LINES

uritype = get_obj('uri_to_type.pkl')

persons = list(filter(lambda uri: TYPE_PERSON in uritype[uri], uritype))
print(len(persons))
# 341079

orphan_persons1 = set(persons)
orphan_persons2 = set(persons)
line_count = 0
for s, p, o in map(parse_line, get_data()):
    line_count += 1
    if line_count % 100000 == 0:
        print(line_count, '/', NUM_LINES)

    if p != HAS_CONTACT_INFO and p != CONTACT_INFO_FOR:
        continue
    if not is_individual(s) or not is_individual(o):
        continue
    if p == HAS_CONTACT_INFO and s in orphan_persons1:
        orphan_persons1.remove(s)
    if p == CONTACT_INFO_FOR and o in orphan_persons2:
        orphan_persons2.remove(o)

print(len(orphan_persons1), len(orphan_persons2))
# 3908 3908
dump_obj('people_without_vcards.pkl', orphan_persons1)