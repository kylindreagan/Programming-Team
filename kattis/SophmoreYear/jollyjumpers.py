try:
    while True:
        n, *sequence = map(int, input().split())
        visited = [False for _ in range(n-1)]

        for i in range(n-1):
            curr = abs(sequence[i]-sequence[i+1])
            if curr > n-1:
                break
            else:
                visited[curr-1] = True
        
        if False in visited:
            print("Not jolly")
        else:
            print("Jolly")

except EOFError:
    quit()