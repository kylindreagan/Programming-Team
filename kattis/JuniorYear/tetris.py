c, piece = map(int, input().split())
columns = [int(x) for x in input().split()]


#I block
if piece == 1:
    total = 0
    prev1 = prev2 = prev3 = float('inf')
    for i in columns:
        if i == prev1 == prev2 == prev3:
            total += 1
        total += 1
        prev3 = prev2
        prev2 = prev1
        prev1 = i
    print(total)

#O block
elif piece == 2:
    total = 0
    prev = float('inf')
    for i in columns:
        if i == prev:
            total += 1
        prev = i
    print(total)

#S block
elif piece == 3:
    total = 0
    prev1 = prev2 = float('inf')
    for i in columns:
        if i-1 == prev1 == prev2:
            total += 1
        if i == prev1-1:
            total += 1
        prev2 = prev1
        prev1 = i
    print(total)

#Z block
elif piece == 4:
    total = 0
    prev1 = prev2 = float('inf')
    for i in columns:
        if i == prev1 == prev2-1:
            total += 1
        if i-1 == prev1:    
            total+=1
        prev2 = prev1
        prev1 = i
    print(total)

#T block
elif piece == 5:
    total = 0
    prev1 = prev2 = float('inf')
    for i in columns:
        if i == prev1 == prev2:
            total += 1
        if i == prev1+1 == prev2 :
            total += 1
        if i == prev1+1:
            total += 1
        if i == prev1-1:
            total += 1
        prev2 = prev1
        prev1 = i
    print(total)

#L block
elif piece == 6:
    total = 0
    prev1 = prev2 = float('inf')
    for i in columns:
        if i == prev1 == prev2:
            total += 1
        if i == prev1 == prev2+1:
            total += 1
        if i == prev1-2:
            total += 1
        if i == prev1:
            total += 1
        prev2 = prev1
        prev1 = i
    print(total)

#J block
else:
    total = 0
    prev1 = prev2 = float('inf')
    for i in columns:
        if i == prev1 == prev2:
            total += 1
        if i+1 == prev1 == prev2:
            total += 1
        if i-2 == prev1:
            total += 1
        if i == prev1:
            total += 1
        prev2 = prev1
        prev1 = i
    print(total)