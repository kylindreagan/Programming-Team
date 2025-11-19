while True:
    try:
        n = int(input())
        pies = [int(x) for x in input().split()]
        tails = []
        tails_idx = []
        parent = [-1] * n
        pos = [0] * n
        for i, pie in enumerate(pies):
            l, r = 0, len(tails)
            while l < r:
                m = (l + r) // 2
                if tails[m] < pie:
                    l = m + 1
                else:
                    r = m
            if l == len(tails):
                tails.append(pie)
                tails_idx.append(i)
            else:
                tails[l] = pie
                tails_idx[l] = i

            pos[i] = l
            if l > 0:
                parent[i] = tails_idx[l-1]
        
        lis_len = len(tails)
        lis = []

        # find where LIS ends
        last = tails_idx[-1]
        while last != -1:
            lis.append(last)
            last = parent[last]

        lis.reverse()
        str_lis = [str(x) for x in lis]

        print(lis_len)
        print(" ".join(str_lis))
    except EOFError:
        break