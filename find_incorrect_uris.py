from utils import dump_obj, get_obj, histogram
from parse import get_lines, parse_line, get_data
from rdf import TYPE_POSITION, RELATED_BY, RELATES, TYPE_PERSON, is_individual, NUM_LINES

# ex: <http://vivo.ufl.edu/individual/n5291953887;http://vivo.ufl.edu/individual/n61770310;http://vivo.ufl.edu/individual/n449234168;http://vivo.ufl.edu/individual/n4920285818;http://vivo.ufl.edu/individual/n9213742161;http://vivo.ufl.edu/individual/n6980175982;http://vivo.ufl.edu/individual/n5531874911;http://vivo.ufl.edu/individual/n7384045581>

incorrect_names = set()
line_count = 0
for s, p, o in map(parse_line, get_data()):
    line_count += 1
    if line_count % 100000 == 0:
        print(line_count, '/', NUM_LINES, len(incorrect_names))

    for name in [s, o]:
        if name.startswith("<http://vivo.ufl.edu/individual/") and not is_individual(name):
            incorrect_names.add(name)
    
print(len(incorrect_names))
# 1694
dump_obj('incorrect_names.pkl', list(incorrect_names))