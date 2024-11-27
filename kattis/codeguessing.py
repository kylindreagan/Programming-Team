from itertools import combinations
p, q = map(int, input().split())

order = input()
remainder = [x for x in range(1,10) if x != p and x != q]
correct_count = 0
answer = None

for b, d in combinations(remainder, 2):
    cards_given = sorted([p,q,b,d])
    curr_order = ''.join("B" if x in remainder else "A" for x in cards_given)
    if curr_order == order:
        correct_count += 1
        answer = (b,d)
    if correct_count > 1:
        break

if correct_count == 1:
    print(answer[0], answer[1])
else:
    print(-1)