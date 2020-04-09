import pickle

with open('types.pkl', 'rb') as infile:
    types = pickle.load(infile)

types2 = dict()
types2[None] = 0
for key in types:
    if key[:2] == '_:':
        types2[None] += 1
    else:
        types2[key] = types[key]

with open('types2.pkl', 'wb') as outfile:
    pickle.dump(dict(types2), outfile)

with open('types.csv', 'w') as outfile:
    data = []
    for key in types2:
        val = types2[key]
        data.append((val, key))
    
    data.sort()
    data.reverse()
    for (val, key) in data:
        outfile.write(str(key))
        outfile.write(',')
        outfile.write(str(val))
        outfile.write('\n')