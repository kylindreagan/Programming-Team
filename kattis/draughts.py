from collections import deque
def locate(ele1, ele2, array):
    location_dict = {ele1: set() , ele2: set()}
    for row in range(10):
        for col in range(10):
            element = array[row][col]
            if element == ele1:
                location_dict[ele1].add((row,col))
            elif element == ele2:
                location_dict[ele2].add((row,col))
    
    return location_dict

def possible_jump(x1, y1, x2, y2, pieces):
    if abs(x2-x1) <= 1 and abs(y2-y1) <= 1:
        if 0 <= x2+x2-x1 < 10 and 0 <= y2+y2-y1 < 10:
            if (x2+x2-x1,y2+y2-y1) not in pieces:
                return True
    return False

def draught_search(locations, board):
    max_jumps = 0
    D = deque()
    og_frozenB = frozenset(locations["B"])
    og_frozenW = frozenset(locations["W"])
    for white in locations["W"]:
        init_curr = (white, og_frozenB, og_frozenW, 0)
        D.append(init_curr)
    while D:
        curr = D.popleft()
        coords, frozen_blacks, frozen_whites, jumps = curr
        blacks = set(frozen_blacks)
        whites = set(frozen_whites)
        x1, y1 = coords
        pieces = blacks.union(whites)
        for x2, y2 in blacks:
            if possible_jump(x1,y1,x2,y2,pieces):
                new_coords = (x2+x2-x1, y2+y2-y1)
                tempB = blacks.copy()
                tempB.remove((x2,y2))
                f_tempB = frozenset(tempB)
                tempW = whites.copy()
                tempW.remove((x1,y1))
                tempW.add(new_coords)
                f_tempW = frozenset(tempW)
                D.append((new_coords, f_tempB, f_tempW, jumps+1))
                max_jumps = max(max_jumps, jumps+1)
    return max_jumps

for i in range(int(input())):
    _ = input().split()
    board = [list(input()) for _ in range(10)]
    location_dict = locate("W", "B", board)
    
    
    if location_dict["W"] == set() or location_dict["B"] == set():
        print(0)
    else:
        print(draught_search(location_dict, board))