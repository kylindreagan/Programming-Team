# CCSC 2025 #9: Eight Bit Interpreter
# --> Use ASCII chars
#Written by Kylind

s = ""
while 1:
    try:
        s += " ".join(input().split())
        s += " "
    except EOFError:
        break
message = ""
for ch in s.split():
    message += chr(int(ch, 2))
print(message)