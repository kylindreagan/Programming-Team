from math import comb

for i in range(int(input())):
    r,s,x,y,w = map(int, input().split())
    p = s-r+1
    prob = sum([comb(y, i)*(p/s)**i*(1-p/s)**(y-i) for i in range(x,y+1)])
    if w * prob > 1:
        print("yes")
    else:
        print("no")