#https://open.kattis.com/problems/rimski
import itertools

def intToRoman(num):
    num_map = [
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
        (1, "I")
    ]
    roman_num = ''
    for i, roman in num_map:
        count = num // i
        roman_num += roman * count
        num %= i
    return roman_num

def romanToInt(s):
    roman_map = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100}
    total = 0
    i = 0
    n = len(s)
    while i < n:
        if i+1 < n and roman_map[s[i]] < roman_map[s[i+1]]:
            total += roman_map[s[i+1]] - roman_map[s[i]]
            i += 2
        else:
            total += roman_map[s[i]]
            i += 1
    return total

valid_romans = set(intToRoman(i) for i in range(1, 101))

def smallestValidPerm(roman_str):
    perms = set(''.join(p) for p in itertools.permutations(roman_str))
    best_value = float('inf')
    best_perm = None
    
    for perm in perms:
        if perm in valid_romans:
            value = romanToInt(perm)
            if value < best_value:
                best_value = value
                best_perm = perm
    return best_perm

roman = input().strip()
result = smallestValidPerm(roman)
print(result)