from parse import get_lines, parse_line, get_data
from rdf import *
from utils import get_obj, transpose_dict, dump_obj
from collections import defaultdict

orphans = set(get_obj('regex_orphans_orphans.pkl'))
types = defaultdict(list)
line_count = 0
for s, p, o in map(parse_line, get_data()):
    line_count += 1
    if line_count % 100000 == 0:
        print(line_count, '/', NUM_LINES)
    
    if p == TYPE and s in orphans:
        types[s].append(o)

dump_obj('regex_orphans_with_types.pkl', dict(types))
"""
dict_items([('<http://vivoweb.org/ontology/core#DateTimeValue>', 38543), ('<http://vitro.mannlib.cornell.edu/ns/vitro/0.7#Namespace>', 15542), ('<http://www.w3.org/2002/07/owl#Thing>', 3067), ('<http://vivoweb.org/ontology/core#Role>', 25555), ('<http://vivoweb.org/ontology/core#Company>', 1486), ('<http://vivoweb.org/ontology/core#FundingOrganization>', 2602), ('<http://vivoweb.org/ontology/core#AwardReceipt>', 172), ('<http://vivoweb.org/ontology/core#Foundation>', 260), ('<http://vivoweb.org/ontology/core#Building>', 935), ('<http://vivoweb.org/ontology/core#InvestigatorRole>', 988), ('<http://vivoweb.org/ontology/core#PopulatedPlace>', 255), ('<http://vivoweb.org/ontology/core#Association>', 361), ('<http://purl.org/ontology/bibo/Journal>', 225), ('<http://www.w3.org/2006/vcard/ns#URL>', 780), ('<http://vivoweb.org/ontology/core#PrincipalInvestigatorRole>', 358), ('<http://purl.org/NET/c4dm/event.owl#Event>', 34), ('<http://vivoweb.org/ontology/core#Publisher>', 352), ('<http://purl.obolibrary.org/obo/ERO_0000014>', 1), ('<http://vivoweb.org/ontology/core#County>', 56), ('<http://vivoweb.org/ontology/core#Relationship>', 8), ('<http://vivoweb.org/ontology/core#AdvisingRelationship>', 17), ('<http://vivoweb.org/ontology/core#Award>', 7), ('<http://www.w3.org/2004/02/skos/core#Concept>', 136), ('<http://vivoweb.org/ontology/core#Program>', 34), ('<http://vivoweb.org/ontology/core#ClinicalOrganization>', 37), ('<http://vivoweb.org/ontology/core#ResearchOrganization>', 79), ('<http://vivoweb.org/ontology/core#Institute>', 97), ('<http://vivoweb.org/ontology/core#Department>', 17), ('<http://vivo.ufl.edu/ontology/vivo-ufl/UFEntity>', 45), ('<http://xmlns.com/foaf/0.1/Person>', 71), ('<http://vivoweb.org/ontology/core#NonAcademic>', 9), ('<http://vivoweb.org/ontology/core#InvitedTalk>', 17), ('<http://vivoweb.org/ontology/core#GovernmentAgency>', 209), ('<http://purl.obolibrary.org/obo/ERO_0000005>', 2), ('<http://vivoweb.org/ontology/core#CoPrincipalInvestigatorRole>', 100), ('<http://vivoweb.org/ontology/core#USPostalAddress>', 4), ('<http://vivoweb.org/ontology/core#Center>', 47), ('<http://vivoweb.org/ontology/core#Course>', 23), ('<http://purl.org/ontology/bibo/Conference>', 142), ('<http://vivoweb.org/ontology/core#College>', 17), ('<http://vivoweb.org/ontology/core#dateTime>', 73), ('<http://vivoweb.org/ontology/core#University>', 105), ('<http://vivoweb.org/ontology/core#TeacherRole>', 1), ('<http://vivoweb.org/ontology/core#Authorship>', 11), ('<http://vitro.mannlib.cornell.edu/ns/vitro/public#FileByteStream>', 7), ('<http://vivo.ufl.edu/ontology/vivo-ufl/GraduateAdvisoryCommittee>', 44), ('<http://vivoweb.org/ontology/core#OutreachProviderRole>', 12), ('<http://purl.org/ontology/bibo/AcademicArticle>', 20), ('<http://vivoweb.org/ontology/core#Database>', 1), ('<http://vivoweb.org/ontology/core#Grant>', 53), ('<http://vivoweb.org/ontology/core#Newsletter>', 3), ('<http://purl.obolibrary.org/obo/ERO_0000012>', 27), ('<http://purl.org/ontology/bibo/Periodical>', 18), ('<http://vivo.ufl.edu/ontology/vivo-ufl/CourtesyFaculty>', 4), ('<http://vivoweb.org/ontology/core#Presentation>', 14), ('<http://vivoweb.org/ontology/core#Laboratory>', 14), ('<http://purl.org/ontology/bibo/Workshop>', 2), ('<http://vivoweb.org/ontology/core#ConferencePaper>', 4), ('<http://vivoweb.org/ontology/core#AdvisorRole>', 1), ('<http://vivoweb.org/ontology/core#NewsRelease>', 2), ('<http://vivoweb.org/ontology/core#Division>', 5), ('<http://vivo.ufl.edu/ontology/vivo-ufl/Abstract>', 6), ('<http://vivoweb.org/ontology/core#SeminarSeries>', 6), ('<http://xmlns.com/foaf/0.1/Agent>', 9), ('<http://vivo.ufl.edu/ontology/vivo-ufl/UFCurrentEntity>', 19), ('<http://vivoweb.org/ontology/core#FacultyMember>', 13), ('<http://vivoweb.org/ontology/core#Committee>', 21), ('<http://vivoweb.org/ontology/core#AcademicDegree>', 9), ('<http://vivoweb.org/ontology/core#AcademicDepartment>', 15), ('<http://vivoweb.org/ontology/core#Address>', 8), ('<http://vivoweb.org/ontology/core#Team>', 3), ('<http://xmlns.com/foaf/0.1/Group>', 1), ('<http://purl.org/ontology/bibo/Proceedings>', 4), ('<http://vivo.ufl.edu/ontology/vivo-ufl/AdministrativeUnit>', 1), ('<http://vivoweb.org/ontology/core#StudentOrganization>', 2), ('<http://vivoweb.org/ontology/core#Hospital>', 4), ('<http://vivoweb.org/ontology/core#School>', 9), ('<http://xmlns.com/foaf/0.1/Organization>', 7), ('<http://vivoweb.org/ontology/core#EditorialArticle>', 2), ('<http://purl.org/ontology/bibo/Article>', 4), ('<http://purl.obolibrary.org/obo/BFO_0000004>', 5), ('<http://vitro.mannlib.cornell.edu/ns/vitro/public#File>', 1), ('<http://purl.org/ontology/bibo/Book>', 3), ('<http://vivoweb.org/ontology/core#Review>', 2), ('<http://vivoweb.org/ontology/core#EducationalProcess>', 3), ('<http://purl.org/ontology/bibo/Magazine>', 2), ('<http://vivoweb.org/ontology/core#Blog>', 3), ('<http://vivo.ufl.edu/ontology/vivo-ufl/TRCatalogLink>', 2), ('<http://vivo.ufl.edu/ontology/vivo-ufl/NonGovernmentalOrganization>', 2), ('<http://vivoweb.org/ontology/core#AdviseeRole>', 1), ('<http://vivoweb.org/ontology/core#Museum>', 3), ('<http://vivoweb.org/ontology/core#GraduateAdvisingRelationship>', 2), ('<http://vivo.ufl.edu/ontology/vivo-ufl/FullTextURL>', 1), ('<http://vivoweb.org/ontology/core#ExtensionUnit>', 1), ('<http://purl.org/ontology/bibo/Webpage>', 2), ('<http://vivoweb.org/ontology/core#PrivateCompany>', 1), ('<http://vivoweb.org/ontology/core#Consortium>', 1), ('<http://vivo.ufl.edu/ontology/vivo-ufl/ExtensionDocument>', 1), ('<http://vivoweb.org/ontology/core#CaseStudy>', 1), ('<http://www.w3.org/2006/vcard/ns#Work>', 1), ('<http://www.w3.org/2006/vcard/ns#Email>', 1), ('<http://vivoweb.org/ontology/core#Student>', 1), ('<http://purl.org/ontology/bibo/Collection>', 2), ('<http://purl.org/ontology/bibo/Newspaper>', 1), ('<http://vivoweb.org/ontology/core#BlogPosting>', 1), ('<http://vivo.ufl.edu/ontology/vivo-ufl/Consultant>', 1), ('<http://vivoweb.org/ontology/core#Meeting>', 1), ('<http://vivoweb.org/ontology/core#ResearcherRole>', 1), ('<http://purl.org/ontology/bibo/Series>', 2), ('<http://vivoweb.org/ontology/core#NonFacultyAcademic>', 1), ('<http://purl.org/ontology/bibo/Chapter>', 1), ('<http://purl.org/ontology/bibo/Website>', 1), ('<http://vivoweb.org/ontology/core#UndergraduateStudent>', 1), ('<http://purl.org/ontology/bibo/Patent>', 2), ('<http://www.w3.org/2006/vcard/ns#Telephone>', 1), ('<http://www.w3.org/2006/vcard/ns#Fax>', 1), ('<http://vitro.mannlib.cornell.edu/ns/vitro/0.7#ClassGroup>', 1), ('<http://vivoweb.org/ontology/core#WorkingPaper>', 1)])
"""