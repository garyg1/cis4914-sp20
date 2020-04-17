from parse import parse_line, get_data
from utils import dump_obj, get_obj, histogram
from rdf import *
from union_find import UnionFind

metadata_uris = get_obj('metadata_uris.pkl')

sets = UnionFind()
line_count = 0
for s, p, o in map(parse_line, get_data()):
    line_count += 1
    if line_count % 100000 == 0:
        print(line_count, '/', NUM_LINES)

    is_subject_individual = is_individual(s)
    is_object_individual = is_individual(o)

    is_subject_metadata = (not is_subject_individual) or (s in metadata_uris)
    is_object_metadata = (not is_object_individual) or (o in metadata_uris)

    if not is_subject_metadata:
        sets.add(s)
    if not is_object_metadata:
        sets.add(o)
    if (not is_subject_metadata) and (not is_object_metadata):
        sets.union(s, o)

dump_obj('components_no_metadata.pkl', sets.components())
