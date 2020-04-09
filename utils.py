import pickle


def dump_obj(name, obj):
    with open(name, 'wb') as outfile:
        pickle.dump(obj, outfile)


def get_obj(name):
    with open(name, 'rb') as infile:
        return pickle.load(infile)
