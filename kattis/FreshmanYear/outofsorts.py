def binarySearch(l, small, large, n):
    while large >= small:
        mid = (small + large) // 2
        if l[mid] == n:
            return True
        elif l[mid] < n:
            small = mid + 1
        else:
            large = mid - 1
    
    return False

n, m, a, c, x = map(int, input().split())
currArr = [_ for _ in range(n)]

for i in range(n):
    x = (a * x + c) % m
    currArr[i] = x

if currArr == sorted(currArr):
    print(len(currArr))
    
else:
    successes = 0
    size = len(currArr) - 1
    for h in currArr:
        if(binarySearch(currArr, 0, size, h)):
            successes += 1
    
    print(successes)
