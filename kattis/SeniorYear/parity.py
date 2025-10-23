while True:
    bits = input().strip()
    if bits == '#':
        break
    if not bits:
        continue
    lastchr = bits[-1]
    bits = bits[:-1]

    if lastchr == 'e' and bits.count('1')%2==0:
        print(bits+'0')
    elif lastchr == 'e':
        print(bits+'1')
    elif bits.count('1')%2==0:
        print(bits+'1')
    else:
        print(bits+'0')