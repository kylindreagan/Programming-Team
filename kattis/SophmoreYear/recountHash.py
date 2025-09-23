def hashDict(l):
    hashTable = {}
    for i in range(len(l)):
        hashTable[i] = None
    
    return hashTable

candidates = []
while True:
    name = input()
    if name == "***":
        break
    else:
        candidates.append(name)

