from collections import deque
from bisect import bisect_right

def board_search(colors):
    n = len(colors)

    board = {}
    for i, c in enumerate(colors):
        board.setdefault(c, []).append(i)

    q = deque([( -1, 0 )])
    visited_positions = set([-1])

    while q:
        pos, steps = q.popleft()

        if pos == n - 1:
            return steps
        
        for c, lst in board.items():
            j = bisect_right(lst, pos)
            if j == len(lst):
                continue

            nxt = lst[j]

            if nxt not in visited_positions:
                visited_positions.add(nxt)
                q.append((nxt, steps + 1))


n = int(input())
colors = [input().strip() for _ in range(n)]
print(board_search(colors))