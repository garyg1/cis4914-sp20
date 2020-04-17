def get_lines(f):
    line = f.readline()
    while line:
        yield line
        line = f.readline()


def get_data():
    return get_lines(open('data/content.nq', 'r'))


def parse_line(line):
    subjectEnd = line.find(' ')
    predicateEnd = line.find(' ', subjectEnd + 1)
    objectEnd = line.find(' ', predicateEnd + 1)

    subject = line[ : subjectEnd]
    predicate = line[subjectEnd + 1 : predicateEnd]
    object = line[predicateEnd + 1 : objectEnd]

    return subject, predicate, object
