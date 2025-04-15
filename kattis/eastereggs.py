from math import dist, hypot

def match(curr, adj, l, r, vis):
    if vis[curr]:
        return False
    vis[curr] = True

    for next in adj[curr]:
        if r[next] == -1 or match(r[next], adj, l, r, vis):
            l[curr] = next
            r[next] = curr
            return True
    return False


def bipartite(adj, n, m):
    l = [-1] * n
    r = [-1] * m
    vis = [False] * n

    works = True
    while works:
        works = False
        vis = [False] * n
        for i in range(n):
            if l[i] == -1:
                works |= match(i, adj, l, r, vis)

    ret = sum(1 for i in range(n) if l[i] != -1)
    return ret

def can_higher(d, p1, p2, k, n, m):
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if dist(p1[i], p2[j]) < d:
                graph[i].append(j)
    b = bipartite(graph, n, m)
    return n + m - b >= k

def MinMaxDist(p1, p2, k, n, m):
    low = 0
    high = max(hypot(x1 - x2, y1 - y2) for x1, y1 in p1 for x2, y2 in p2)
    eps = 1e-6
    while high-low >= eps:
        mid = (low + high) / 2
        if can_higher(mid, p1, p2, k, n, m):
            low = mid
        else:
            high = mid
    return low

eggs, blue, red = map(int, input().split())
blue_plants = [tuple(map(float, input().split())) for _ in range(blue)]
red_plants = [tuple(map(float, input().split())) for _ in range(red)]

print(MinMaxDist(blue_plants, red_plants, eggs, blue, red))