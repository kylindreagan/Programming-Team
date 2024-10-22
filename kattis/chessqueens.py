import math

def count_queens(N: int, M: int) -> int:
    rowscols = ((M-1) + (N-1)) * N * M
    diagonals = 0
    mid_N, mid_M = (N+2)//2, (M+2)//2
    odd_N, odd_M = N % 2 == 1, M % 2 == 1
    for i in range(1,(N+3)//2):
        for j in range(1,(M+3)//2):
            temp = min(i-1, j-1) + min(N-i, M-j) + min(i-1, N-j) + min(j-1, M-i)
            if i == mid_N and odd_N and j == mid_M and odd_M:
                diagonals += temp
            elif i == mid_N and odd_N:
                diagonals += temp * 2
            elif j == mid_M and odd_M:
                diagonals += temp * 2
            else:
                diagonals +=temp * 4
    return diagonals + rowscols 

def count_queens_square(N: int) -> int:
    rowscols = (2*(N-1)) * N ** 2
    current_square_size = (N+1) // 2
    diagonals = 0
    for i in range(current_square_size):
        if i == current_square_size-1 and N % 2 == 1:
             diagonals += (N - 1 + 2 * i)
        else:
            diagonals += (N - 1 + 2 * i) * (N - 1 - 2 * i) * 4
    return rowscols + diagonals
             
def count_queens_summation(N: int, M: int) -> int:
    horizontal = N * math.comb(M, 2) * 2
    vertical = M * math.comb(N, 2) * 2
    smallest_side = min(N, M)
    diagonal = abs(M-N) * math.comb(smallest_side, 2)
    # Major diagonals (\) - Top-left to bottom-right
    for k in range(2, smallest_side+1):  # Diagonal length
        count = (N - k+1) + (M - k + 1)
        diagonal += math.comb(k, 2) * count * 2
    return horizontal + vertical + diagonal

while True:
    M, N = map(int, input().split())
    if M == N == 0:
        break
    elif M == N:
        print(count_queens_square(N))
    else:
        print(count_queens(N, M))
    print(count_queens_summation(N, M))