from parse import get_lines, parse_line, get_data
from rdf import TYPE, LABEL, RELATES, RELATED_BY, NUM_LINES, is_individual
from utils import get_obj, transpose_dict, dump_obj
from collections import defaultdict

orphans = set(get_obj('regex_orphans_orphans.pkl'))
types = defaultdict(int)
line_count = 0
for s, p, o in map(parse_line, get_data()):
    line_count += 1
    if line_count % 100000 == 0:
        print(line_count, '/', NUM_LINES)
    
    if p == TYPE and s in orphans:
        types[o] += 1

dump_obj('regex_orphans_types.pkl', dict(types))

"""
sorted(types.items(), key = lambda x: x[1])
[('<http://www.w3.org/2002/07/owl#Thing>', 90425), ('<http://purl.obolibrary.org/obo/BFO_0000001>', 45322), ('<http://purl.obolibrary.org/obo/BFO_0000003>', 38786), ('<http://vivoweb.org/ontology/core#DateTimeValue>', 38543), ('<http://purl.obolibrary.org/obo/BFO_0000008>', 38543), ('<http://purl.obolibrary.org/obo/BFO_0000148>', 38543), ('<http://vivoweb.org/ontology/core#Role>', 27015), ('<http://vitro.mannlib.cornell.edu/ns/vitro/0.7#Namespace>', 15542), ('<http://purl.obolibrary.org/obo/BFO_0000002>', 6536), ('<http://purl.obolibrary.org/obo/BFO_0000004>', 4479), ('<http://xmlns.com/foaf/0.1/Agent>', 3233), ('<http://xmlns.com/foaf/0.1/Organization>', 3087), ('<http://vivoweb.org/ontology/core#FundingOrganization>', 2602), ('<http://purl.obolibrary.org/obo/BFO_0000020>', 1751), ('<http://purl.obolibrary.org/obo/BFO_0000017>', 1489), ('<http://purl.obolibrary.org/obo/BFO_0000023>', 1489), ('<http://vivoweb.org/ontology/core#Company>', 1487), ('<http://vivoweb.org/ontology/core#ResearcherRole>', 1447), ('<http://vivoweb.org/ontology/core#InvestigatorRole>', 1446), ('<http://vivoweb.org/ontology/core#GeographicLocation>', 1246), ('<http://vivoweb.org/ontology/core#Location>', 1246), ('<http://purl.obolibrary.org/obo/BFO_0000006>', 1246), ('<http://purl.obolibrary.org/obo/BFO_0000141>', 1246), ('<http://purl.obolibrary.org/obo/IAO_0000030>', 1241), ('<http://purl.obolibrary.org/obo/BFO_0000031>', 1241), ('<http://vivoweb.org/ontology/core#Building>', 935), ('<http://purl.obolibrary.org/obo/BFO_0000029>', 935), ('<http://purl.obolibrary.org/obo/ARG_2000379>', 935), ('<http://www.w3.org/2006/vcard/ns#Kind>', 935), ('<http://vivoweb.org/ontology/core#Facility>', 935), ('<http://www.w3.org/2006/vcard/ns#Location>', 935), ('<http://www.w3.org/2006/vcard/ns#Explanatory>', 782), ('<http://www.w3.org/2006/vcard/ns#Addressing>', 782), ('<http://www.w3.org/2006/vcard/ns#Communication>', 782), ('<http://www.w3.org/2006/vcard/ns#Identification>', 782), ('<http://www.w3.org/2006/vcard/ns#URL>', 780), ('<http://vivoweb.org/ontology/core#Association>', 361), ('<http://vivoweb.org/ontology/core#PrincipalInvestigatorRole>', 358), ('<http://vivoweb.org/ontology/core#Publisher>', 352), ('<http://vivoweb.org/ontology/core#GeographicRegion>', 311), ('<http://vivoweb.org/ontology/core#GeopoliticalEntity>', 311), ('<http://vivoweb.org/ontology/core#InformationResource>', 304), ('<http://vivoweb.org/ontology/core#Relationship>', 262), ('<http://vivoweb.org/ontology/core#Foundation>', 260), ('<http://purl.org/ontology/bibo/Collection>', 257), ('<http://vivoweb.org/ontology/core#PopulatedPlace>', 255), ('<http://purl.org/ontology/bibo/Periodical>', 249), ('<http://purl.obolibrary.org/obo/BFO_0000015>', 243), ('<http://purl.org/NET/c4dm/event.owl#Event>', 233), ('<http://purl.org/ontology/bibo/Journal>', 225), ('<http://vivoweb.org/ontology/core#GovernmentAgency>', 208), ('<http://vivoweb.org/ontology/core#AwardReceipt>', 172), ('<http://www.w3.org/2004/02/skos/core#Concept>', 152), ('<http://purl.org/ontology/bibo/Conference>', 142), ('<http://vivoweb.org/ontology/core#dateTime>', 105), ('<http://vivoweb.org/ontology/core#University>', 105), ('<http://vivoweb.org/ontology/core#CoPrincipalInvestigatorRole>', 100), ('<http://vivoweb.org/ontology/core#Institute>', 97), ('<http://vivoweb.org/ontology/core#ResearchOrganization>', 79), ('<http://xmlns.com/foaf/0.1/Person>', 76), ('<http://xmlns.com/foaf/0.1/Group>', 69), ('<http://vivoweb.org/ontology/core#Committee>', 65), ('<http://vivoweb.org/ontology/core#County>', 56), ('<http://vivoweb.org/ontology/core#Grant>', 53), ('<http://vivoweb.org/ontology/core#Agreement>', 53), ('<http://purl.org/ontology/bibo/Document>', 48), ('<http://vivoweb.org/ontology/core#Center>', 47), ('<http://vivo.ufl.edu/ontology/vivo-ufl/UFEntity>', 44), ('<http://vivo.ufl.edu/ontology/vivo-ufl/GraduateAdvisoryCommittee>', 44), ('<http://vivoweb.org/ontology/core#ClinicalOrganization>', 37), ('<http://vivoweb.org/ontology/core#Program>', 34), ('<http://purl.org/ontology/bibo/Article>', 33), ('<http://vivoweb.org/ontology/core#Department>', 32), ('<http://vivoweb.org/ontology/core#Presentation>', 31), ('<http://purl.obolibrary.org/obo/ERO_0000012>', 27), ('<http://vivoweb.org/ontology/core#Course>', 23), ('<http://purl.org/ontology/bibo/AcademicArticle>', 20), ('<http://vivoweb.org/ontology/core#AdvisingRelationship>', 19), ('<http://vivo.ufl.edu/ontology/vivo-ufl/UFCurrentEntity>', 19), ('<http://vivoweb.org/ontology/core#InvitedTalk>', 17), ('<http://vivoweb.org/ontology/core#College>', 17), ('<http://vivoweb.org/ontology/core#AcademicDepartment>', 15), ('<http://vivoweb.org/ontology/core#Laboratory>', 14), ('<http://vivoweb.org/ontology/core#FacultyMember>', 13), ('<http://vivoweb.org/ontology/core#Address>', 12), ('<http://vivoweb.org/ontology/core#OutreachProviderRole>', 12), ('<http://vivoweb.org/ontology/core#Authorship>', 11), ('<http://vivoweb.org/ontology/core#NonAcademic>', 9), ('<http://vivoweb.org/ontology/core#AcademicDegree>', 9), ('<http://vivoweb.org/ontology/core#School>', 9), ('<http://vivoweb.org/ontology/core#Award>', 7), ('<http://vitro.mannlib.cornell.edu/ns/vitro/public#FileByteStream>', 7), ('<http://purl.org/ontology/bibo/Book>', 7), ('<http://vivo.ufl.edu/ontology/vivo-ufl/Abstract>', 6), ('<http://vivoweb.org/ontology/core#SeminarSeries>', 6), ('<http://vivoweb.org/ontology/core#EventSeries>', 6), ('<http://vivoweb.org/ontology/core#Division>', 5), ('<http://vivoweb.org/ontology/core#USPostalAddress>', 4), ('<http://vivo.ufl.edu/ontology/vivo-ufl/CourtesyFaculty>', 4), ('<http://vivoweb.org/ontology/core#ConferencePaper>', 4), ('<http://purl.org/ontology/bibo/Proceedings>', 4), ('<http://vivoweb.org/ontology/core#Hospital>', 4), ('<http://purl.org/ontology/bibo/Website>', 4), ('<http://vivoweb.org/ontology/core#Newsletter>', 3), ('<http://vivoweb.org/ontology/core#Team>', 3), ('<http://vivoweb.org/ontology/core#EducationalProcess>', 3), ('<http://vivoweb.org/ontology/core#Blog>', 3), ('<http://vivoweb.org/ontology/core#Museum>', 3), ('<http://vivoweb.org/ontology/core#URLLink>', 3), ('<http://purl.obolibrary.org/obo/ERO_0000005>', 2), ('<http://purl.org/ontology/bibo/Workshop>', 2), ('<http://vivoweb.org/ontology/core#NewsRelease>', 2), ('<http://vivoweb.org/ontology/core#StudentOrganization>', 2), ('<http://vivoweb.org/ontology/core#EditorialArticle>', 2), ('<http://vivoweb.org/ontology/core#Review>', 2), ('<http://purl.org/ontology/bibo/Magazine>', 2), ('<http://vivo.ufl.edu/ontology/vivo-ufl/TRCatalogLink>', 2), ('<http://vivo.ufl.edu/ontology/vivo-ufl/NonGovernmentalOrganization>', 2), ('<http://vivoweb.org/ontology/core#GraduateAdvisingRelationship>', 2), ('<http://purl.org/ontology/bibo/Webpage>', 2), ('<http://vivoweb.org/ontology/core#Student>', 2), ('<http://purl.org/ontology/bibo/Series>', 2), ('<http://purl.org/ontology/bibo/Patent>', 2), ('<http://www.w3.org/2006/vcard/ns#Code>', 2), ('<http://purl.obolibrary.org/obo/ERO_0000014>', 1), ('<http://vivoweb.org/ontology/core#TeacherRole>', 1), ('<http://vivoweb.org/ontology/core#Database>', 1), ('<http://vivoweb.org/ontology/core#AdvisorRole>', 1), ('<http://vivo.ufl.edu/ontology/vivo-ufl/AdministrativeUnit>', 1), ('<http://vitro.mannlib.cornell.edu/ns/vitro/public#File>', 1), ('<http://vivoweb.org/ontology/core#AdviseeRole>', 1), ('<http://vivo.ufl.edu/ontology/vivo-ufl/FullTextURL>', 1), ('<http://vivoweb.org/ontology/core#ExtensionUnit>', 1), ('<http://vivoweb.org/ontology/core#PrivateCompany>', 1), ('<http://vivoweb.org/ontology/core#Consortium>', 1), ('<http://vivo.ufl.edu/ontology/vivo-ufl/ExtensionDocument>', 1), ('<http://vivoweb.org/ontology/core#CaseStudy>', 1), ('<http://www.w3.org/2006/vcard/ns#Work>', 1), ('<http://www.w3.org/2006/vcard/ns#Email>', 1), ('<http://purl.org/ontology/bibo/Newspaper>', 1), ('<http://vivoweb.org/ontology/core#BlogPosting>', 1), ('<http://vivoweb.org/ontology/core#Meeting>', 1), ('<http://vivoweb.org/ontology/core#NonFacultyAcademic>', 1), ('<http://purl.org/ontology/bibo/BookSection>', 1), ('<http://purl.org/ontology/bibo/Chapter>', 1), ('<http://purl.org/ontology/bibo/DocumentPart>', 1), ('<http://vivoweb.org/ontology/core#UndergraduateStudent>', 1), ('<http://www.w3.org/2006/vcard/ns#Telephone>', 1), ('<http://www.w3.org/2006/vcard/ns#Fax>', 1), ('<http://vivoweb.org/ontology/core#WorkingPaper>', 1), ('<http://vivoweb.org/ontology/core#Process>', 1), ('<http://purl.obolibrary.org/obo/OBI_0000011>', 1), ('<http://vivoweb.org/ontology/core#Project>', 1), ('<http://purl.org/ontology/bibo/CollectedDocument>', 1), ('<http://www.w3.org/2006/vcard/ns#Type>', 1), ('<http://www.w3.org/2006/vcard/ns#TelephoneType>', 1), ('<http://vitro.mannlib.cornell.edu/ns/vitro/0.7#ClassGroup>', 1)]

[ x for x in sorted(list(t.items()), key=lambda t: -t[1]) if x[0].startswith("<http://vivoweb.org") ]
[('<http://vivoweb.org/ontology/core#DateTimeValue>', 38543), ('<http://vivoweb.org/ontology/core#Role>', 27015), ('<http://vivoweb.org/ontology/core#FundingOrganization>', 2602), ('<http://vivoweb.org/ontology/core#Company>', 1487), ('<http://vivoweb.org/ontology/core#ResearcherRole>', 1447), ('<http://vivoweb.org/ontology/core#InvestigatorRole>', 1446), ('<http://vivoweb.org/ontology/core#GeographicLocation>', 1246), ('<http://vivoweb.org/ontology/core#Location>', 1246), ('<http://vivoweb.org/ontology/core#Building>', 935), ('<http://vivoweb.org/ontology/core#Facility>', 935), ('<http://vivoweb.org/ontology/core#Association>', 361), ('<http://vivoweb.org/ontology/core#PrincipalInvestigatorRole>', 358), ('<http://vivoweb.org/ontology/core#Publisher>', 352), ('<http://vivoweb.org/ontology/core#GeographicRegion>', 311), ('<http://vivoweb.org/ontology/core#GeopoliticalEntity>', 311), ('<http://vivoweb.org/ontology/core#InformationResource>', 304), ('<http://vivoweb.org/ontology/core#Relationship>', 262), ('<http://vivoweb.org/ontology/core#Foundation>', 260), ('<http://vivoweb.org/ontology/core#PopulatedPlace>', 255), ('<http://vivoweb.org/ontology/core#GovernmentAgency>', 208), ('<http://vivoweb.org/ontology/core#AwardReceipt>', 172), ('<http://vivoweb.org/ontology/core#dateTime>', 105), ('<http://vivoweb.org/ontology/core#University>', 105), ('<http://vivoweb.org/ontology/core#CoPrincipalInvestigatorRole>', 100), ('<http://vivoweb.org/ontology/core#Institute>', 97), ('<http://vivoweb.org/ontology/core#ResearchOrganization>', 79), ('<http://vivoweb.org/ontology/core#Committee>', 65), ('<http://vivoweb.org/ontology/core#County>', 56), ('<http://vivoweb.org/ontology/core#Grant>', 53), ('<http://vivoweb.org/ontology/core#Agreement>', 53), ('<http://vivoweb.org/ontology/core#Center>', 47), ('<http://vivoweb.org/ontology/core#ClinicalOrganization>', 37), ('<http://vivoweb.org/ontology/core#Program>', 34), ('<http://vivoweb.org/ontology/core#Department>', 32), ('<http://vivoweb.org/ontology/core#Presentation>', 31), ('<http://vivoweb.org/ontology/core#Course>', 23), ('<http://vivoweb.org/ontology/core#AdvisingRelationship>', 19), ('<http://vivoweb.org/ontology/core#InvitedTalk>', 17), ('<http://vivoweb.org/ontology/core#College>', 17), ('<http://vivoweb.org/ontology/core#AcademicDepartment>', 15), ('<http://vivoweb.org/ontology/core#Laboratory>', 14), ('<http://vivoweb.org/ontology/core#FacultyMember>', 13), ('<http://vivoweb.org/ontology/core#Address>', 12), ('<http://vivoweb.org/ontology/core#OutreachProviderRole>', 12), ('<http://vivoweb.org/ontology/core#Authorship>', 11), ('<http://vivoweb.org/ontology/core#NonAcademic>', 9), ('<http://vivoweb.org/ontology/core#AcademicDegree>', 9), ('<http://vivoweb.org/ontology/core#School>', 9), ('<http://vivoweb.org/ontology/core#Award>', 7), ('<http://vivoweb.org/ontology/core#SeminarSeries>', 6), ('<http://vivoweb.org/ontology/core#EventSeries>', 6), ('<http://vivoweb.org/ontology/core#Division>', 5), ('<http://vivoweb.org/ontology/core#USPostalAddress>', 4), ('<http://vivoweb.org/ontology/core#ConferencePaper>', 4), ('<http://vivoweb.org/ontology/core#Hospital>', 4), ('<http://vivoweb.org/ontology/core#Newsletter>', 3), ('<http://vivoweb.org/ontology/core#Team>', 3), ('<http://vivoweb.org/ontology/core#EducationalProcess>', 3), ('<http://vivoweb.org/ontology/core#Blog>', 3), ('<http://vivoweb.org/ontology/core#Museum>', 3), ('<http://vivoweb.org/ontology/core#URLLink>', 3), ('<http://vivoweb.org/ontology/core#NewsRelease>', 2), ('<http://vivoweb.org/ontology/core#StudentOrganization>', 2), ('<http://vivoweb.org/ontology/core#EditorialArticle>', 2), ('<http://vivoweb.org/ontology/core#Review>', 2), ('<http://vivoweb.org/ontology/core#GraduateAdvisingRelationship>', 2), ('<http://vivoweb.org/ontology/core#Student>', 2), ('<http://vivoweb.org/ontology/core#TeacherRole>', 1), ('<http://vivoweb.org/ontology/core#Database>', 1), ('<http://vivoweb.org/ontology/core#AdvisorRole>', 1), ('<http://vivoweb.org/ontology/core#AdviseeRole>', 1), ('<http://vivoweb.org/ontology/core#ExtensionUnit>', 1), ('<http://vivoweb.org/ontology/core#PrivateCompany>', 1), ('<http://vivoweb.org/ontology/core#Consortium>', 1), ('<http://vivoweb.org/ontology/core#CaseStudy>', 1), ('<http://vivoweb.org/ontology/core#BlogPosting>', 1), ('<http://vivoweb.org/ontology/core#Meeting>', 1), ('<http://vivoweb.org/ontology/core#NonFacultyAcademic>', 1), ('<http://vivoweb.org/ontology/core#UndergraduateStudent>', 1), ('<http://vivoweb.org/ontology/core#WorkingPaper>', 1), ('<http://vivoweb.org/ontology/core#Process>', 1), ('<http://vivoweb.org/ontology/core#Project>', 1)]

[ x for x in sorted(list(t.items()), key=lambda t: -t[1]) if x[0].startswith("<http://www.w3.org/2006/vcard/") ]
[('<http://www.w3.org/2006/vcard/ns#Kind>', 935), ('<http://www.w3.org/2006/vcard/ns#Location>', 935), ('<http://www.w3.org/2006/vcard/ns#Explanatory>', 782), ('<http://www.w3.org/2006/vcard/ns#Addressing>', 782), ('<http://www.w3.org/2006/vcard/ns#Communication>', 782), ('<http://www.w3.org/2006/vcard/ns#Identification>', 782), ('<http://www.w3.org/2006/vcard/ns#URL>', 780), ('<http://www.w3.org/2006/vcard/ns#Code>', 2), ('<http://www.w3.org/2006/vcard/ns#Work>', 1), ('<http://www.w3.org/2006/vcard/ns#Email>', 1), ('<http://www.w3.org/2006/vcard/ns#Telephone>', 1), ('<http://www.w3.org/2006/vcard/ns#Fax>', 1), ('<http://www.w3.org/2006/vcard/ns#Type>', 1), ('<http://www.w3.org/2006/vcard/ns#TelephoneType>', 1)]

[ x for x in sorted(list(t.items()), key=lambda t: -t[1]) if x[0].startswith("<http://xmlns.com/foaf/") ]
[('<http://xmlns.com/foaf/0.1/Agent>', 3233), ('<http://xmlns.com/foaf/0.1/Organization>', 3087), ('<http://xmlns.com/foaf/0.1/Person>', 76), ('<http://xmlns.com/foaf/0.1/Group>', 69)]
"""