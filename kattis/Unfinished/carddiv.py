def sum_digits3(n):
   r = 0
   while n:
       r, n = r + n % 10, n // 10
   return r

n, m = map(int, ma)
x = "".join(str(i) for i in range(n, m + 1))

print(sum_digits3(int(x)))