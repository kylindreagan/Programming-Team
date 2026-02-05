import sys

class UFDS:
    def __init__(self, N):
        self.parent = list(range(N))
        self.rank = [0] * N
        self.next = list(range(1, N + 1))
        self.head = list(range(N))
        self.tail = list(range(N)) 
    
    def find_set(self, i):
        while self.parent[i] != i:
            self.parent[i] = self.parent[self.parent[i]] 
            i = self.parent[i]
        return i
    
    def union(self, i, j):
        if i == j:
            return
        
        x, y = self.find_set(i), self.find_set(j)
        if x == y:
            return
        
        self.parent[y] = x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1
        
        self.next[self.tail[x]] = self.head[y]
        self.tail[x] = self.tail[y]
        self.head[y] = -1  
        self.tail[y] = -1
    
    def balkanize(self, x):
        root = self.find_set(x)
        members = []
        
        if self.head[root] != -1:
            current = self.head[root]
            while True:
                members.append(current)
                if current == self.tail[root]:
                    break
                current = self.next[current]
        
        for u in members:
            self.parent[u] = u
            self.rank[u] = 0
            self.head[u] = u
            self.tail[u] = u
            self.next[u] = u + 1 if u + 1 < len(self.parent) else -1
        
        if x == root:
            self.parent[x] = x
            self.rank[x] = 0
            self.head[x] = x
            self.tail[x] = x
            self.next[x] = x + 1 if x + 1 < len(self.parent) else -1
        
        return members
    
    def get_ruler(self, i):
        return self.find_set(i) + 1

def main():
    data = sys.stdin.buffer.read().split()
    
    idx = 0
    n, q = int(data[idx]), int(data[idx+1])
    idx += 2
    
    ufds = UFDS(n)
    results = []
    
    for _ in range(q):
        cmd = data[idx].decode()
        idx += 1
        
        if cmd == 'a':
            x = int(data[idx]) - 1
            y = int(data[idx+1]) - 1
            idx += 2
            ufds.union(x, y)
            
        elif cmd == 'b':
            x = int(data[idx]) - 1
            idx += 1
            ufds.balkanize(x)
            
        else:
            x = int(data[idx]) - 1
            idx += 1
            results.append(str(ufds.get_ruler(x)))
    
    sys.stdout.write("\n".join(results))

if __name__ == "__main__":
    main()