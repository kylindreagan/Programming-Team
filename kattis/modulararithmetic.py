import operator
operators = {'+': operator.add, '-': operator.sub, '*': operator.mul}

def gcdExtended(a,b):
    x,y,u,v=0,1,1,0
    while a != 0:
        q,r = b//a,b%a
        m,n=x-u*q,y-v*q
        b,a,x,y,u,v,=a,r,u,v,m,n
    gcd = b 
    return gcd, x, y


def modOp(b,m,a):
    d, x, y = gcdExtended(b, m)
    if d != 1: return -1
    return (a*x)%m

def main():
    while True:
        MOD, cases = map(int, input().split())
        if MOD == cases == 0:
            break
        for _ in range(cases):
            x, op, y = input().split()
            x, y = int(x), int(y)
            if op == '/':
                print(modOp(y, MOD, x))
            else:
                print(operators[op](x,y)%MOD)

main()