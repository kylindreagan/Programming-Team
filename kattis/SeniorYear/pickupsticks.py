from collections import deque

def topo_stick(adj, n):
    indeg = [0] * n
    for u in range(n):
        for v in adj[u]:
            indeg[v] += 1

    q = deque([i for i in range(n) if indeg[i] == 0])
    order = []

    while q:
        u = q.popleft()
        order.append(u + 1)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    if len(order) == n:
        return order
    return False


n, m = map(int, input().split())
stick_count = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    stick_count[a-1].append(b-1)
x = topo_stick(stick_count, n)
if not x:
    print("IMPOSSIBLE")
else:
    for s in x:
        print(s)