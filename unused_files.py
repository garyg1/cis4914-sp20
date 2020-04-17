from utils import dump_obj, get_obj, histogram
from parse import get_lines, parse_line, get_data
from rdf import TYPE_FILE, is_individual

uritype = get_obj('saved/uri_to_type.pkl')

files = filter(lambda uri: TYPE_FILE in uritype[uri], uritype)

print(len(files))
# 7113
unused_files = set(files)
for s, p, o in map(parse_line, get_data()):
    if not is_individual(s) or not is_individual(o): continue
    if s in unused_files: unused_files.remove(s)
    if o in unused_files: unused_files.remove(o)

print(unused_files)
# {'<http://vivo.ufl.edu/individual/n81500>'}