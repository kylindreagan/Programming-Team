n = int(input())
class_dict = {}
for i in range(n):
    prob_type = input().split()
    prob_name = prob_type[0]
    words = prob_type[2:]
    class_dict[prob_name] = words

problem = []

try:
    while True:
        temp = input().split()
        if temp == []:
            raise EOFError
        problem = problem + temp

except EOFError:
    max_count = -1
    possible = {}
    for k,j in class_dict.items():
        running_total = 0
        for j1 in j:
            running_total += problem.count(j1)
        if running_total == max_count:
            possible[k] = running_total
        elif running_total > max_count:
            max_count = running_total
            possible = {}
            possible[k] = running_total
    
    possSort = sorted(possible.keys(), key=lambda x:x)
    for key in possSort:
        print(key)