#Problem: https://open.kattis.com/problems/kitten

from queue import Queue

kitten = int(input())

def bfs(p, end):
        visited = dict()
        g = [x for x in graph.keys()]
        for m in range(n-1):
            visited[g[m]] = False
        q = Queue()
        L = [[p]]
        visited[p] = True
        q.put(p)
        while not q.empty():
            x = q.get()
            l = []
            for neighbor in graph[x]:
                if neighbor == end:
                    L.append(neighbor)
                    return L
                if visited[neighbor] == False:
                    visited[neighbor] = True
                    q.put(neighbor)
                    l.append(neighbor)
            if len(l) != 0:
                L.append(l)

def skimmer(l):
    x = -1
    y = 0
    L = [l[x]]
    l.pop(x)
    
    while True:
        try:
            change = False
            if l[x] == l[0]:
                L.append(l[0][0])
                return L
            for i in graph[L[y]]:
                if i in l[x]:
                    L.append(i)
                    x -= 1
                    y += 1
                    change = True
            if not change:
                x -= 1
        except IndexError:
            x += 1
            l[x].pop(L[y])
            L.pop(y)
            y -= 1

graph = dict()
ground = -1

while True:
    branch = input().split()
    x = [int(j) for j in branch]
    y = [int(b) for b in x]
    y.pop(0)
    if ground == -1:
        ground = x[0]
    if -1 in x:
        break
    elif x[0] not in graph:
        graph[x[0]] = set(y)
    else:
        for i in range(len(y)):
            graph[x[0]].add(y[i])
    for j in y:
        if j not in graph:
            graph[j] = set()
        graph[j].add(x[0])

n = len(graph)+1
q = bfs(kitten, ground)
l = skimmer(q)
l.reverse()

for k in l:
    print(k, end=" ")