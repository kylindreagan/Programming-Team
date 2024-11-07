for _ in range(int(input())):
    towns, paths = map(int, input().split())
    adj = [set() for k in range(towns)]
    for path in range(paths):
        fromCity, toCity = map(int, input().split())
        adj[fromCity-1].add(toCity-1)
    for i in range(towns):
        for j in range(towns):
            if not i in adj[j]: continue
            for k in adj[i]:
                adj[j].add(k)
    loopExists = False
    for m in range(towns):
        if m in adj[m]:
            loopExists = True
            break
    print("YES" if loopExists else "NO")
