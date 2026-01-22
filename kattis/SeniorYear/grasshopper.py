from collections import deque
import sys

moves = [(2,1), (1,2), (-2,1), (-1,2), (2,-1), (1,-2), (-2,-1), (-1,-2)]

for line in sys.stdin:
    r, c, gr, gc, lr, lc = map(int, line.split())
    
    gr -= 1
    gc -= 1
    lr -= 1
    lc -= 1

    visited = [[False]*c for _ in range(r)]
    q = deque([(gr, gc, 0)])
    visited[gr][gc] = True

    found = False

    while q:
        x, y, d = q.popleft()

        if x == lr and y == lc:
            print(d)
            found = True
            break

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny, d + 1))

    if not found:
        print("impossible")