from utils import dump_obj, get_obj, histogram
from parse import get_lines, parse_line, get_data
from rdf import TYPE_MEMBERSHIP, TYPE_PERSON, INHERES_IN, BEARER_OF, is_individual, NUM_LINES

uritype = get_obj('uri_to_type.pkl')

memberships = list(filter(lambda uri: TYPE_MEMBERSHIP in uritype[uri], uritype))
print(len(memberships))
# 2410

orphan_memberships_1 = set(memberships)
orphan_memberships_2 = set(memberships)
line_count = 0
for s, p, o in map(parse_line, get_data()):
    line_count += 1
    if line_count % 100000 == 0:
        print(line_count, '/', NUM_LINES)

    if p != INHERES_IN and p != BEARER_OF:
        continue
    if p == INHERES_IN and s in orphan_memberships_1 and o in uritype and TYPE_PERSON in uritype[o]:
        orphan_memberships_1.remove(s)
    if p == BEARER_OF and o in orphan_memberships_2 and s in uritype and TYPE_PERSON in uritype[s]:
        orphan_memberships_2.remove(o)

print(len(orphan_memberships_1), len(orphan_memberships_2))
# 3 3
dump_obj('membership_without_person.pkl', list(orphan_memberships_1))