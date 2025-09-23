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
    rowscols = ((M-1) + (N-1)) * N * M
    #symmetrical
    diagonal = diagonal_pairs(N, M)*2
    return rowscols + diagonal

def diagonal_pairs(n: int, m: int) -> int:
    min_num = min(n, m)
    nondependant_diag=abs(abs(n-m)-1) * (min_num*(min_num-1))//2
    dependant_diag = ((min_num-1)*min_num*(min_num+1))//3
    #2 diagonals
    return (dependant_diag+nondependant_diag)*2

while True:
    M, N = map(int, input().split())
    if M == N == 0:
        break
    elif M == N:
        print(count_queens_square(N))
    else:
        print(count_queens_summation(M,N))