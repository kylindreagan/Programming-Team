import re

digits = '0123456789'

def next_element(n:str) -> str:
    k = ""
    for d in digits:
        count = len(re.findall(d, n))
        if count != 0:
            k += str(count) + d
    return k
    
def in_seq(n:str, m:str, max_seq:int = 101) -> int:
    seen = set()
    curr = n
    for i in range(max_seq):
        if m == curr:
            return i + 1
        seen.add(curr)
        curr = next_element(curr)
        if curr in seen:
            return -1
    return -1


n, m = input().split()
if n == m:
    print(1)
else:
    ans = in_seq(n,m)
    if ans < 0:
        print("Does not appear")
    else:
        print(ans)