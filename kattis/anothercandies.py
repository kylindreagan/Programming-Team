for i in range(int(input())):
    input()
    n = int(input())
    running_total = sum(int(input()) for x in range(n))
    print(["NO", "YES"][running_total % n == 0])