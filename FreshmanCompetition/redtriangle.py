N = int(input())
final = []
for i in range(N):
    strips = [int(x) for x in input().split()]
    b = 1
    totalA = 1
    for i in range(len(strips)-1):
        totalA = totalA - 1 + strips[b]
        b += 1
    final.append(totalA)
n = 0
for i in range(len(final)):
    print(final[n])
    n += 1