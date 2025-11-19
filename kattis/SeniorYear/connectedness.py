import sys
sys.setrecursionlimit(3000000)
input = sys.stdin.readline

class UFDS:
    def __init__(self, n):
        self.p = list(range(n))
        self.rank = [0] * n
        self.num_sets = n

    def find_set(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]   # path halving
            x = self.p[x]
        return x

    def union(self, a, b):
        x = self.find_set(a)
        y = self.find_set(b)
        if x == y:
            return False
        self.num_sets -= 1

        if self.rank[x] < self.rank[y]:
            x, y = y, x
        self.p[y] = x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1
        return True


import sys
input = sys.stdin.readline

v, e = map(int, input().split())
if e < v - 1:
    print(-1)
elif v == 1:
    print(0)
else:
    uf = UFDS(v)
    for i in range(1, e+1):
        a, b = map(int, input().split())
        uf.union(a-1, b-1)
        if uf.num_sets == 1:
            print(i)
            break
    else:
        print(-1)