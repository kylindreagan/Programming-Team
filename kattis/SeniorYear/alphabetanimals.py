animal = input()
start = animal[-1]
alphabet = {chr(i): 0 for i in range(97, 123)}
best = "?"
pick = False
valid = []

for i in range(int(input())):
    nextanim = input()
    nextalpha = nextanim[0]
    if nextanim[0] == start:
        valid.append(nextanim)
        if not pick:
            best = nextanim
            pick = True
    alphabet[nextalpha] += 1

for a in valid:
    if (alphabet[a[-1]] < 2 and a[-1] == a[0]) or not alphabet[a[-1]]:
        best = a + "!"
        break

print(best)