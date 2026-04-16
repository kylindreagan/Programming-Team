T = int(input())
recordDict = {}

for T in range(T):
    teamRec = input().split()
    teamName = teamRec.pop(0)
    winloss = teamRec.pop(0)
    win = int(winloss[0])
    loss = int(winloss[2])
    total = 0
    for j in teamRec:
        total += int(j)
    eloEquation = (total+400 * (win-loss)) / len(teamRec)
    test = str(int((eloEquation * 1000)//1))
    if test[-1] == "5" and int(test[-2])%2 == 0:
        eloEquation += .005
    recordDict[teamName] = "{:.2f}".format(eloEquation)

eloSort = sorted(recordDict.items(), key=lambda x:x[1], reverse=True)

for m in range(len(recordDict)):
    print(str(m+1) + ")", eloSort[m][0], eloSort[m][1])