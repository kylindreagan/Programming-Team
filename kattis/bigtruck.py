import heapq

def Truck_BFS(end, graph, items):
    sols = []
    min_d = float('inf')
    pq = [(0, 1, items[0])]
    # Dictionary to track the minimum distance to each city
    best_path = {i: (float('inf'), 0) for i in graph}
    best_path[1] = (0, items[0])
    # Keep track of the best items collected at each city with a given distance
    while pq:
        curr_path, city, curr_items = heapq.heappop(pq)
        for neighbor, distance in graph[city]:    
            next_path = curr_path + distance
            next_items = curr_items + items[neighbor-1]
            best_distance, best_collected = best_path[neighbor]
            if next_path <= min_d:
                if neighbor == end:
                    if next_path < min_d:
                        min_d = min(min_d, next_path)
                        sols = []
                    sols.append((next_path, next_items))
                if next_path <  best_distance or (next_path == best_distance and next_items > best_collected):
                    heapq.heappush(pq, (next_path, neighbor, next_items))
                    best_path[neighbor] = (next_path, next_items)
    if sols:
        return max(sols, key=lambda x: x[1])
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

path = Truck_BFS(locations, graph, items)
if path == None:
    print("impossible")
else:
    print(path[0], path[1])