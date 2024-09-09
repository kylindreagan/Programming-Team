def digit_sum(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s


def digit_sum_precomp(limit):
    # Precompute digit sums for all numbers up to 'limit'
    digit_sums = {x:0 for x in range(limit+1)}
    for i in range(1, limit + 1):
        digit_sums[i] = digit_sums[i - 1] + digit_sum(i)
    return digit_sums

def main():
    n = int(input())
    ranges = [None for _ in range(n)]
    ans = [None for _ in range(n)]
    max_limit = 0 

    for i in range(n):
        x,y = map(int, input().split())
        ranges[i] = (x,y)
        max_limit = max(max_limit, y)

    digit_sums = digit_sum_precomp(max_limit)

    for x,y in ranges:
        if x == 0:
            print(digit_sums[y])
        else:
            print(digit_sums[y] - digit_sums[x-1])

main()