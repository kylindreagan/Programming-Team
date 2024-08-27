T = int(input())
gradesDict = {"A":4.0, "B+":3.5, "B":3.0,"C+":2.5,"C":2,"D":1,"F":0,"S":0,"U":0}
hoursDict = {}
GPADict = {}

for i in range(T):
    name, classes = map(str, input().split())
    classes = int(classes)
    qualityHours = 0
    totalHours = 0
    FHours = 0
    SHours = 0
    for j in range(classes):
        className, grade, credithours = map(str, input().split())
        credithours = int(credithours)
        if grade == "U" or grade == "S":
            if grade == "S":
                SHours += credithours
        else: 
            totalHours += credithours
            qualityHours += gradesDict[grade] * credithours
        if grade == "F":
            FHours += credithours
    GPADict[name] = "{:.2f}".format(qualityHours / totalHours)
    hoursDict[name] = totalHours - FHours + SHours

for name in hoursDict.keys():
    print(name, "has earned", hoursDict[name], "hours with a GPA of", GPADict[name])
