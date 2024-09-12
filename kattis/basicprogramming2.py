from collections import Counter

N,t = map(int, input().split())
A = [int(x) for x in input().split()]

if t == 1:
    seen = set()
    for num in A:
        if 7777 - num in seen and 7777 - num != num:
            print("Yes")
            quit()
        seen.add(num)
    print("No")


elif t == 2:
    if len(A) == len(set(A)):
        print("Unique")
        quit()
    print("Contains Duplicate")

if t == 3:
    count = Counter(A)
    majority_element = -1
    for num, freq in count.items():
        if freq > N // 2:
            majority_element = num
            break
    print(majority_element)

elif t == 4:
    A.sort()
    even = len(A)%2==0
    mid = N//2
    if even:
        print(A[mid-1],A[(mid)])
    else:
        print(A[mid])

else:
    digit_range = sorted(x for x in A if 100 <= x <= 999)
    print(" ".join(map(str, digit_range)))