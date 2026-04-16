for _ in range(int(input())):
    _, *rank  = map(int, input().split())
    rank.sort(reverse=True)
    unique = set()
    seen = False
    total = 0
    for r in rank:
        if seen and r not in unique:
            total += 1
        elif r in unique:
            seen = True
        else:
            unique.add(r)
    print(total)