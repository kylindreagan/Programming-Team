n,k = map(int, input().split())
can_get = [True] * k
init = input()
for i in range(n-1):
    test = input()
    for i in range(len(test)):
        if can_get[i]:
            can_get[i] = test[i] == init[i]
    if all(element == False for element in can_get):
        print(0)
        break
total = 0
for t in can_get:
    if t:
        total += 1
print(total)