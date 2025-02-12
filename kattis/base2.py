import heapq

def TransBFS(graph, start):
    min_cost = -1
    min_steps = float('inf')
    #cost, steps, language
    pq = [(0, 0,  start)]
    visited = set()
    while pq:
        cost, steps, language = heapq.heappop(pq)
        for neighbor, distance in graph[language]:    
            next_steps = steps + distance
            if steps <= min_steps:
                    if neighbor == "English":
                        min_steps = steps
                        if min_steps == steps:
                            min_cost = min(min_cost, cost)
                        else:
                            min_cost = cost
                    else:
                         pq.heappush()

    
