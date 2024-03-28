from math import ceil
n = int(input())

printer = 1
statues = 0
days = 0
while statues < n:
    if n < 3 * printer:
        statues += printer
        days += 1
    else:
        if printer == 1:
            printer += 1
            days += 1
        elif n // 2 > printer:
            printer += printer
            days += 1
        else:
            statues += ceil(printer/2)
            printer += (printer//2)
            days += 1

print(days)