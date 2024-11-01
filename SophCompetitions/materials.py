from queue import Queue
from math import ceil
total = {}
def craft_search(start, initial_value, recipes, returns, materials):
    Q = Queue()
    Q.put((start, initial_value))
    while not Q.empty:
        name, value = Q.get()
        if name in materials:
            total[name] += value
        else:
            for material in recipes[start]:
                subvalue, subname = material
                needed = ceil((int(subvalue) * value) / returns[name])
                Q.put(subname, needed)

    

for i in range(int(input())):
    name = input()
    m, r, p =map(int, input().split())
    materials = set()
    recipes, returns = {}, {}
    built = [None for _ in range(p)]
    for _ in range(m):
        raw = input()
        materials.add(raw)
        total[raw] = 0
    for _ in range(r):
        into, outto = input().split(">")
        outtonum, outtoname = outto
        recipes[outtoname] = into.split(",")
        returns[outtoname] = int(outtonum)
    running_total = 0
    for b in range(p):
        num_build, name_build = input().split()
        craft_search(name_build, num_build, recipes, returns, materials)
    
    print(name)
    for rawmat in materials:
        print("\t" + str(total[rawmat]), rawmat)