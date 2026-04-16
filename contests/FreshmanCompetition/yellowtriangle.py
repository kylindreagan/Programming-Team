n = 0
totals = []
while n != -1:
    n = int(input())
    previousHour = 0
    total = 0
    for i in range(n):
        miles,hours = map(int, input().split())
        total = total + miles * (hours - previousHour)
        previousHour = hours
    totals.append(total)
count = 0
for i in range(len(totals)-1):
    print(totals[count], "miles")
    count += 1