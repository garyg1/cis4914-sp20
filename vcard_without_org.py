from utils import dump_obj, get_obj, histogram
from parse import get_lines, parse_line, get_data
from rdf import TYPE_VCARD_ORGANIZATION, HAS_CONTACT_INFO, CONTACT_INFO_FOR, TYPE_FOAF_ORGANIZATION, is_individual, NUM_LINES

uritype = get_obj('uri_to_type.pkl')

vcards = list(filter(lambda uri: TYPE_VCARD_ORGANIZATION in uritype[uri], uritype))
print(len(vcards))
# 1050

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
    if p == CONTACT_INFO_FOR and s in orphan_vcards and o in uritype and TYPE_FOAF_ORGANIZATION in uritype[o]:
        orphan_vcards.remove(s)
    if p == HAS_CONTACT_INFO and o in orphan_vcards and s in uritype and TYPE_FOAF_ORGANIZATION in uritype[s]:
        orphan_vcards.remove(o)

print(len(orphan_vcards))
# 1
dump_obj('vcards_without_orgs.pkl', list(orphan_vcards))
# <http://vivo.ufl.edu/individual/n130884>
# should not be vcard:Organization
# <http://vivo.ufl.edu/individual/n130884> <http://vitro.mannlib.cornell.edu/ns/vitro/0.7#mostSpecificType> <http://www.w3.org/2006/vcard/ns#Organization> <http://vitro.mannlib.cornell.edu/default/vitro-kb-inf> .
