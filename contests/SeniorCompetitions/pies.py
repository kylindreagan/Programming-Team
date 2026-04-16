for i in range(int(input())):
    n = int(input())
    pies = [int(x) for x in input().split()][:n]
    tails = []
    for pie in pies:
        l, r = 0, len(tails)
        while l < r:
            m = (l + r) // 2
            if tails[m] < pie:
                l = m + 1
            else:
                r = m
        if l == len(tails):
            tails.append(pie)
        else:
            tails[l] = pie
    print(f"Case {i + 1}: {n - len(tails)}")