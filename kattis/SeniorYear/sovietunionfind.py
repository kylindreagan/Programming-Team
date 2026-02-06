import sys

class UFDS:
    __slots__ = ('parent', 'next', 'head', 'tail')  # Memory and access optimization
    
    def __init__(self, N):
        self.parent = list(range(N))
        self.next = list(range(1, N + 1))
        self.head = list(range(N))
        self.tail = list(range(N))
    
    def find_set(self, i):
        parent = self.parent
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    
    def union(self, i, j):
        if i == j:
            return
        
        x = self.find_set(i)
        y = self.find_set(j)
        if x == y:
            return
        
        self.parent[y] = x
        
        self.next[self.tail[x]] = self.head[y]
        self.tail[x] = self.tail[y]
        self.head[y] = -1
        self.tail[y] = -1
    
    def balkanize(self, x):
        root = self.find_set(x)
        h = self.head[root]
        if self.head[root] == root and self.tail[root] == root:
            return [x] if x == root else []
        
        members = []
        curr = h
        tail = self.tail[root]
        while True:
            members.append(curr)
            if curr == tail:
                break
            curr = self.next[curr]
        
        parent, head, tail_arr, next_arr, n = self.parent, self.head, self.tail, self.next, len(self.parent)
        for u in members:
            parent[u] = head[u] = tail_arr[u] = u
            next_arr[u] = u + 1 if u + 1 < n else -1
        
        if x == root:
            parent[x] = head[x] = tail_arr[x] = x
            tail_arr[x] = x
            next_arr[x] = x + 1 if x + 1 < n else -1
        
        return members

def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    
    n = int(next(it))
    q = int(next(it))
    
    ufds = UFDS(n)
    results = []
    results_append = results.append
    for _ in range(q):
        cmd = next(it)
        b = cmd[0]
        
        if b == 97:  # 'a' = 97 in ASCII
            x = int(next(it)) - 1
            y = int(next(it)) - 1
            ufds.union(x, y)
            
        elif b == 98:  # 'b' = 98 in ASCII
            x = int(next(it)) - 1
            ufds.balkanize(x)
            
        else:
            x = int(next(it)) - 1
            results_append(str(ufds.find_set(x) + 1))
    
    sys.stdout.write("\n".join(results))

if __name__ == "__main__":
    main()