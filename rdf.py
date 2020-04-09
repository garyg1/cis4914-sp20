import re

TYPE = "<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>"
LABEL = "<http://www.w3.org/2000/01/rdf-schema#label>"
AUTHORSHIP = "<http://vivoweb.org/ontology/core#Authorship>"
RELATES = "<http://vivoweb.org/ontology/core#relates>"
RELATED_BY = "<http://vivoweb.org/ontology/core#relatedBy>"
NUM_LINES = 37983245
MOST_SPECIFIC_TYPE = "<http://vitro.mannlib.cornell.edu/ns/vitro/0.7#mostSpecificType>"

INDIVIDUAL = re.compile("<http:\/\/vivo\.ufl\.edu\/individual\/n[0-9]+>")
def is_individual(uri):
    return INDIVIDUAL.match(uri)
