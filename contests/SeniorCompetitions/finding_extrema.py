# CCSC 2025 #6: Finding Extrema
# --> Calculus
#Written by Kylind and Nyugen

from math import sqrt, ceil, floor
def f(x):
    return x**3 - 5*x**2 + 5*x + 2
for i in range(int(input())):
    a, b, n = map(float, input().split())
    s = (b-a)/n
    cps = [(f(a),a), (f(b),b)]
    x1 = (5 + sqrt(10))/3
    x2 = (5 - sqrt(10))/3
    if a <= x1 <= b:
        x1f = floor((x1 - a)/s)*s+a
        x1c = ceil((x1 - a)/s)*s+a
        if a <= x1f <= b:
            cps.append((f(x1f),x1f))
        if a <= x1c <= b:
            cps.append((f(x1c),x1c))
    if a <= x2 <= b:
        x2f = floor((x2 - a)/s)*s+a
        x2c = ceil((x2 - a)/s)*s+a
        if a <= x2f <= b:
            cps.append((f(x2f),x2f))
        if a <= x2c <= b:
            cps.append((f(x2c),x2c))
    cps.sort()
    print(f"case {i+1}, minimum of {cps[0][0]:.1f} at x={cps[0][1]:.1f}, maximum of {cps[-1][0]:.1f} at x={cps[-1][1]:.1f}")