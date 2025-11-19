import heapq

c, p, x, l = map(int, input().split())
trade = []
stay, og = {i:0 for i in range(c)}, {i:0 for i in range(c)}
relations = {i:set() for i in range(c)}

if x == l:
    print('leave')
    quit()

for i in range(p):
    a,b = map(int, input().split())
    a-=1
    b-=1
    stay[a] += 1
    stay[b] += 1
    og[a] += 1
    og[b] += 1
    relations[a].add(b)
    relations[b].add(a)

leaving = [l-1]
stay[l-1] = og[l-1] = 0

while leaving:
    y = heapq.heappop(leaving)
    for y_n in relations[y]:
        if og[y_n] != 0:
            stay[y_n] -= 1
            if stay[y_n] <= og[y_n] // 2:
                stay[y_n] = og[y_n] = 0
                heapq.heappush(leaving, y_n)
                if y_n == x-1:
                    print("leave")
                    quit()

print("stay")