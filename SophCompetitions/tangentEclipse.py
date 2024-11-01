""" 
Ax^2 + By^2 = C
2Ax + 2Byy' = 0

y - e = m(x - d) 

b^2 - 4ac
"""

for i in range(int(input())):
    A, B, C, d, e = map(float, input().split())
    m = (A*d)/(B*e) * -1
    b = (A*d*d)/ (B*e) + e
    if b >= 0:
        print("Line #"+str(i+1)+":  y =", f'{m:.3f}'+"x +", f'{b:.3f}')
    else:
        print("Line #"+str(i+1)+":  y =", f'{m:.3f}'+"x -", f'{abs(b):.3f}')