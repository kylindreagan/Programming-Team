from itertools import groupby

def max_consecutive_count(lst, element):
    return max((len(list(group)) for key, group in groupby(lst) if key == element), default=0)

while True:
    boxes = []
    n =int(input())
    if n == 0:
        break
    for i in range(n):
        weight, max_load = map(int, input().split())
        boxes.append((i,weight, max_load))

    boxes.sort(key=lambda x: -x[2])
    max_stack = 0
    running_stack = [0-boxes[i][2] for i in range(n)]
    is_valid_box = [False]*n
    is_valid_box[0] = True
    for h in range(1,n):
        curr_box = boxes[h]
        for j in range(h):
            if running_stack[j] <= 0 and boxes[j][0] < curr_box[0] :
                running_stack[j] += curr_box[1]
                is_valid_box[j] = running_stack[j] <= 0
        is_valid_box[h] = True
        max_stack = max(max_consecutive_count(is_valid_box, True), max_stack)
    print(max_stack)