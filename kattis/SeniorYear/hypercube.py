def pos(code):
    if len(code) == 0:
        return 0
    if code[0]=='0':
        return pos(code[1:])
    return (1 << len(code)) - 1 - pos(code[1:])

n, a, b = input().split()
print(abs(pos(b)-pos(a))-1)