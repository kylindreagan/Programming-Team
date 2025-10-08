def dfsList(node,graph,visited): 
    if visited[node] == False: 
        visited[node] = True  
        for neighbor in graph[node]:
            dfsList(neighbor,graph,visited) 

while True:
    valid = True
    p, c = map(int, input().split())
    if p == c == 0:
        break
    graph = []
    for i in range(c): 
        x,y = map(int, input().split())
        graph.append([x,y])
    visiCheck = [True for _ in range(p)]
    for j in range(c):
        visited = [False for _ in range(p)]
        adjList = {i:set() for i in range(p)}
        for h in range(c):
            if h != j:
                x,y = graph[h][0], graph[h][1]
                adjList[x].add(y) 
                adjList[y].add(x)
        dfsList(0,adjList,visited)
        if visiCheck != visited:
            print("Yes")
            valid = False
            break
    if valid:
        print("No")