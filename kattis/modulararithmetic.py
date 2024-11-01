import operator
operators = {'+': operator.add, '-': operator.sub, '*': operator.mul}

#https://www.geeksforgeeks.org/python-program-for-basic-and-extended-euclidean-algorithms-2/
def gcdExtended(a, b): 
    # Base Case 
    if a == 0 : 
        return b,0,1
             
    gcd,x1,y1 = gcdExtended(b%a, a) 
     
    # Update x and y using results of recursive 
    # call 
    x = y1 - (b//a) * x1 
    y = x1 
     
    return gcd,x,y 

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