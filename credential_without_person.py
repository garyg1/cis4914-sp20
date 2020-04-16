from utils import dump_obj
from queries import query_orphans
from rdf import TYPE_ISSUED_CREDENTIAL, TYPE_PERSON, RELATED_BY, RELATES

all, orphan_begin, orphan_end = query_orphans(TYPE_ISSUED_CREDENTIAL, TYPE_PERSON, RELATES, RELATED_BY)
print(len(all), len(orphan_begin), len(orphan_end))
dump_obj('credential_without_person.pkl', orphan_begin)

# ['<http://vivo.ufl.edu/individual/n222500>', '<http://vivo.ufl.edu/individual/n427156>']
