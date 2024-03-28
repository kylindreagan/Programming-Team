import itertools

def subcategories(s, subd):
    for i in s:
        if i not in subd.keys():
            subd[i] = 0
        subd[i] += 1
    return subd

def validSubset(s,S):
    subd = {}
    x=[j for i in s for j in i]
    for a in S:
        subd[a] = x.count(a)
    for h in subd.keys():
        if subd[h]/k > 1/2:
            return False
    return True

n, k = map(int, input().split())
probSep, probComb = set(), [None for x in range(n)]
for i in range(n):
    t, *p = map(str, input().split())
    probComb[i] = p
    probSep.update(p)

subsets = list(itertools.combinations(probComb, k))
final= [x for x in subsets if validSubset(x, probSep)]
print(len(final))
