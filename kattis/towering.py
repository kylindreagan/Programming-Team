import itertools

boxes = [int(x) for x in input().split()]
t2 = boxes.pop(-1)
t1 = boxes.pop(-1)

temp = [x for x in itertools.combinations(boxes, 3) if sum(x) == t1]
tower1 = list(temp[0])
tower2 = [i for i in boxes if i not in tower1]
tower1.sort(key=lambda x:x, reverse=True)
tower2.sort(key=lambda x:x, reverse=True)
final = [str(j) for j in tower1 + tower2]
print(" ".join(final), end=" ")