from parse import parse_line, get_data
from utils import dump_obj, get_obj, histogram
from rdf import *
from union_find import UnionFind

uridegree = get_obj('uri_to_degree.pkl')

HIGH_DEGREE_MIN = 100
high_degree_uris = set(uri for (uri, degree) in uridegree.items() if degree > HIGH_DEGREE_MIN)

sets = UnionFind()
line_count = 0
for s, p, o in map(parse_line, get_data()):
    line_count += 1
    if line_count % 100000 == 0:
        print(line_count, '/', NUM_LINES)

    is_subject_individual = is_individual(s)
    is_object_individual = is_individual(o)

    should_ignore_subject = (not is_subject_individual) or (s in high_degree_uris)
    should_ignore_object = (not is_object_individual) or (o in high_degree_uris)

    if not should_ignore_subject:
        sets.add(s)
    if not should_ignore_object:
        sets.add(o)
    if (not should_ignore_subject) and (not should_ignore_object):
        sets.union(s, o)

components = sets.components()

# h = histogram(map(len, components))
# list(sorted(h.items(), key = lambda x: -x[0]))
# [(1498104, 1), (421, 1), (411, 1), (376, 1), (363, 1), (356, 1), (347, 1), (320, 1), (310, 1), (308, 1), (267, 1), (255, 1), (249, 1), (221, 2), (214, 1), (200, 1), (194, 1), (193, 2), (192, 1), (187, 1), (185, 1), (184, 2), (182, 2), (181, 1), (180, 1), (179, 1), (176, 1), (174, 1), (171, 1), (168, 2), (167, 1), (166, 2), (162, 1), (160, 1), (159, 1), (157, 3), (156, 2), (154, 1), (151, 2), (150, 2), (149, 3), (148, 1), (146, 2), (145, 1), (144, 1), (143, 1), (142, 1), (140, 2), (139, 5), (136, 1), (134, 1), (133, 3), (132, 2), (131, 2), (130, 1), (129, 3), (128, 4), (127, 2), (126, 3), (125, 5), (124, 2), (123, 2), (122, 3), (121, 3), (120, 4), (119, 3), (118, 5), (117, 2), (115, 4), (114, 3), (113, 2), (112, 3), (111, 4), (110, 2), (109, 3), (108, 4), (107, 3), (106, 5), (105, 8), (104, 5), (103, 4), (102, 6), (101, 6), (100, 4), (99, 5), (98, 9), (97, 13), (96, 9), (95, 10), (94, 7), (93, 5), (92, 4), (91, 8), (90, 7), (89, 10), (88, 6), (87, 4), (86, 4), (85, 13), (84, 7), (83, 10), (82, 13), (81, 5), (80, 11), (79, 8), (78, 14), (77, 16), (76, 12), (75, 12), (74, 11), (73, 22), (72, 18), (71, 6), (70, 21), (69, 19), (68, 18), (67, 32), (66, 28), (65, 34), (64, 30), (63, 14), (62, 26), (61, 30), (60, 32), (59, 37), (58, 40), (57, 28), (56, 36), (55, 23), (54, 47), (53, 39), (52, 43), (51, 40), (50, 69), (49, 59), (48, 49), (47, 32), (46, 55), (45, 52), (44, 57), (43, 71), (42, 99), (41, 66), (40, 99), (39, 62), (38, 138), (37, 98), (36, 114), (35, 101), (34, 140), (33, 101), (32, 126), (31, 96), (30, 188), (29, 167), (28, 202), (27, 189), (26, 235), (25, 224), (24, 237), (23, 217), (22, 303), (21, 323), (20, 285), (19, 311), (18, 448), (17, 413), (16, 537), (15, 594), (14, 928), (13, 1528), (12, 3283), (11, 1790), (10, 2649), (9, 2327), (8, 3821), (7, 5318), (6, 6270), (5, 15759), (4, 62352), (3, 16557), (2, 50365), (1, 157073)]
dump_obj('components_no_high_degree.pkl', sets.components())
