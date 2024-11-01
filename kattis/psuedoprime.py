from math import sqrt

#https://www.geeksforgeeks.org/check-if-a-number-is-fermat-pseudoprime/
# Function to check if the given number is composite
def checkcomposite(n):
     
    # Check if there is any divisor of n less than sqrt(n)
    for i in range(2,int(sqrt(n))+1,1):
        if (n % i == 0):
            return 1
    return 0

def power(x, y, mod):
    # Initialize result
    res = 1
 
    while (y):
        # If power is odd, then update the answer
        if (y & 1):
            res = (res * x) % mod
 
        # Square the number and reduce
        # the power to its half
        y = y >> 1
        x = (x * x) % mod
 
    # Return the result
    return res

while True:
    p, a = map(int, input().split())
    if a == p == 0:
        break
    if (checkcomposite(p) and power(a,p,p)==a):
        print("yes")
    else:
        print("no")
    