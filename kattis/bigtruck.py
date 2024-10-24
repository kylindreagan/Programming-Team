import heapq
def Truck_BFS(start, end, graph, items):
    sols = []
    min_d = float('inf')
    pq = [(start, 0, items[0])]
    # Dictionary to track the minimum distance to each city
    best_path = {i: float('inf') for i in graph}
    best_path[start] = 0
    # Keep track of the best items collected at each city with a given distance
    best_items = {i: 0 for i in graph}
    best_items[start] = items[0]
    while pq:
        city, curr_path, curr_items = heapq.heappop(pq)
        
        for neighbor, distance in graph[city]:    
            next_path = curr_path + distance
            next_items = curr_items + items[neighbor-1]
            if next_path <= min_d:
                if neighbor == end:
                    if next_path < min_d:
                        min_d = min(min_d, next_path)
                        sols = []
                    sols.append((next_path, next_items))
                if next_path < best_path[neighbor] or (next_path == best_path[neighbor] and next_items > best_items[neighbor]):
                    heapq.heappush(pq, (neighbor, next_path, next_items))
                    best_items[city] = next_items
                    best_path[city] = next_path
    
    if sols:
        return sorted(sols, key=lambda x: x[1], reverse=True)[0]
    else:
        return None

locations = int(input())
items = [int(x) for x in input().split()]

num_roads = int(input())

graph = {i: set() for i in range(1,locations+1)}

for i in range(num_roads):
    a, b, d = map(int, input().split())
    graph[a].add((b,d))
    graph[b].add((a,d))

path = Truck_BFS(1, locations, graph, items)
if path == None:
    print("impossible")
else:
    print(path[0], path[1])