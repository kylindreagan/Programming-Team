#https://open.kattis.com/problems/tictactoe
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

def has_win(p):
    # horizontal
    for i in range(n):
        run = 0
        for j in range(n):
            if board[i][j] == p:
                run += 1
                if run >= m: return True
            else:
                run = 0

    # vertical
    for j in range(n):
        run = 0
        for i in range(n):
            if board[i][j] == p:
                run += 1
                if run >= m: return True
            else:
                run = 0

    # diag
    for s in range(-(n-1), n):
        run = 0
        for i in range(n):
            j = i + s
            if 0 <= j < n:
                if board[i][j] == p:
                    run += 1
                    if run >= m: return True
                else:
                    run = 0

    # anti
    for s in range(2*n-1):
        run = 0
        for i in range(n):
            j = s - i
            if 0 <= j < n:
                if board[i][j] == p:
                    run += 1
                    if run >= m: return True
                else:
                    run = 0
    return False


x = sum(r.count('X') for r in board)
o = sum(r.count('O') for r in board)
dots = sum(r.count('.') for r in board)

if not (x == o or x == o + 1):
    print("ERROR")
    exit()

x_win = has_win('X')
o_win = has_win('O')

if x_win and o_win:
    print("ERROR")
    exit()

def valid_last_move(player):
    for i in range(n):
        for j in range(n):
            if board[i][j] == player:
                board[i][j] = '.'
                if not has_win(player):
                    board[i][j] = player
                    return True
                board[i][j] = player
    return False


if x_win:
    if x != o + 1 or not valid_last_move('X'):
        print("ERROR")
    else:
        print("X WINS")

elif o_win:
    if x != o or not valid_last_move('O'):
        print("ERROR")
    else:
        print("O WINS")

else:
    if dots:
        print("IN PROGRESS")
    else:
        print("DRAW")