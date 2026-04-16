p = 1
n = 1
final = []
while n != 0:
    sets = []
    n = int(input())
    if n == 0:
        break
    else:
        for i in range(n):
            name = str(input())
            sets.append(name)
        final.append(sets)
b = 0
for i in range(len(final)):
    firsthalf = []
    secondhalf = []
    sets2 = final[b]
    a = 0
    c = 1
    for i in range(len(sets2)):
        if (a + 2 <= len(sets2)):
            firsthalf.append(sets2[a])
            a += 2
        elif(c +2 <= len(sets2)):
            secondhalf.append(sets2[c])
            c += 2
        else:
            firsthalf.append(sets2[-1])
    print("SET", p)
    p += 1
    n2 = 0
    for i in range(len(firsthalf)):
        print(firsthalf[n2])
        n2 += 1
    n3 = -1
    for i in range(len(secondhalf)):
        print(secondhalf[n3])
        n3 -= 1
    b += 1

            