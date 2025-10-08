#Assistance from https://www.geeksforgeeks.org/dsa/tarjan-algorithm-find-strongly-connected-components/
"""def tarjandfs(u, parent):
    visited[u] = True
    disc[u] = low[u] = time[0]
    time[0] += 1

    for v in graph[u]:
        if not visited[v]:
            tarjandfs(v, u)
            low[u] = min(low[u], low[v])

            # bridge condition
            if low[v] > disc[u]:
                bridges.append((u, v))
        elif v != parent:
            low[u] = min(low[u], disc[v])

while True:
    p, c = map(int, input().split())
    if p == 0 and c == 0:
        break

    graph = [[] for _ in range(p)]
    for _ in range(c):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False]*p
    disc = [float('inf')]*p
    low = [float('inf')]*p
    time = [0]
    bridges = []

    for i in range(p):
        if not visited[i]:
            tarjandfs(i, -1)
    if bridges:
        print("Yes")
    else:
        print("No")"""

import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def solve():
    while True:
        p, c = map(int, input().split())
        if p == 0 and c == 0:
            break

        graph = [[] for _ in range(p)]
        for _ in range(c):
            a, b = map(int, input().split())
            graph[a].append(b)
            graph[b].append(a)

        visited = [False] * p
        disc = [0] * p
        low = [0] * p
        time = 0
        found = False

        def dfs(u, parent):
            nonlocal time, found
            visited[u] = True
            disc[u] = low[u] = time
            time += 1

            for v in graph[u]:
                if found: return  # early exit
                if not visited[v]:
                    dfs(v, u)
                    low[u] = min(low[u], low[v])
                    if low[v] > disc[u]:
                        found = True
                        return
                elif v != parent:
                    low[u] = min(low[u], disc[v])

        for i in range(p):
            if not visited[i]:
                dfs(i, -1)
                if found:
                    break

        print("Yes" if found else "No")

solve()