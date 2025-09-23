b_list = []
primes = []

def sieve(n):
    global b_list
    global primes
    b_list = [True] * (n+1)
    for i in range(2, n+1):
        if b_list[i]:
            for j in range(i*i, n+1, i):
                b_list[j] = False
    primes = [str(i) for i in range(2,n+1) if b_list[i]]

#l= smallest prime, h = biggest prime
l, h = map(int, input().split())
#p = substring
p = str(input())
sieve(10000000)

primeList = set()
count = 1
for i in range(h):
    if count >= l:
        primeList.add(primes[i])
    count += 1
final = [str(x) for x in primeList if str(x).find(p) != -1]

print(len(final))