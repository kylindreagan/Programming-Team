import sys
import math
from collections import defaultdict, Counter

def normalize(a, b, c):
    gcd = math.gcd(int(a), int(b))
    if gcd != 0:
        a //= gcd
        b //= gcd
    
    # Canonicalize: make first non-zero positive
    if a < 0 or (a == 0 and b < 0):
        a, b, c = -a, -b, -c
    
    return a, b, c

def perpendicular_dir(a, b):
    # Perpendicular is (-b, a) 
    a2, b2 = -b, a
    # Canonicalize
    if a2 < 0 or (a2 == 0 and b2 < 0):
        a2, b2 = -a2, -b2
    return a2, b2

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    idx = 1
    
    # Group lines by normalized direction
    dir_to_lines = defaultdict(list)  # (a,b) -> list of c values
    
    for _ in range(n):
        x1, y1, x2, y2 = map(int, input_data[idx:idx+4])
        idx += 4
        
        # (y2-y1)x - (x2-x1)y + (x2-x1)y1 - (y2-y1)x1 = 0
        A = y2 - y1
        B = -(x2 - x1)
        C = (x2 - x1) * y1 - (y2 - y1) * x1
        
        if A == 0 and B == 0:
            continue  # Should not happen as points are distinct
        
        # Reduce by GCD to keep integers
        gcd = math.gcd(A, B)
        if gcd != 0:
            A //= gcd
            B //= gcd
            C //= gcd
        
        # Canonicalize: make first non-zero positive
        if A < 0 or (A == 0 and B < 0):
            A, B, C = -A, -B, -C
        
        dir_to_lines[(A, B)].append(C)
    
    for direction in dir_to_lines:
        dir_to_lines[direction].sort()
    
    # Build map from direction to its perpendicular direction
    dir_to_perp = {}
    directions = list(dir_to_lines.keys())
    
    for A, B in directions:
        # Perpendicular direction is (B, -A) or normalized
        perp = perpendicular_dir(A, B)
        # Check if perpendicular direction exists in our lines
        if perp in dir_to_lines:
            dir_to_perp[(A, B)] = perp
    
    # Count distances for each direction
    total_squares = 0
    processed_pairs = set()
    
    for direction1 in directions:
        if direction1 not in dir_to_perp:
            continue
            
        direction2 = dir_to_perp[direction1]
        
        # Avoid double counting (d1,d2) and (d2,d1)
        pair_key = tuple(sorted([direction1, direction2]))
        if pair_key in processed_pairs:
            continue
        processed_pairs.add(pair_key)
        
        lines1 = dir_to_lines[direction1]
        lines2 = dir_to_lines[direction2]
        
        # Count distances in direction1
        dist_count1 = Counter()
        m1 = len(lines1)
        for i in range(m1):
            for j in range(i + 1, m1):
                # For normalized lines ax+by+c=0 with a²+b²=1, distance is |c2-c1|
                # But we're using integer coefficients, so we need to normalize
                dist = abs(lines1[j] - lines1[i])
                dist_count1[dist] += 1
        
        # Count distances in direction2
        dist_count2 = Counter()
        m2 = len(lines2)
        for i in range(m2):
            for j in range(i + 1, m2):
                dist = abs(lines2[j] - lines2[i])
                dist_count2[dist] += 1
        
        # Intersect distances
        for dist in set(dist_count1.keys()) & set(dist_count2.keys()):
            total_squares += dist_count1[dist] * dist_count2[dist]
    
    print(total_squares)

if __name__ == "__main__":
    solve()