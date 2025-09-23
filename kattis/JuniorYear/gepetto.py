from itertools import combinations

def validPizza(s, subs):
    return  all((s & i) != i for i in subs)

n, m = map(int, input().split())
#each 'set' is represented as an integer where each bit corresponds to an element in the set.
forbidden = [sum(1 << (x - 1) for x in map(int, input().split())) for _ in range(m)]

final = [comb for x in range(1, n + 1) for comb in combinations(range(1, n + 1), x) if validPizza(sum(1 << (y - 1) for y in comb), forbidden)]

print(len(final)+1)