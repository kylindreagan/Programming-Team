import sys

for line in sys.stdin:
    if not line.strip():
        continue
    a, b, c = map(int, line.split())
    integer_part = a // b
    remainder = a % b
    fractional_digits = []
    
    for _ in range(c):
        remainder *= 10
        digit = remainder // b
        fractional_digits.append(str(digit))
        remainder = remainder % b
    print(f"{integer_part}.{''.join(fractional_digits)}")