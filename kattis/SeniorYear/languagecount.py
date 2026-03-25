from collections import defaultdict
lanCount = defaultdict(int)
for _ in range(int(input())):
    _, _, word = input().split()
    if word[-3:] == "(m)" or word[-3:] == "(f)":
        word = word[:-3]
    lanCount[word] += 1

sortedLan = dict(sorted(lanCount.items()))
for x in sortedLan.items():
    print(x[0], x[1])