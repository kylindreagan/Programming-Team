import itertools

N,t = map(int, input().split())
A = [int(x) for x in input().split()]

if t == 1:
    possible = [x for x in itertools.combinations(A, 2) if sum(x) == 7777]
    if possible == []:
        print("No")
    else:
        for i,j in possible:
            if i != j:
                print("Yes")
                quit()
        print("No")

elif t == 2:
    if len(A) == len(set(A)):
        print("Unique")
        quit()
    print("Contains Duplicate")

elif t == 3:
    for num in A:
        if A.count(num) > N/2:
            print(num)
            quit()
    
    print(-1)

elif t == 4:
    A.sort()
    even = len(A)%2==0
    if even:
        print(A[(N//2)-1],A[(N//2)])
    else:
        print(A[N//2])

else:
    digit_range = [x for x in A if 999>=x and x>=100]
    digit_range.sort()
    print(" ".join(map(str, digit_range)))