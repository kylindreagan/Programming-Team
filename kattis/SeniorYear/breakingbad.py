from collections import deque

def isBipartite(V, adj):
    color = [-1] * V  
    
    for i in range(V):
        if color[i] == -1:
            color[i] = 0
            q = deque([i])

            while q:
                u = q.popleft()

                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        q.append(v)
                    elif color[v] == color[u]:
                        return color, False
    
    return color, True 


n = int(input())
buy_dic = {input():i for i in range(n)}
adj = [[] for _ in range(n)]

for i in range(int(input())):
    x, y = input().split()
    adj[buy_dic[x]].append(buy_dic[y])
    adj[buy_dic[y]].append(buy_dic[x])

color, isBi = isBipartite(n, adj)

if not isBi:
    print("impossible")
else:
    Walt, Jesse = [x for x in buy_dic.keys() if color[buy_dic[x]] == 0], [x for x in buy_dic.keys() if color[buy_dic[x]] == 1]
    print(" ".join(Walt))
    print(" ".join(Jesse))