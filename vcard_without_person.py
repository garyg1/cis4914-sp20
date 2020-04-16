from utils import dump_obj, get_obj, histogram
from parse import get_lines, parse_line, get_data
from rdf import TYPE_INDIVIDUAL, HAS_CONTACT_INFO, CONTACT_INFO_FOR, TYPE_PERSON, is_individual, NUM_LINES

# vcards without CONTACT_INFO_FOR relation (any entity)

uritype = get_obj('uri_to_type.pkl')

vcards = list(filter(lambda uri: TYPE_INDIVIDUAL in uritype[uri], uritype))
print(len(vcards))
# 393485

orphan_vcards = set(vcards)
line_count = 0
for s, p, o in map(parse_line, get_data()):
    line_count += 1
    if line_count % 100000 == 0:
        print(line_count, '/', NUM_LINES)

    if p != HAS_CONTACT_INFO and p != CONTACT_INFO_FOR:
        continue
    if not is_individual(s) or not is_individual(o):
        continue
    if p == CONTACT_INFO_FOR and s in orphan_vcards:
        orphan_vcards.remove(s)
    if p == HAS_CONTACT_INFO and o in orphan_vcards:
        orphan_vcards.remove(o)

print(len(orphan_vcards))
# 5023
dump_obj('vcards_without_people.pkl', list(orphan_vcards))