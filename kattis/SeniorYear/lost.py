import heapq
from collections import defaultdict
from math import inf

def main():
    n, m = map(int, input().split())
    target_languages = input().split()
    
    graph = defaultdict(list)
    for _ in range(m):
        l1, l2, c = input().split()
        cost = int(c)
        graph[l1].append((l2, cost))
        graph[l2].append((l1, cost))
    
    all_languages = set(target_languages) | {"English"}
    
    min_steps = {lang: inf for lang in all_languages}
    min_steps["English"] = 0
    
    queue = ["English"]
    step = 0
    while queue:
        next_queue = []
        step += 1
        for lang in queue:
            for neighbor, _ in graph[lang]:
                if min_steps[neighbor] == inf:
                    min_steps[neighbor] = step
                    next_queue.append(neighbor)
        queue = next_queue
    
    max_steps = 0
    for lang in target_languages:
        if min_steps[lang] == inf:
            print("Impossible")
            return
        max_steps = max(max_steps, min_steps[lang])
    
    dist = {lang: inf for lang in all_languages}
    dist["English"] = 0
    pq = [(0, 0, "English")]
    
    used_edges = set()
    
    while pq:
        cost, steps, lang = heapq.heappop(pq)
        
        if cost > dist[lang] or steps > max_steps:
            continue
            
        for neighbor, edge_cost in graph[lang]:
            next_steps = steps + 1
            next_cost = cost + edge_cost
            
            # Only consider if within step limit and we found a better cost
            if next_steps <= max_steps and next_cost < dist[neighbor]:
                dist[neighbor] = next_cost
                heapq.heappush(pq, (next_cost, next_steps, neighbor))
    
    total_cost = 0
    visited = {"English"}
    
    for distance in range(1, max_steps + 1):
        nodes_at_distance = [lang for lang in target_languages + ["English"] 
                           if min_steps[lang] == distance]
        
        for node in nodes_at_distance:
            if node in visited:
                continue
                
            min_edge_cost = inf
            for neighbor, edge_cost in graph[node]:
                if neighbor in visited and min_steps[neighbor] == distance - 1:
                    min_edge_cost = min(min_edge_cost, edge_cost)
            
            if min_edge_cost == inf:
                print("Impossible")
                return
                
            total_cost += min_edge_cost
            visited.add(node)
    
    print(total_cost)

if __name__ == "__main__":
    main()