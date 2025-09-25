import re
n = int(input())
digits = {c:i for i, c in enumerate(input().split())}
num = input()
pattern = re.compile('|'.join(map(re.escape, digits)))
tokens  = pattern.findall(num)
tokens.reverse()
total = 0
for j, t in enumerate(tokens):
    total += digits[t] * (n**j)
print(total)