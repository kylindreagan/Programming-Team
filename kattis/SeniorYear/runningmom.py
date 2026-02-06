from collections import defaultdict

graph = defaultdict(set)
n = int(input())

for _ in range(n):
    city1, city2 = input().strip().split()
    graph[city1].add(city2)
    graph[city2]

def has_cycle(city, visited, recstack, memo):
    if city in memo:
        return memo[city]
    
    visited.add(city)
    recstack.add(city)
    
    for neighbor in graph[city]:
        if neighbor not in visited:
            if has_cycle(neighbor, visited, recstack, memo):
                memo[city] = True
                return True
        elif neighbor in recstack:
            memo[city] = True
            return True
    
    recstack.remove(city)
    memo[city] = False
    return False

import sys
for line in sys.stdin:
    city = line.strip()
    if not city:
        break
    visited = set()
    recstack = set()
    memo = {}
    if has_cycle(city, visited, recstack, memo):
        print(city, 'safe')
    else:
        print(city, 'trapped')