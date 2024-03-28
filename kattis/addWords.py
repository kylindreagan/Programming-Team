try:
    d, ops = {}, {"+", "-"}
    while True:
        strCode = input()
        code = strCode.split()
        if code[0] == "clear":
            d = {}
        elif code[0] == "def":
            d[code[1]] = code[2]
        elif code[0] == "calc":
            code.pop(0)
            strCode = strCode[5:]
            answer = 0
            if code[0] in d.keys():
                answer += int(d[code.pop(0)])
                for i in code:
                    if i == "=":
                        break
                    if i in ops:
                        x = i
                    elif i not in d.keys():
                        answer = ["unknown"]
                        break
                    else:
                        comp = str(answer) + " " + x + " " + d[i]
                        answer = eval(comp)
                if str(answer) not in d.values():
                    answer = ["unknown"]
                else:
                    answer = [i for i in d if d[i]==str(answer)]
            else:
                answer = ["unknown"]
            print(strCode, answer[0])
except EOFError:
    quit()