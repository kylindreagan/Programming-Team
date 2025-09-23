def partition(arr, index, n):
    for j in range(n - index):
        if arr[j+index] < arr[index]: return False
    return True

n = int(input())
arr = [int(x) for x in input().split()]
if arr == sorted(arr): print(len(arr))
else:
    count, biggest, allTime = 0, 0, max(arr)
    for i in range(n):
        curr = arr[i]
        if curr == allTime:
            if partition(arr, i, n): count += 1
            break
        if curr > biggest:
            biggest = curr 
            if partition(arr, i, n):count += 1
    
    print(count)