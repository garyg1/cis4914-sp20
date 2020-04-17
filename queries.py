from parse import parse_line, get_data
from utils import get_obj
from rdf import NUM_LINES, TYPE_ANY, TYPE_EDGE_ANY

uritype = get_obj('uri_to_type.pkl')

def query_orphans(queries):
    """
    simultaneously runs `queries` in parallel. 
    
    returns a list [(q1_all, q1_start, q1_end), ...] corresponding to the queries where:
    - q1_all is a list of all elements of type1
    - q1_start is a list of all elements of type1 that are not out-connected to a type2 by a begin_edge_type
    - q1_end is a list of all elements of type1 that are not in-connected to a type2 by a end_edge_type

    queries must be an array of the form
    [(type1, type2, begin_edge_type, end_edge_type), ...]
    """

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
            if (
                    p == begin_edge or begin_edge == TYPE_EDGE_ANY
                ) and s in types_begin[i] and (
                    type2 == TYPE_ANY or o in uritype and type2 in uritype[o]
                ):
                types_begin[i].remove(s)
            if (
                    p == end_edge or end_edge == TYPE_EDGE_ANY
                ) and o in types_end[i] and (
                    type2 == TYPE_ANY or s in uritype and type2 in uritype[s]
                ):
                types_end[i].remove(o)

    return list(zip(all_of_type, types_begin, types_end))