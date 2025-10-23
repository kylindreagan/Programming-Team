from collections import deque

r,c,n = map(int, input().split())
weak_points = deque(tuple(int(x) for x in input().split()) for _ in range(n))
until_next = n
visited = set(weak_points)
counter = 1
if len(visited) == r * c:
    print(counter)

else:
    temp = 0
    while weak_points:
        x,y = weak_points.popleft()

        for v,h in [(1,0),(-1,0),(0,1),(0,-1)]:
            if 0<x+v<=r and 0<y+h<=c and (x+v, y+h) not in visited:
                weak_points.append((x+v, y+h))
                visited.add((x+v, y+h))
                temp += 1
        
        until_next -= 1
        if until_next == 0 and temp != 0:
             until_next = temp
             temp = 0
             counter += 1
        
        if len(visited) == r * c:
            break
    
    print(counter+1)