moves = 0
board = [list(input()) for _ in range(7)]
for i in range(7):
    if "." in board[i]:
        curr_row = board[i]
        for j in range(7):
            if curr_row[j] == ".":
                if j > 1 and curr_row[j-1] == "o" and curr_row[j-2] == "o":
                    moves += 1
                if j < 5 and curr_row[j+1] == "o" and curr_row[j+2] == "o":
                    moves += 1
                if i > 1 and board[i-1][j] == "o" and board[i-2][j] == "o":
                    moves += 1
                if i < 5 and board[i+1][j] == "o" and board[i+2][j] == "o":
                    moves += 1
print(moves)