from utils import dump_obj
from queries import query_orphans
from rdf import *

results = query_orphans([
    (TYPE_ISSUED_CREDENTIAL, TYPE_AGENT, RELATES, RELATED_BY),
    (TYPE_ISSUED_CREDENTIAL, TYPE_CREDENTIAL, RELATES, RELATED_BY),

    (TYPE_MEMBERSHIP, TYPE_PERSON, INHERES_IN, BEARER_OF),
    (TYPE_MEMBERSHIP, TYPE_COMMITTEE, ROLE_CONTRIBUTES_TO, CONTRIBUTING_ROLE),

    (TYPE_PERSON, TYPE_INDIVIDUAL, HAS_CONTACT_INFO, CONTACT_INFO_FOR),

    (TYPE_INDIVIDUAL, TYPE_ANY, CONTACT_INFO_FOR, HAS_CONTACT_INFO),
    (TYPE_VCARD_ORGANIZATION, TYPE_FOAF_ORGANIZATION, CONTACT_INFO_FOR, HAS_CONTACT_INFO),

    (TYPE_POSITION, TYPE_PERSON, RELATES, RELATED_BY),
    (TYPE_POSITION, TYPE_FOAF_ORGANIZATION, RELATES, RELATED_BY),

    (TYPE_DATETIMEINTERVAL, TYPE_ANY, TYPE_ANY, DATETIMEINTERVAL_OF),

    (TYPE_AUTHORSHIP, TYPE_AGENT, RELATES, RELATED_BY),
    (TYPE_AUTHORSHIP, TYPE_INFORMATION_CONTENT_ENTITY, RELATES, RELATED_BY),

    (TYPE_GRANT, TYPE_AGENT, RELATES, RELATED_BY),

    (TYPE_EDUCATIONAL_PROCESS, TYPE_PERSON, HAS_PARTICIPANT, PARTICIPATES_IN),
    (TYPE_EDUCATIONAL_PROCESS, TYPE_FOAF_ORGANIZATION, HAS_PARTICIPANT, PARTICIPATES_IN),
    
    (TYPE_AWARDED_DEGREE, TYPE_PERSON, RELATES, RELATED_BY),
    (TYPE_AWARDED_DEGREE, TYPE_FOAF_ORGANIZATION, ASSIGNED_BY, ASSIGNS),
    (TYPE_AWARDED_DEGREE, TYPE_ACADEMIC_DEGREE, RELATES, RELATED_BY),
    
    (TYPE_ADVISING_RELATIONSHIP, TYPE_PERSON, RELATES, RELATED_BY),
    (TYPE_ADVISING_RELATIONSHIP, TYPE_ADVISOR_ROLE, RELATES, RELATED_BY),
    (TYPE_ADVISING_RELATIONSHIP, TYPE_ADVISEE_ROLE, RELATES, RELATED_BY),
    
    (TYPE_AWARD_RECEIPT, TYPE_AWARD, RELATES, RELATED_BY),
    (TYPE_AWARD_RECEIPT, TYPE_AGENT, RELATES, RELATED_BY),
])

names = [
    'issued_credential_without_person.pkl',
    'issued_credential_without_credential.pkl',

    'membership_without_person.pkl',
    'membership_without_commmittee.pkl',
    
    'person_without_vcard.pkl',

    'vcard_without_person.pkl',
    'vcard_without_org.pkl',

    'position_without_person.pkl',
    'position_without_org.pkl',

    'datetimeinterval_without_parent.pkl',

    'authorship_without_person.pkl',
    'authorship_without_academic_article.pkl',

    'grant_without_person.pkl',

    'educational_process_without_person.pkl',
    'educational_process_without_org.pkl',
    
    'awarded_degree_without_person.pkl',
    'awarded_degree_without_org.pkl',
    'awarded_degree_without_academic_degree.pkl',
    
    'advising_relationship_without_person.pkl',
    'advising_relationship_without_advisor.pkl',
    'advising_relationship_without_advisee.pkl',
    
    'award_receipt_without_award.pkl',
    'award_receipt_without_person.pkl',
]

for name, (all, begin, end) in zip(names, results):
    print(name, len(all), len(begin), len(end))
    dump_obj(name, {'in-orphans': begin, 'out-orphans': end})