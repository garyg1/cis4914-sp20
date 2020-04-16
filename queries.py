from parse import parse_line, get_data
from utils import get_obj
from rdf import NUM_LINES, TYPE_ANY

uritype = get_obj('uri_to_type.pkl')

def query_orphans(queries):
    all_of_type = []
    types_begin = []
    types_end = []
    for type1, type2, begin_edge, end_edge in queries:
        all_type1 = list(filter(lambda uri: type1 in uritype[uri], uritype))
        orphan_type1_begin = set(all_type1)
        orphan_type1_end = set(all_type1)

        all_of_type.append(all_type1)
        types_begin.append(orphan_type1_begin)
        types_end.append(orphan_type1_end)

    line_count = 0
    for s, p, o in map(parse_line, get_data()):
        line_count += 1
        if line_count % 100000 == 0:
            print(line_count, '/', NUM_LINES)

        for i, (type1, type2, begin_edge, end_edge) in enumerate(queries):
            if p != begin_edge and p != end_edge:
                continue
            if p == begin_edge and s in types_begin[i] and (type2 == TYPE_ANY or o in uritype and type2 in uritype[o]):
                types_begin[i].remove(s)
            if p == end_edge and o in types_end[i] and (type2 == TYPE_ANY or s in uritype and type2 in uritype[s]):
                types_end[i].remove(o)

    return list(zip(all_of_type, types_begin, types_end))