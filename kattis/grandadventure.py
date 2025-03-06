from collections import deque

for i in range(int(input())):
    journey = input().strip('.')
    money = jewels = incense = 0
    bag = deque()
    failure = False
    for step in journey:
        if step == '.':
            continue
        if step == "$":
            money += 1
            bag.append(step)
        elif step == "|":
            incense += 1
            bag.append(step)
        elif step == "*":
            jewels += 1
            bag.append(step)
        elif step == "b":
            if money == 0:
                print("NO")
                failure = True
                break
            while bag:
                curr = bag.pop()
                if curr == "$":
                    money -= 1
                    break
                if curr == "|":
                    incense -= 1
                if curr == "*":
                    jewels -= 1
        elif step == "j":
            if jewels == 0:
                print("NO")
                failure = True
                break
            while bag:
                curr = bag.pop()
                if curr == "$":
                    money -= 1
                if curr == "|":
                    incense -= 1
                if curr == "*":
                    jewels -= 1
                    break
        else:
            if incense == 0:
                print("NO")
                failure = True
                break
            while bag:
                curr = bag.pop()
                if curr == "$":
                    money -= 1
                if curr == "|":
                    incense -= 1
                    break
                if curr == "*":
                    jewels -= 1
    if not failure:
        if jewels == money == incense == 0:
            print("YES")
        else:
            print("NO")