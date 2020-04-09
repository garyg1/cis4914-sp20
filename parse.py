def get_lines(f):
    line = f.readline()
    while line:
        yield line
        line = f.readline()


def get_data():
    return get_lines(open('data/content.nq', 'r'))


def parse_line(line):
    line = ' '.join(line.split(' ')[:-2])
    subjectEnd = line.find(' ')
    predicateEnd = line.find(' ', subjectEnd + 1)

    subject = line[:subjectEnd]
    predicate = line[subjectEnd + 1: predicateEnd]
    object = line[predicateEnd + 1:]

    # if (subject[:2] == '_:'):
    #     subject = None
    # if (predicate[:2] == '_:'):
    #     predicate = None
    # if (object[:2] == '_:'):
    #     object = None

    return subject, predicate, object
