import decimal

for i in range(int(input())):
    r, b, m = [decimal.Decimal(s) for s in input().split()]
    og_b = b
    r /= 100
    r += 1
    paid = False
    
    if m <= b * (r - 1):
        print("impossible")
        continue

    for j in range(1,1201):
        b = b*r-m
        b = b.quantize(decimal.Decimal('.01'), rounding = decimal.ROUND_HALF_UP)
        if b <= 0:
            print(j)
            paid=True
            break
    
    if not paid:
        print("impossible")