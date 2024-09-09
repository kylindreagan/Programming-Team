import math

# Sum of digits from 1 to n using a logarithmic approach
def sumOfDigitsFrom1ToN(n):
    if n < 10:
        return (n * (n + 1)) // 2

    d = int(math.log10(n))  # Number of digits in n - 1
    a = [0] * (d + 2)  # Precompute sum of digits from 1 to 10^i - 1
    a[0] = 0
    a[1] = 45  # Sum of digits from 1 to 9
    for i in range(2, d + 1):
        a[i] = a[i - 1] * 10 + 45 * 10 ** (i - 1)

    return sumOfDigitsFrom1ToNUtil(n, a)

# Helper function to compute the sum of digits from 1 to n
def sumOfDigitsFrom1ToNUtil(n, a):
    total = 0
    while n > 0:
        if n < 10:
            total += (n * (n + 1)) // 2
            break

        d = int(math.log10(n))
        p = 10 ** d  # 10^d, largest power of 10 <= n
        msd = n // p  # Most significant digit of n

        # Contribution of the most significant digit
        total += msd * a[d] + (msd * (msd - 1) // 2) * p + msd * (1 + n % p)

        # Reduce n by removing the most significant digit
        n %= p

    return total

def main():
    for _ in range(int(input())):
        x, y = map(int, input().split())

        # Handle range [x, y]
        totalA = sumOfDigitsFrom1ToN(y)
        if x > 0:
            totalA -= sumOfDigitsFrom1ToN(x - 1)

        print(totalA)

main()