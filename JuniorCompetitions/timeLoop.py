from queue import Queue

def time_search(graph, start):
    visited = set()
    q = Queue()
    q.put(start)
    while not q.empty():
        curr = q.get()
        for j in graph[curr]:
            if j in visited:
                return True, visited
            visited.add(j)
            q.put(j)
    return False, visited

answers = []
for _ in range(int(input())):
    towns, paths = map(int, input().split())
    town_dict = {(i+1):set() for i in range(towns)}
    for path in range(paths):
        u, v = map(int, input().split())
        town_dict[u].add(v)
    loopexists = False
    visited = set()
    for val in range(1,towns+1):
       for key in range(1,towns+1):
           if val not in town_dict[key]: continue
           for subval in town_dict[val]:
               town_dict[key].add(subval)
    for town in range(1,towns+1):
        if town in town_dict[town]:
            loopexists = True
            break
    answers.append("YES" if loopexists else "NO")

print(answers)