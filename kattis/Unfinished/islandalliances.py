from collections import defaultdict

class UFDS:
    def __init__(self, N):
        self.p = [i for i in range(N)]
        self.rank = [0 for _ in range(N)]
        self.visited = [False for _ in range(N)]
        self.num_sets = N

    def find_set(self, i):
        if self.p[i] == i: return i
        self.p[i] = self.find_set(self.p[i])
        return self.p[i]

    def is_same_set(self, i, j):
        return self.find_set(i) == self.find_set(j)

    def union(self, i, j):
        if not self.is_same_set(i, j):
            self.num_sets -= 1
            x, y = self.find_set(i), self.find_set(j)
            if self.rank[x] > self.rank[y]:
                self.p[y] = x
            else:
                self.p[x] = y
                if self.rank[x] == self.rank[y]:
                    self.rank[y] += 1

n,m,q = map(int, input().split())
enemies = defaultdict(set)
ufds = UFDS(n+1)

for i in range(m):
    u, v = map(int, input().split())
    enemies[u].add(v)
    enemies[v].add(u)

for j in range(q):
    a,b = map(int, input().split())
    A,B = ufds.find_set(a), ufds.find_set(b)
    approved = 1
    for ca in enemies[A]:
        if ufds.is_same_set(ca, B):
            print("REFUSE")
            approved = 0
            break
    for cb in enemies[B]:
        if not approved:
            break
        if ufds.is_same_set(cb, A):
            print("REFUSE")
            approved = 0
            break
    if approved:
        print("APPROVE")
        ufds.union(A,B)
        enemies[A].union(enemies[B])
        enemies[B].union(enemies[A])