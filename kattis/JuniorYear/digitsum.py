from collections import defaultdict

def precompute_sums(max_digit):
    a = [0] * (max_digit + 1)
    a[0] = 0
    a[1] = 45  # Sum of digits from 1 to 9
    for i in range(2, max_digit + 1):
        a[i] = a[i - 1] * 10 + 45 * 10 ** (i - 1)
    return a

# Helper function to compute the sum of digits from 1 to n
def sumOfDigitsFrom1ToN(n, a, mem):
    if n in mem:
        return mem[n]
    ogn = n
    total = 0
    while n > 0:
        if n in mem:
            total += mem[n]
            break
        # Determine the number of digits
        d = get_log10(int(n))
        p = 10 ** d  # 10^d, largest power of 10 <= n
        msd = n // p  # Most significant digit of n

        # Contribution from the most significant digit
        total += (int)(msd * a[d] + (msd*(msd-1) // 2) * p +  
            msd * (1 + n % p))
        n %= p
    
    # Cache the result
    mem[ogn] = total
    return total

def get_log10(x):
    return len(str(x))-1

def main():
    n = int(input())
    a = precompute_sums(15)

    mem = defaultdict(int)
    mem[0]
    for j in range(1,16):
        if j < 9:
            mem[j] = (j * (j + 1)) // 2
        
    queries = [tuple(map(int, input().split())) for _ in range(n)]
    results = []
    
    for x,y in queries:
        total = sumOfDigitsFrom1ToN(y, a, mem)
        if x > 0:
            total -= sumOfDigitsFrom1ToN(x-1, a, mem)
        results.append(total)

    print("\n".join(map(str, results)))

if __name__ == "__main__":
    main()