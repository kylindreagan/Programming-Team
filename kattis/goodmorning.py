#old code
import sys

global num
num = [[1,2,3],[4,5,6],[7,8,9],[-1,0,-1]]


def findIndex(first):
    for a in range(4):
        for b in range(3):
            if num[a][b] == first:
                return [a, b]
    return [9,9]


def getPosibilites(i,j,strMin):
    a = num[i][j]
    ls = [a]
    if i+1<4:
        b = num[i+1][j]
        if b==-1:
            ls.append(b)
    if j+1<3:
        c = num[i][j+1]
        if c == -1:
            ls.append(c)
    if i+1<4 and j+1<3:
        d = num[i+1][j+1]
        if d == -1:
            ls.append(d)
    return ls

def getClosest(posi, strMin, index):
    current = int(strMin[:index+1])
    acum = strMin[:index]
    a = [int(acum+str(p)) if p > 0 else int(acum+str(0)) for p in posi]
    closest = sys.maxsize
    for s in a:
        if abs(current-s)<abs(current-closest):
            closest=s
    return closest


def solution(min):
    strMin = str(min)
    a = int(strMin[0])
    currentNumber = str(a)
    for index in range(1,len(str(min))):
        i,j = findIndex(a)
        a = int(strMin[index])
        k,s = findIndex(a)
        if i<=k and j<=s:
            currentNumber+=str(a)
        else:
            posi = getPosibilites(i,j,strMin)
            currentNumber=getClosest(posi,strMin,index)
        i,j=k,s
    return currentNumber

for _ in range(int(input())):
    min = int(input())
    print(solution(min))