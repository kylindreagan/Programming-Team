from itertools import*
from functools import partial

def generateDupes(l):
    d = {}
    for i in l:
        x = partial(l, i)
        if len(x) > 1:
            d[i] = x
    return d

def indices(lst, item): 
    return [i for i, x in enumerate(lst) if x == item]

def validCombinations(strs, c):
    result = []
    for combo in combinations(strs, 3):
        if combo[0][c] == combo[1][c] == combo[2][c] or  combo[0][c] != combo[1][c] and combo[1][c] != combo[2][c] and combo[0][c] != combo[2][c]:
            result.append(combo)
    return result


cardLayout = []
n = 1
d = {}
for i in range(4):
    l = input().split()
    cardLayout += l
    for j in l:
        d[j] = n
        n += 1

dupeDict = None
m = len(set(cardLayout))
if m < 3:
    keyPrefinal = [frozenset(Y) for Y in combinations(range(1,n-m+1), 3)]
    keyFinal = [list(t) for t in keyPrefinal]
    for X in keyFinal:
        X.sort(key=lambda x:x)
    
    for X2 in keyFinal:
        strKeys = [str(Y) for Y in X2]
        if len(set(strKeys)) == 3:
            print(" ".join(strKeys))
    quit()

elif m != 12:
    dupeDict = dict((x, [bern+1 for bern in indices(cardLayout, x)]) for x in set(cardLayout) if cardLayout.count(x) > 1)

c1 = validCombinations(cardLayout,0)
c2 = validCombinations(cardLayout,1)
c3 = validCombinations(cardLayout,2)
c4 = validCombinations(cardLayout,3)

final = list(set.intersection(*map(set, [c1, c2, c3, c4])))

if len(final) == 0:
    print("no sets")
    quit()

keyPrefinal = []
for b in final:
    l = [d[q] for q in b]
    keyPrefinal.append(l)


if dupeDict != None:
    for val in dupeDict.values():
        if len(val) >= 3:
            selfsets = set(comb for comb in combinations(val, 3))
            for somanyfuckingvariables in selfsets:
                keyPrefinal.append(list(somanyfuckingvariables))
        inKeys = val.pop(-1)
        replace = [x1 for x1 in keyPrefinal if inKeys in x1]
        for pi in replace:
            for new in range(len(val)):
                thiscodesucks = list(map(lambda x: str(x).replace(str(inKeys), str(val[new])), pi))
                theta = [int(x) for x in thiscodesucks]
                keyPrefinal.append(theta)



keyFinals = set(frozenset(inner_list) for inner_list in keyPrefinal)
keyFinal = [list(t) for t in keyFinals]
for X in keyFinal:
    X.sort(key=lambda x:x)

keyFinal.sort(key=lambda x:x)
for X2 in keyFinal:
    strKeys = [str(Y) for Y in X2]
    if len(set(strKeys)) == 3:
        print(" ".join(strKeys))