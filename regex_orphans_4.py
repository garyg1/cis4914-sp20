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
    
    if p == MOST_SPECIFIC_TYPE and s in orphans:
        types[s].append(o)

dump_obj('regex_orphans_with_types.pkl', dict(types))

"""
[('vivo:DateTimeValue', 38543), ('vivo:Role', 25555), ('vitro:Namespace', 15542), ('owl:Thing', 3067), ('vivo:FundingOrganization', 2602), ('vivo:Company', 1486), ('vivo:InvestigatorRole', 988), ('vivo:Building', 935), ('vcard:URL', 780), ('vivo:Association', 361), ('vivo:PrincipalInvestigatorRole', 358), ('vivo:Publisher', 352), ('vivo:Foundation', 260), ('vivo:PopulatedPlace', 255), ('bibo:Journal', 225), ('vivo:GovernmentAgency', 209), ('vivo:AwardReceipt', 172), ('bibo:Conference', 142), ('skos:Concept', 136), ('vivo:University', 105), ('vivo:CoPrincipalInvestigatorRole', 100), ('vivo:Institute', 97), ('vivo:ResearchOrganization', 79), ('vivo:dateTime', 73), ('foaf:Person', 71), ('vivo:County', 56), ('vivo:Grant', 53), ('vivo:Center', 47), ('ufvivo:UFEntity', 45), ('ufvivo:GraduateAdvisoryCommittee', 44), ('vivo:ClinicalOrganization', 37), ('c4dm:Event', 34), ('vivo:Program', 34), ('obo:ERO_0000012', 27), ('vivo:Course', 23), ('vivo:Committee', 21), ('bibo:AcademicArticle', 20), ('ufvivo:UFCurrentEntity', 19), ('bibo:Periodical', 18), ('vivo:AdvisingRelationship', 17), ('vivo:Department', 17), ('vivo:InvitedTalk', 17), ('vivo:College', 17), ('vivo:AcademicDepartment', 15), ('vivo:Presentation', 14), ('vivo:Laboratory', 14), ('vivo:FacultyMember', 13), ('vivo:OutreachProviderRole', 12), ('vivo:Authorship', 11), ('vivo:NonAcademic', 9), ('foaf:Agent', 9), ('vivo:AcademicDegree', 9), ('vivo:School', 9), ('vivo:Relationship', 8), ('vivo:Address', 8), ('vivo:Award', 7), ('vitro:FileByteStream', 7), ('foaf:Organization', 7), ('ufvivo:Abstract', 6), ('vivo:SeminarSeries', 6), ('vivo:Division', 5), ('obo:BFO_0000004', 5), ('vivo:USPostalAddress', 4), ('ufvivo:CourtesyFaculty', 4), ('vivo:ConferencePaper', 4), ('bibo:Proceedings', 4), ('vivo:Hospital', 4), ('bibo:Article', 4), ('vivo:Newsletter', 3), ('vivo:Team', 3), ('bibo:Book', 3), ('vivo:EducationalProcess', 3), ('vivo:Blog', 3), ('vivo:Museum', 3), ('obo:ERO_0000005', 2), ('bibo:Workshop', 2), ('vivo:NewsRelease', 2), ('vivo:StudentOrganization', 2), ('vivo:EditorialArticle', 2), ('vivo:Review', 2), ('bibo:Magazine', 2), ('ufvivo:TRCatalogLink', 2), ('ufvivo:NonGovernmentalOrganization', 2), ('vivo:GraduateAdvisingRelationship', 2), ('bibo:Webpage', 2), ('bibo:Collection', 2), ('bibo:Series', 2), ('bibo:Patent', 2), ('obo:ERO_0000014', 1), ('vivo:TeacherRole', 1), ('vivo:Database', 1), ('vivo:AdvisorRole', 1), ('foaf:Group', 1), ('ufvivo:AdministrativeUnit', 1), ('vitro:File', 1), ('vivo:AdviseeRole', 1), ('ufvivo:FullTextURL', 1), ('vivo:ExtensionUnit', 1), ('vivo:PrivateCompany', 1), ('vivo:Consortium', 1), ('ufvivo:ExtensionDocument', 1), ('vivo:CaseStudy', 1), ('vcard:Work', 1), ('vcard:Email', 1), ('vivo:Student', 1), ('bibo:Newspaper', 1), ('vivo:BlogPosting', 1), ('ufvivo:Consultant', 1), ('vivo:Meeting', 1), ('vivo:ResearcherRole', 1), ('vivo:NonFacultyAcademic', 1), ('bibo:Chapter', 1), ('bibo:Website', 1), ('vivo:UndergraduateStudent', 1), ('vcard:Telephone', 1), ('vcard:Fax', 1), ('vitro:ClassGroup', 1), ('vivo:WorkingPaper', 1)]
"""