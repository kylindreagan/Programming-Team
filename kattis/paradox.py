for _ in range(int(input())):
    input()
    NCS, NEc = map(int, input().split())
    CSStudents,EcStudents = [int(x) for x in input().split()],[int(y) for y in input().split()]
    CSIQ = sum(CSStudents) / NCS
    EcIQ = sum(EcStudents) / NEc
    count = 0
    for i in CSStudents:
        if  i < CSIQ and i > EcIQ:
            count += 1
    print(count)