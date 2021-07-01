dct = {'uno':'dos','tres':'uno', 'dos': 'tres'}
v= dct ['tres']

for k in range (len(dct)):
    v = dct[v]

print(v)
