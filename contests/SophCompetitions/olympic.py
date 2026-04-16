import math
from collections import OrderedDict

for _ in range(int(input())):
    p = {} 
    for i in range(int(input())):
        weight, num = map(int, input().split())
        p[weight] = num
    for j in range(int(input())):
        target = int(input())
        if target < 45:
            print("No solution")
        else:
            total = {}
            sortedP = OrderedDict(sorted(p.items(), key=lambda x:x[0], reverse = True))
            current = 45
            b = 0
            while True:
                try:
                    plates = [x for x in sortedP.keys()]
                    cWeight = plates[b]
                    if current == target:
                        if current == 45:
                            print("No plates")
                        count = 1
                        for h in total.keys(): 
                            if count == len(total):
                                print(h, "x", total[h])
                            else:
                                print(h, "x", total[h], end=",")
                                count += 1
                        break
                    elif target == current:
                        count = 1
                        for h in total.keys(): 
                            if count == len(total):
                                print(h, "x", total[h])
                            else:
                                print(h, "x", total[h], end=",")
                                count += 1
                        break
                    elif abs(target - (current + cWeight*2)) < abs(target - current) and target - (current + cWeight*2) >= 0:
                        current += cWeight * 2
                        if cWeight not in total:
                            total[cWeight] = 0
                        total[cWeight] += 2
                        if (sortedP[cWeight] - 2) == 0:
                            b += 1
                        else:
                            sortedP[cWeight] -= 2
                    else:
                        b += 1
                except IndexError:
                    if len(total) == 0:
                        print("No plates")
                    else:
                        count = 1
                        for h in total.keys(): 
                            if count == len(total):
                                print(h, "x", total[h])
                            else:
                                print(h, "x", total[h], end=", ")
                                count += 1
                    break