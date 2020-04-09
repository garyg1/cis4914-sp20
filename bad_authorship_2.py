from parse import parse_line, get_data
from rdf import TYPE, LABEL, RELATES, NUM_LINES, RELATED_BY
from utils import dump_obj, get_obj

authors = get_obj('bad_authorship_authors.pkl')

for s, p, o in map(parse_line, get_data()):
    if p not in set([RELATES, RELATED_BY, TYPE]) and s in authors:
        print(s, p, o)

"""
MOST_SPECIFIC_TYPE wrong?
<http://vivo.ufl.edu/individual/n6654993213> <http://vitro.mannlib.cornell.edu/ns/vitro/0.7#mostSpecificType> <http://vivo.ufl.edu/ontology/vivo-ufl/UFEntity>
<http://vivo.ufl.edu/individual/n6654993213> <http://vitro.mannlib.cornell.edu/ns/vitro/0.7#mostSpecificType> <http://xmlns.com/foaf/0.1/Person>

EXAMPLE
duplicate harvesting?
<http://vivo.ufl.edu/individual/n8997932387> <http://vivo.ufl.edu/ontology/vivo-ufl/dateHarvested> "2013-11-25T17:10:21.364684"^^<http://www.w3.org/2001/XMLSchema#string>
<http://vivo.ufl.edu/individual/n8997932387> <http://vivo.ufl.edu/ontology/vivo-ufl/dateHarvested> "2013-11-25T17:10:15.170174"^^<http://www.w3.org/2001/XMLSchema#string>
<http://vivo.ufl.edu/individual/n8997932387> <http://purl.obolibrary.org/obo/ARG_2000028> <http://vivo.ufl.edu/individual/n3736034>
<http://vivo.ufl.edu/individual/n8997932387> <http://vivo.ufl.edu/ontology/vivo-ufl/harvestedBy> "Python Pubs version 1.2.1"^^<http://www.w3.org/2001/XMLSchema#string>
<http://vivo.ufl.edu/individual/n8997932387> <http://vivo.ufl.edu/ontology/vivo-ufl/harvestedBy> "Python Pubs version 1.1"^^<http://www.w3.org/2001/XMLSchema#string>
<http://vivo.ufl.edu/individual/n8997932387> <http://www.w3.org/2000/01/rdf-schema#label> "Mikulec, I."^^<http://www.w3.org/2001/XMLSchema#string>

EXAMPLE
<http://vivo.ufl.edu/individual/n1948286669> <http://vivo.ufl.edu/ontology/vivo-ufl/dateHarvested> "2013-11-25T17:10:21.364603"^^<http://www.w3.org/2001/XMLSchema#string>
<http://vivo.ufl.edu/individual/n1948286669> <http://vivo.ufl.edu/ontology/vivo-ufl/privacyFlag> "N"^^<http://www.w3.org/2001/XMLSchema#string>
<http://vivo.ufl.edu/individual/n1948286669> <http://purl.obolibrary.org/obo/ARG_2000028> <http://vivo.ufl.edu/individual/n746566>
<http://vivo.ufl.edu/individual/n1948286669> <http://vivo.ufl.edu/ontology/vivo-ufl/homeDept> <http://vivo.ufl.edu/individual/n102962>
<http://vivo.ufl.edu/individual/n1948286669> <http://vivo.ufl.edu/ontology/vivo-ufl/harvestedBy> "PeopleSoft-BizTalk-Harvester"^^<http://www.w3.org/2001/XMLSchema#string>
<http://vivo.ufl.edu/individual/n1948286669> <http://vivo.ufl.edu/ontology/vivo-ufl/harvestedBy> "Python Pubs version 1.1"^^<http://www.w3.org/2001/XMLSchema#string>
<http://vivo.ufl.edu/individual/n1948286669> <http://www.w3.org/2000/01/rdf-schema#label> "Bansal, Manisha Makker"^^<http://www.w3.org/2001/XMLSchema#string>

EXAMPLE
<http://vivo.ufl.edu/individual/n9345367699> <http://vivo.ufl.edu/ontology/vivo-ufl/dateHarvested> "2014-08-13T15:05:24.291179"^^<http://www.w3.org/2001/XMLSchema#string>
<http://vivo.ufl.edu/individual/n9345367699> <http://purl.obolibrary.org/obo/ARG_2000028> <http://vivo.ufl.edu/individual/n4384428>
<http://vivo.ufl.edu/individual/n9345367699> <http://vivo.ufl.edu/ontology/vivo-ufl/harvestedBy> "Python Pubs version 1.3"^^<http://www.w3.org/2001/XMLSchema#string>
<http://vivo.ufl.edu/individual/n9345367699> <http://www.w3.org/2000/01/rdf-schema#label> "Blekman, F."^^<http://www.w3.org/2001/XMLSchema#string>
"""