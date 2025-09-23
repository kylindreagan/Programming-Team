#found at https://www.geeksforgeeks.org/matrix-exponentiation/#finding-nth-fibonacci-number
MOD = 10**9 + 7
def multiply(A, B):
    # Matrix to store the result
    C = [[0, 0], [0, 0]]

    # Matrix Multiply
    C[0][0] = (A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD
    C[0][1] = (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD
    C[1][0] = (A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD
    C[1][1] = (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD

    # Copy the result back to the first matrix
    A[0][0] = C[0][0]
    A[0][1] = C[0][1]
    A[1][0] = C[1][0]
    A[1][1] = C[1][1]

# Function to find (Matrix M ^ expo)
def power(M, expo):
    # Initialize result with identity matrix
    ans = [[1, 0], [0, 1]]

    # Fast Exponentiation
    while expo:
        if expo & 1:
            multiply(ans, M)
        multiply(M, M)
        expo >>= 1

    return ans


def nthFib(n):
    # Base case
    if n == 1:
        return 1, 1  # F(1) = 1, F(2) = 1

    M = [[1, 1], [1, 0]]
    # F(0) = 0, F(1) = 1

    # Multiply matrix M (n - 2) times
    res = power(M, n - 2)

    return res[1][0], res[0][0]

#End of geeksforgeeks code
a, b = map(int, input().split())
n = int(input())
if n == 0:
    print(a,b)
    quit()

#a always starts at nth odd number
start =  1 + (2 * (n-1))
FibStep0, FibStep1 = nthFib(start + 2)
FibStep2 = (FibStep0 + FibStep1) % MOD
an = (FibStep0*a + FibStep1*b) % MOD
bn = (FibStep1*a + FibStep2*b) % MOD
print(an,bn)