import sys
input = sys.stdin.readline

n, k = map(int, input().split())
perms = [input().strip() for _ in range(n)]

order0 = perms[0]
id_map = {c: i for i, c in enumerate(order0)}
pos = [ [0]*k for _ in range(n) ]

for p in range(n):
    for idx, c in enumerate(perms[p]):
        pos[p][id_map[c]] = idx

# Build DAG adjacency using consistency check
adj = [[] for _ in range(k)]
indeg = [0]*k

for i in range(k):
    for j in range(k):
        if i == j:
            continue
        ok = True
        for p in range(n):
            if pos[p][i] > pos[p][j]:
                ok = False
                break

        if ok:
            adj[i].append(j)
            indeg[j] += 1

# Longest path in DAG (topo DP)
from collections import deque

dp = [1]*k
q = deque()

for i in range(k):
    if indeg[i] == 0:
        q.append(i)

while q:
    u = q.popleft()
    for v in adj[u]:
        if dp[v] < dp[u] + 1:
            dp[v] = dp[u] + 1
        indeg[v] -= 1
        if indeg[v] == 0:
            q.append(v)

print(max(dp))