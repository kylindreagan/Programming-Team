#n = number of circles
#m = 1 or 2; 1 means that the circles are laid out in a circle, while 2 means they are in a line

n, m = map(int, input().split())
field = [None for _ in range(n)]

turn = False

while True:
    x = int(input())
    if x > n or x < 1:
        break
    if m == 1:
        if x == 0:
            if field[x-1] != None or field[x] == turn:
                break
            else:
                field[x-1] = turn
        if x == n - 1:
            if field[x-1] != None or field[x-2] == turn:
                break
            else:
                field[x-1] = turn
        else:
            if field[x-1] != None or field[x-2] == turn or field[x] == turn:
                break
            else:
                field[x-1] = turn
    turn = not turn