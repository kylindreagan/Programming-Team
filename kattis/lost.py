import heapq
from collections import defaultdict

def TransBFS(graph, start):
    min_cost = float('inf')
    min_steps = float('inf')
    visited = set()
    #cost, steps, language
    pq = [(0, 0, start)]
    while pq:
        cost, steps, language = heapq.heappop(pq)
        for neighbor, distance in graph[language]:
            if neighbor in starts:
                next_cost = cost + distance
            else:
                 next_cost = cost
            if steps + 1 < min_steps or (steps + 1 == min_steps and next_cost < min_cost):
                    if neighbor == "English":
                        min_steps = steps
                        min_cost = next_cost
                    else:
                         heapq.heappush(pq, (next_cost, steps + 1, neighbor))
    
    return min_cost

n, m = map(int, input().split())
starts = [x for x in input().split()]
graph = defaultdict(list)
for i in range(m):
     lan1, lan2, cost = input().split()
     graph[lan1].append((lan2, int(cost)))
     graph[lan2].append((lan1, int(cost)))

total_cost = 0
for start in starts:
     if start == "English":
          curr_cost = 0
     else:
        curr_cost = TransBFS(graph, start)
     if curr_cost == float('inf'):
          print("Impossible")
          quit()
     total_cost += curr_cost

print(total_cost)