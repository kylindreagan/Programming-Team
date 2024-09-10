import math

def digit_sum(n, memory):
    if n in memory:
        return memory[n]
    og_n = n
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    memory[og_n] = s
    return s


def digit_sum_precomp(limit, memory):
    # Precompute digit sums for all numbers up to 'limit'
    digit_sums = {x:0 for x in range(limit+1)}
    for i in range(1, limit + 1):
        if i < 10:
            digit_sums[i] = (i * (i + 1)) // 2
        else:
            digit_sums[i] = digit_sums[i - 1] + digit_sum(i, memory)
    return digit_sums

# Sum of digits from 1 to n using a logarithmic approach
def sumOfDigitsFrom1ToN(n, mem, bound):
    if n <= bound:
        return mem[n]

    d = int(math.log10(n))  # Number of digits in n - 1
    a = [0] * (d + 2)  # Precompute sum of digits from 1 to 10^i - 1
    a[0] = 0
    a[1] = 45  # Sum of digits from 1 to 9
    for i in range(2, d + 1):
        a[i] = a[i - 1] * 10 + 45 * 10 ** (i - 1)

    return sumOfDigitsFrom1ToNUtil(n, a, mem, bound)

# Helper function to compute the sum of digits from 1 to n
def sumOfDigitsFrom1ToNUtil(n, a, digit_sums, bound):
    total = 0
    while n > 0:
        if n <= bound:
            total += digit_sums[n]
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
    n = int(input())
    ranges = [None for _ in range(n)]
    digit_cache = {}
    max_limit = 0
    for i in range(n):
        x, y = map(int, input().split())
        ranges[i] = (x,y)
        max_limit = max(max_limit, y)
           
    bound = min(max_limit, 1000000)
    digit_sums = digit_sum_precomp(bound, digit_cache)

    if max_limit <= 1000000:
        for x,y in ranges:
            if x == 0:
                print(digit_sums[y])
            else:
                print(digit_sums[y] - digit_sums[x-1])
        quit()

    for x, y in ranges:
        if x == 0:
            print(sumOfDigitsFrom1ToN(y, digit_sums, bound))
        else:
            print(sumOfDigitsFrom1ToN(y, digit_sums, bound) -
                  sumOfDigitsFrom1ToN(x - 1, digit_sums, bound))

if __name__ == "__main__":
    main()