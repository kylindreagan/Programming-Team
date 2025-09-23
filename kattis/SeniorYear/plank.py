import heapq

n = int(input())
pq = [n]
t = 0

while pq:
    curr = heapq.heappop(pq)
    if curr - 1 == 0:
        t += 1
    elif curr - 1 > 0:
        heapq.heappush(pq, curr - 1)
    if curr - 2 == 0:
        t += 1
    elif curr - 2 > 0:
        heapq.heappush(pq, curr - 2)
    if curr - 3 == 0:
        t += 1
    elif curr - 3 > 0:
        heapq.heappush(pq, curr - 3)

print(t)