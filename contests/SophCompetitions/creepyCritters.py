#CSCC 2023

#UNION FIND -DISJOINT SETS
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
    
    def getRank(self):
        return self.rank
    
    def getP(self):
        return self.p

for i in range(int(input())):
    N = int(input())
    ufds = UFDS(N)
    tJar, tMG, d1,d2 = [],[], {},{}
    
    for j in range(N):
        mg, jar = map(int, input().split())
        tMG.append(mg)
        tJar.append(jar)
    M = int(input())
    
    for x in range(M):
        k1, k2 = map(int, input().split())
        ufds.union(k1, k2)
    rank, p = ufds.getRank(), ufds.getP()
    
    for h in range(N):
        temp = ufds.find_set(h)
        if temp not in d1:
            d1[temp] = 0
        if temp not in d2:
            d2[temp] = 0
        d1[p[h]] += tJar[h]
        d2[p[h]] += tMG[h]
    
    if sum(d1.values()) != N * 5 or sum(d2.values()) != N:
        print("Case #" + str(i+1) + ": no")
    else:
        valid = True
        for key in d1.keys():
            if d1[key] != d2[key] * 5:
                valid = False
                break
        if valid:
            print("Case #" + str(i+1) + ": yes")
        else:
            print("Case #" + str(i+1) + ": no")