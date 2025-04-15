import re

for i in range(int(input())):
    x,y = map(int, input().split())
    aquarium="\n".join([input() for _ in range(x)])
    flounder = r'><\(+">|<"\}+><|><\{+">|<"\)+><'
    koi = r'><\(+\*>|<\*\}+><|><\{+\*>|<\*\)+><'
    trout = r"><\(+'>|<'\}+><|><\{+'>|<'\)+><"
    total = 0
    print(len(re.findall(f'(?={flounder})', aquarium)), len(re.findall(f'(?={koi})', aquarium)), len(re.findall(f'(?={trout})', aquarium)))