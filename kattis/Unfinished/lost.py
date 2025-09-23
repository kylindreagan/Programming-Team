import heapq
from collections import defaultdict

def TransBFS(graph, start, mem):
    min_cost = float('inf')
    min_steps = float('inf')
    #steps, cost, language
    pq = [(0, 0, start)]
    while pq:
        steps, cost, language = heapq.heappop(pq)
        for neighbor, neighcost in graph[language]:
            next_cost = cost
            if neighbor not in mem or neighbor == "English":
               next_cost += neighcost
            if steps < min_steps or (steps == min_steps and next_cost < min_cost):
                    if neighbor == "English":
                        min_steps = steps
                        if min_steps == steps:
                            min_cost = min(min_cost, next_cost)
                        else:
                            min_cost = cost
                    else:
                         heapq.heappush(pq, (steps + 1, next_cost, neighbor))
    
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
        curr_cost = TransBFS(graph, start, starts)
     if curr_cost == float('inf'):
          print("Impossible")
          quit()
     total_cost += curr_cost

print(total_cost)