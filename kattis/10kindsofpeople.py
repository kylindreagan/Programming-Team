from collections import deque

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]# LEFT, RIGHT, UP, DOWN

def segregation_enforcer(start, target, world, len_target, width_target, init_point, visited, run_id) -> bool:
    Q = deque([start])

    targetx, targety = target
    
    while Q:
        currx, curry = Q.popleft()
        
        if currx == targetx and curry == targety:
            return True
        
        for dx, dy in directions:
            nextx, nexty = currx + dx, curry + dy
            if 0 <= nextx <= width_target and 0 <= nexty <= len_target:
                if visited[nexty][nextx] != run_id and world[nexty][nextx] == init_point:
                    visited[nexty][nextx] = run_id
                    Q.append((nextx, nexty))

    return False

def main():
    mapy, mapx = map(int, input().split())
    world = [list(input()) for row in range(mapy)]
    wbinary = sum(x.count(0) for x in world)
    wdecimal = sum(x.count(1) for x in world)
    
    n = int(input())
    for i in range(n):
        r1, r2, c1, c2 = map(int,input().split())
        r1, r2, c1, c2 = r1-1, r2-1, c1-1, c2-1
        init_point = world[r1][r2]
        visited = [[0] * mapx for _ in range(mapy)]
        if r1 == c1 and r2 == c2:
            print(["binary","decimal"][int(init_point)])
        elif init_point != world[c1][c2]:
            print("neither")
        elif (init_point == 0 and wbinary < 2) or (init_point == 1 and wdecimal < 2):
            print("neither")
        elif (init_point == 1 and wbinary == 0) or (init_point == 0 and wdecimal == 0):
             print(["binary","decimal"][int(init_point)])
        else:
            if segregation_enforcer((r2,r1), (c2, c1), world, mapy-1, mapx-1, init_point, visited, i+1):
                print(["binary","decimal"][int(init_point)])
            else:
                print("neither")

if __name__ == "__main__":
    main()