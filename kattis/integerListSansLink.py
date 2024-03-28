import json

for i in range(int(input())):
    BAPC = input()
    deletes = BAPC.count("D")
    n = int(input())
    inputListStr = input()
    if deletes > n:
        print("error")
    elif deletes == n or n == 0:
        print("[]")
    elif deletes == 0:
        reverses = BAPC.count("R")
        if reverses % 2 == 0:
            print(inputListStr)
        else:
            print("[" + inputListStr[::-1].strip('[').strip(']') + "]")
    else:
        inputList = json.loads(inputListStr)
        for j in BAPC:
            if j == "R":
                inputList.reverse()
            else:
                inputList.pop(0)
                
    for i 
