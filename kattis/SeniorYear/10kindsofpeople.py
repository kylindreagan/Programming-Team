from collections import deque

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]# LEFT, RIGHT, UP, DOWN

def labelMap(world, mapy, mapx):
    labels = [[-1]*mapx for _ in range(mapy)]
    label_id = 0

    for y in range(mapy):
        for x in range(mapx):
            if labels[y][x] == -1:
                segregateWorld(world, labels, y, x, mapy, mapx, label_id)
                label_id += 1
    return labels

def segregateWorld(world, labels, starty, startx, mapy, mapx, label_id):
    init_point = world[starty][startx]
    queue = deque([(starty, startx)])
    labels[starty][startx] = label_id

    while queue:
        y, x = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < mapx and 0 <= ny < mapy:
                if world[ny][nx] == init_point and labels[ny][nx] == -1:
                    labels[ny][nx] = label_id
                    queue.append((ny, nx))
def main():
    mapy, mapx = map(int, input().split())
    world = [list(input()) for _ in range(mapy)]
    
    n = int(input())
    m = labelMap(world, mapy, mapx)
    for _ in range(n):
        r1, r2, c1, c2 = map(int,input().split())
        r1, r2, c1, c2 = r1-1, r2-1, c1-1, c2-1
        init_point = world[r1][r2]
        if r1 == c1 and r2 == c2:
            print(["binary","decimal"][int(init_point)])
        elif init_point != world[c1][c2]:
            print("neither")
        else:
            if m[r1][r2]==m[c1][c2]:
                print(["binary","decimal"][int(init_point)])
            else:
                print("neither")

if __name__ == "__main__":
    main()