from utils import dump_obj
from queries import query_orphans
from rdf import *

all, begin, end = query_orphans([
    (TYPE_DATETIMEVALUE, TYPE_ANY, TYPE_EDGE_ANY, TYPE_EDGE_ANY),
])[0]

print(len(all), len(begin), len(end))
dump_obj('orphaned_datetimevalues.pkl', {'in-orphans': begin, 'out-orphans': end})