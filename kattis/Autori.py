name = str(input())
hyphens = name.count("-")
firstLetter = name [0 : 1]
y = name.rfind("-")
lastLetter = name[y + 1 : y + 2]
N = hyphens
M = 1
hyphen = "-"
def find_nth(string, substring, n):
    start = string.find(substring)
    while start >= 0 and n > 1:
        start = string.find(substring, start+len(substring))
        n -= 1
    return start
if(hyphens == 1):
    print((firstLetter + lastLetter))
elif(hyphens == 0):
    print((firstLetter))
else:
    autori = ""
    while(N > 1):
        N -= 1
        n1 = find_nth(name, hyphen, M)
        letter = name[n1 + 1 : n1 + 2]
        M += 1
        autori = autori + letter
    final = (firstLetter + autori + lastLetter)
    print(final)