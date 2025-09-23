def sieve(n):
    b_list = [True] * (n+1)
    for i in range(2, n+1):
        if b_list[i]:
            for j in range(i*i, n+1, i):
                b_list[j] = False
    primes = [i for i in range(2,n+1) if b_list[i]]

    return primes

og_list = sieve(32000)

for i in range(int(input())):
    representations, total = 0, []
    x = int(input())
    new_list = [i for i in og_list if i <= x//2]
    for e in new_list:
        if x-e in og_list:
            total.append((x-e, e))
            representations += 1
    
    print(f"{x} has {representations} representation(s)")
    for j in total:
        print(f"{j[1]}+{j[0]}")
    print()