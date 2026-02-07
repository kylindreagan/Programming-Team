import heapq

def board_search(board, n, end):
    visited = set()
    fully_visited = set()
    pq = [(board[end][0], 1)]
    for key in board.keys():
        if key != end:
            pq.append((board[key][0], 1))
    
    while pq:
        position, steps = heapq.heappop(pq)
        if position == n-1:
            return steps
        if position in visited:
            continue
        visited.add(position)
        for k in board.keys():
            done = True
            if k in fully_visited:
                continue
            for i in board[k]:
                if i not in visited:
                    done = False
                    if i < position:
                        continue
                    heapq.heappush(pq, (i, steps+1))
                    break
            if done:
                fully_visited.add(k)

n = int(input())
board = {}
for i in range(n):
    curr_color = input()
    if i == n-1:
        end = curr_color
    if curr_color  not in board:
        board[curr_color] = []
    board[curr_color].append(i)

print(board_search(board, n, end))