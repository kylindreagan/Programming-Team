from queue import Queue

def Tree_BFS(start, end, tree):
    
    path = start[0]
    visited = set()
    visited.add(start)
    q = Queue()
    q.put((tree[start], path))
    while not q.empty():
        current = q.get()
        next, curr_path = current
        for neighbor in next:
            if neighbor == end:
                return curr_path + end[0]
            if neighbor not in visited:
                q.put((tree[neighbor], curr_path + neighbor[0]))
                visited.add(neighbor)
        

first_case = True
for _ in range(int(input())):
    if not first_case:
        print()
    first_case = False
    input()
    num_roads, routes = map(int, input().split())
    roads = {}
    
    for i in range(num_roads):
        a, b = input().split()
        if a not in roads:
            roads[a] = set()
        roads[a].add(b)
        if b not in roads:
            roads[b] = set()
        roads[b].add(a)
    
    results = [None for _ in range(routes)]
    for j in range(routes):
        start, end = input().split()
        results[j] = Tree_BFS(start, end, roads)
    print("\n".join(results))