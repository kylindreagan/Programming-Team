m = int(input())
printing = []
for i in range(m):
    xBook, yBook = map(eval, input().split())
    numCandle = int(input())
    distances = []
    for i in range(numCandle):
        candleX, candleY = map(eval,input().split())
        Distance = ( ((xBook - candleX)** 2) - ((yBook - candleY) ** 2) ) ** .5
        distances.append(Distance)
    n = 0
    for i in range(len(distances)):
        