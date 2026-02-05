import sys
sys.setrecursionlimit(300000)

class UFDS:
    def __init__(self, N):
        self.p = [i for i in range(N)]
        self.rank = [0 for _ in range(N)]
        self.ruler = [i for i in range(N)] 
    
    def find_set(self, i):
        if self.p[i] == i:
            return i
        self.p[i] = self.find_set(self.p[i])
        return self.p[i]
    
    def is_same_set(self, i, j):
        return self.find_set(i) == self.find_set(j)
    
    def union(self, i, j):
        if self.is_same_set(i, j):
            return
            
        x, y = self.find_set(i), self.find_set(j)
        ruler_i = self.ruler[x]
        
        if self.rank[x] > self.rank[y]:
            self.p[y] = x
            self.ruler[x] = ruler_i
        else:
            self.p[x] = y
            self.ruler[y] = ruler_i
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1
    
    def balkanize(self, i):
        root = self.find_set(i)
        
        members = []
        for j in range(len(self.p)):
            if self.find_set(j) == root:
                members.append(j)
        
        for member in members:
            self.p[member] = member
            self.rank[member] = 0
            self.ruler[member] = member
    
    def get_ruler(self, i):
        root = self.find_set(i)
        return self.ruler[root] + 1

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n, q = int(data[idx]), int(data[idx+1])
    idx += 2
    
    ufds = UFDS(n)
    results = []
    
    for _ in range(q):
        query_type = data[idx]
        idx += 1
        
        if query_type == 'a':
            x = int(data[idx]) - 1
            y = int(data[idx+1]) - 1
            idx += 2
            ufds.union(x, y)
            
        elif query_type == 'b':
            x = int(data[idx]) - 1
            idx += 1
            ufds.balkanize(x)
            
        elif query_type == 'c':
            x = int(data[idx]) - 1
            idx += 1
            results.append(str(ufds.get_ruler(x)))
    
    print("\n".join(results))

if __name__ == "__main__":
    main()