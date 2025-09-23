#UNION-FIND DISJOINT SETS (found on internet)
class UFDS:
    def __init__(self, N):
        self.p = [i for i in range(N)]
        self.rank = [0 for _ in range(N)]
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

def dino_dist(n, samples):
    adj_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            s1, s2 = samples[i], samples[j]
            d = sum(c1 != c2 for c1, c2 in zip(s1, s2)) if len(s1) == len(s2) else -1
            adj_matrix[i][j] = adj_matrix[j][i] = d
    
    return adj_matrix

def FW_minimax(n, D):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                D[i][j] = min(D[i][j], max(D[i][k], D[k][j]))
    
    return sum(D[0])

n, k = map(int, input().split())
UF = UFDS(n)
samples = [input() for _ in range(n)]

D = dino_dist(n,samples)
print(D)
indices = []

total = FW_minimax(n, D)
print(total)