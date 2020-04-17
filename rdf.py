import re

NUM_LINES = 37983245

ASSIGNED_BY = "<http://vivoweb.org/ontology/core#assignedBy>"
ASSIGNS = "<http://vivoweb.org/ontology/core#assigns>"
AUTHORSHIP = "<http://vivoweb.org/ontology/core#Authorship>"
BEARER_OF = "<http://purl.obolibrary.org/obo/RO_0000053>"
CONTACT_INFO_FOR = "<http://purl.obolibrary.org/obo/ARG_2000029>"
CONTRIBUTING_ROLE = "<http://vivoweb.org/ontology/core#contributingRole>"
DATETIMEINTERVAL_OF = "<http://vivoweb.org/ontology/core#dateTimeInterval>"
DATETIMEVALUE_OF = "<http://vivoweb.org/ontology/core#dateTimeValue>"
HAS_CONTACT_INFO = "<http://purl.obolibrary.org/obo/ARG_2000028>"
HAS_PARTICIPANT = "<http://purl.obolibrary.org/obo/RO_0000057>"
INHERES_IN = "<http://purl.obolibrary.org/obo/RO_0000052>"
LABEL = "<http://www.w3.org/2000/01/rdf-schema#label>"
MOST_SPECIFIC_TYPE = "<http://vitro.mannlib.cornell.edu/ns/vitro/0.7#mostSpecificType>"
PARTICIPATES_IN = "<http://purl.obolibrary.org/obo/RO_0000056>"
RELATED_BY = "<http://vivoweb.org/ontology/core#relatedBy>"
RELATES = "<http://vivoweb.org/ontology/core#relates>"
ROLE_CONTRIBUTES_TO = "<http://vivoweb.org/ontology/core#roleContributesTo>"
TYPE = "<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>"

TYPE_ACADEMIC_ARTICLE = "<http://purl.org/ontology/bibo/AcademicArticle>"
TYPE_ACADEMIC_DEGREE = "<http://vivoweb.org/ontology/core#AcademicDegree>"
TYPE_ADVISING_RELATIONSHIP = "<http://vivoweb.org/ontology/core#AdvisingRelationship>"
TYPE_ADVISOR_ROLE = "<http://vivoweb.org/ontology/core#AdvisorRole>"
TYPE_ADVISEE_ROLE = "<http://vivoweb.org/ontology/core#AdviseeRole>"
TYPE_AGENT = "<http://xmlns.com/foaf/0.1/Agent>"
TYPE_ANY = "**any type**"
TYPE_EDGE_ANY = "**any edge**"
TYPE_AUTHORSHIP = AUTHORSHIP
TYPE_AWARD = "<http://vivoweb.org/ontology/core#Award>"
TYPE_AWARD_RECEIPT = "<http://vivoweb.org/ontology/core#AwardReceipt>"
TYPE_AWARDED_DEGREE = "<http://vivoweb.org/ontology/core#AwardedDegree>"
TYPE_COMMITTEE = "<http://vivoweb.org/ontology/core#Committee>"
TYPE_CONCEPT = "<http://www.w3.org/2004/02/skos/core#Concept>"
TYPE_CREDENTIAL = "<http://vivoweb.org/ontology/core#Credential>"
TYPE_DATETIME = "<http://vivoweb.org/ontology/core#dateTime>"
TYPE_DATETIMEINTERVAL = "<http://vivoweb.org/ontology/core#DateTimeInterval>"
TYPE_DATETIMEPRECISION = "<http://vivoweb.org/ontology/core#DateTimeValuePrecision>"
TYPE_DATETIMEVALUE = "<http://vivoweb.org/ontology/core#DateTimeValue>"
TYPE_EDUCATIONAL_PROCESS = "<http://vivoweb.org/ontology/core#EducationalProcess>"
TYPE_FILE = "<http://vitro.mannlib.cornell.edu/ns/vitro/public#File>"
TYPE_FOAF_ORGANIZATION = "<http://xmlns.com/foaf/0.1/Organization>"
TYPE_GRANT = "<http://vivoweb.org/ontology/core#Grant>"
TYPE_INDIVIDUAL = "<http://www.w3.org/2006/vcard/ns#Individual>"
TYPE_INFORMATION_CONTENT_ENTITY = "<http://purl.obolibrary.org/obo/IAO_0000030>"
TYPE_ISSUED_CREDENTIAL = "<http://vivoweb.org/ontology/core#IssuedCredential>"
TYPE_KIND = "<http://www.w3.org/2006/vcard/ns#Kind>"
TYPE_MEMBERSHIP = "<http://vivoweb.org/ontology/core#MemberRole>"
TYPE_PERSON = "<http://xmlns.com/foaf/0.1/Person>"
TYPE_POSITION = "<http://vivoweb.org/ontology/core#Position>"
TYPE_UNIVERSITY = "<http://vivoweb.org/ontology/core#University>"
TYPE_VCARD_ORGANIZATION = "<http://www.w3.org/2006/vcard/ns#Organization>"

INDIVIDUAL = re.compile("<http:\/\/vivo\.ufl\.edu\/+individual\/+[\w-]+>")
def is_individual(uri):
    return INDIVIDUAL.match(uri)

datetime_types = [TYPE_DATETIME, TYPE_DATETIMEINTERVAL, TYPE_DATETIMEPRECISION, TYPE_DATETIMEVALUE]
def is_datetime(t):
    return t in datetime_types

def get_type_short_name(uri):
    uri_prefixes = ["<http://purl.org/NET/c4dm/event.owl#", "<http://www.w3.org/2004/02/skos/core#", "<http://xmlns.com/foaf/0.1/", "<http://purl.obolibrary.org/obo/", "<http://vivo.ufl.edu/ontology/vivo-ufl/", "<http://www.w3.org/2006/vcard/ns#", "<http://vivoweb.org/ontology/core#", "<http://vitro.mannlib.cornell.edu/ns/vitro/0.7#", "<http://vitro.mannlib.cornell.edu/ns/vitro/public#", "<http://www.w3.org/2002/07/owl#", "<http://purl.org/ontology/bibo/"]
    name_prefixes = ["c4dm", "skos", "foaf", "obo", "ufvivo", "vcard", "vivo", "vitro", "vitro", "owl", "bibo"]
    for uri_prefix, name_prefix in zip(uri_prefixes, name_prefixes):
        if uri.startswith(uri_prefix):
            return name_prefix + ":" + uri[len(uri_prefix) : -1]
    return "unknown:" + uri