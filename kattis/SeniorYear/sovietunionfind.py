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
        
        tail_x = self.tail[x]
        head_y = self.head[y]
        
        self.next[tail_x] = head_y
        self.tail[x] = self.tail[y]
        self.head[y] = -1
        self.tail[y] = -1
    
    def balkanize(self, x):
        root = self.find_set(x)
        
        if self.head[root] == root and self.tail[root] == root:
            return [x] if x == root else []
        
        members = []
        current = self.head[root]
        tail = self.tail[root]
        
        while True:
            members.append(current)
            if current == tail:
                break
            current = self.next[current]
        
        parent = self.parent
        head = self.head
        tail_arr = self.tail
        next_arr = self.next
        n = len(parent)
        
        for u in members:
            parent[u] = u
            head[u] = u
            tail_arr[u] = u
            next_arr[u] = u + 1 if u + 1 < n else -1
        
        if x == root:
            parent[x] = x
            head[x] = x
            tail_arr[x] = x
            next_arr[x] = x + 1 if x + 1 < n else -1
        
        return members

def main():
    data = sys.stdin.buffer.read().split()
    
    idx = 0
    n, q = int(data[idx]), int(data[idx+1])
    idx += 2
    
    ufds = UFDS(n)
    results = []
    results_append = results.append
    for _ in range(q):
        cmd = data[idx]
        idx += 1
        
        if cmd[0] == 97:  # 'a' = 97 in ASCII
            x = int(data[idx]) - 1
            y = int(data[idx+1]) - 1
            idx += 2
            ufds.union(x, y)
            
        elif cmd[0] == 98:  # 'b' = 98 in ASCII
            x = int(data[idx]) - 1
            idx += 1
            ufds.balkanize(x)
            
        else:
            x = int(data[idx]) - 1
            idx += 1
            results_append(str(ufds.get_ruler(x)))
    
    sys.stdout.write("\n".join(results))

if __name__ == "__main__":
    main()