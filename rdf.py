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