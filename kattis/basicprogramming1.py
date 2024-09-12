N, t = map(int, input().split())

A = [int(x) for x in input().split()]

if t == 1:
    print(7)
elif t == 2:
    if A[0] == A[1]:
        print("Equal")
    else:
        print(["Bigger", "Smaller"][A[0] < A[1]])
elif t == 3:
    print(sorted(A[:3])[1])
elif t == 4:
    print(sum(A))
elif t == 5:
    A = [z for z in A if z % 2 == 0]
    print(sum(A))
elif t == 6:
    A = [chr(y%26+97) for y in A]
    print("".join(A))
else:
    i, inds = 0, {0}
    N -= 1
    if max(A) < N:
        print("Cyclic")
        quit()
    while True:
        if i < 0 or i > N:
            print("Out")
            quit()
        if i == N:
            print("Done")
            quit()
        i = A[i]
        if i in inds:
            print("Cyclic")
            quit()
        inds.add(i)