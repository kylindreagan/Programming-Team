import heapq
from math import sqrt
from collections import defaultdict

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]# LEFT, RIGHT, UP, DOWN

def heuristic(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

cache = set()
uncache = set()

def segregation_enforcer(start, target, world, len_target, width_target, init_point) -> bool:
    final_tuple = (start, target)
    pq = []
    targetx, targety = target
    heapq.heappush(pq, (heuristic(*start,  targetx, targety), 0, start))
    cost_so_far = defaultdict()
    cost_so_far[start] = 0
    visited = set()
    
    
    while pq:
        priority, current_cost, (currx, curry) = heapq.heappop(pq)
        curr = (currx, curry)

        if (abs(currx - targetx) == 1 and curry == targety) or (abs(curry - targety) == 1 and currx == targetx):
            cache.add(final_tuple)
            return True
        
        if (curr, target) in cache:
            cache.add(final_tuple)
            return True
        
        if (curr, target) in uncache:
            uncache.add(final_tuple)
            return False
        
        if curr in visited:
            continue
        
        visited.add(curr)

        up = down = left = right = False 
        
        for dx, dy in directions:
            nextx, nexty = currx + dx, curry + dy
            if 0 <= nextx <= width_target and 0 <= nexty <= len_target:
                if world[nexty][nextx] == init_point:
                    new_cost = current_cost + 1
                    next_tup = (nextx, nexty)
                    if dx == 1:
                            right = True
                    elif dx == -1:
                        left = True
                    else:
                        if dy == 1:
                            down = True
                        if dy == -1:
                            up = True
                    if new_cost < cost_so_far.get(next_tup, float('inf')):
                        cost_so_far[next_tup] = new_cost
                        priority = new_cost + heuristic(nextx, nexty, targetx, targety)
                        heapq.heappush(pq, (priority, new_cost, next_tup))
        
        if down == right == True or (down == True and currx < width_target) or (right == True and curry < len_target):
            nextx, nexty = currx + 1, curry + 1
            if world[nexty][nextx] == init_point:
                new_cost = current_cost + sqrt(2)
                next_tup = (nextx, nexty)
                if new_cost < cost_so_far.get(next_tup, float('inf')):
                    cost_so_far[next_tup] = new_cost
                    priority = new_cost + heuristic(nextx, nexty, targetx, targety)
                    heapq.heappush(pq, (priority, new_cost, next_tup))
        
        # Diagonal South-West (Down-Left)
        if down == left == True or (down == True and currx > 0) or (left == True and curry < len_target):
            nextx, nexty = currx - 1, curry + 1
            if world[nexty][nextx] == init_point:
                new_cost = current_cost + sqrt(2)
                next_tup = (nextx, nexty)
                if new_cost < cost_so_far.get(next_tup, float('inf')):
                    cost_so_far[next_tup] = new_cost
                    priority = new_cost + heuristic(nextx, nexty, targetx, targety)
                    heapq.heappush(pq, (priority, new_cost, next_tup))

        # Diagonal North-East (Up-Right)
        if up == right == True or (up == True and currx < len_target) or (right == True and curry > 0):
            nextx, nexty = currx + 1, curry - 1
            if world[nexty][nextx] == init_point:
                new_cost = current_cost + sqrt(2)
                next_tup = (nextx, nexty)
                if new_cost < cost_so_far.get(next_tup, float('inf')):
                    cost_so_far[next_tup] = new_cost
                    priority = new_cost + heuristic(nextx, nexty, targetx, targety)
                    heapq.heappush(pq, (priority, new_cost, next_tup))

        # Diagonal North-West (Up-Left)
        if up == left == True or (up == True and currx > 0) or (left == True and curry > 0):
            nextx, nexty = currx - 1, curry - 1
            if world[nexty][nextx] == init_point:
                new_cost = current_cost + sqrt(2)
                next_tup = (nextx, nexty)
                if new_cost < cost_so_far.get(next_tup, float('inf')):
                    cost_so_far[next_tup] = new_cost
                    priority = new_cost + heuristic(nextx, nexty, targetx, targety)
                    heapq.heappush(pq, (priority, new_cost, next_tup))


    uncache.add(final_tuple)
    return False

def main():
    mapy, mapx = map(int, input().split())
    world = [list(input()) for _ in range(mapy)]
    
    n = int(input())
    for _ in range(n):
        r1, r2, c1, c2 = map(int,input().split())
        r1, r2, c1, c2 = r1-1, r2-1, c1-1, c2-1
        init_point = world[r1][r2]
        if r1 == c1 and r2 == c2:
            print(["binary","decimal"][int(init_point)])
        elif init_point != world[c1][c2]:
            print("neither")
        else:
            if segregation_enforcer((r2,r1), (c2, c1), world, mapy-1, mapx-1, init_point):
                print(["binary","decimal"][int(init_point)])
            else:
                print("neither")

if __name__ == "__main__":
    main()