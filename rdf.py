import re

TYPE = "<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>"
LABEL = "<http://www.w3.org/2000/01/rdf-schema#label>"
AUTHORSHIP = "<http://vivoweb.org/ontology/core#Authorship>"
RELATES = "<http://vivoweb.org/ontology/core#relates>"
RELATED_BY = "<http://vivoweb.org/ontology/core#relatedBy>"
NUM_LINES = 37983245
MOST_SPECIFIC_TYPE = "<http://vitro.mannlib.cornell.edu/ns/vitro/0.7#mostSpecificType>"
TYPE_DATETIMEVALUE = "<http://vivoweb.org/ontology/core#DateTimeValue>"
TYPE_DATETIME = "<http://vivoweb.org/ontology/core#dateTime>"
TYPE_DATETIMEPRECISION = "<http://vivoweb.org/ontology/core#DateTimeValuePrecision>"
TYPE_DATETIMEINTERVAL = "<http://vivoweb.org/ontology/core#dateTimeInterval>"

INDIVIDUAL = re.compile("<http:\/\/vivo\.ufl\.edu\/individual\/[\w-]+>")
def is_individual(uri):
    return INDIVIDUAL.match(uri)

datetime_types = [TYPE_DATETIME, TYPE_DATETIMEINTERVAL, TYPE_DATETIMEPRECISION, TYPE_DATETIMEVALUE]
def is_datetime(t):
    return t in datetime_types