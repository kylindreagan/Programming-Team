import sys

def get_safe_integer_aabb(points):
    if not points:
        return None
    
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    
    has_min_x = any(p[0] == min_x for p in points)
    has_max_x = any(p[0] == max_x for p in points)
    has_min_y = any(p[1] == min_y for p in points)
    has_max_y = any(p[1] == max_y for p in points)
    
    left   = min_x - 1 if has_min_x else min_x
    right  = max_x + 1 if has_max_x else max_x
    bottom = min_y - 1 if has_min_y else min_y
    top    = max_y + 1 if has_max_y else max_y
    
    corners = [(left, bottom), (right, bottom), (right, top), (left, top)]
    perm = (right - left) * 2 +  (top - bottom) * 2
    return perm


points = []
for i in range(int(input())):
    x,y = map(int, input().split())
    points.append((x,y))
perm = get_safe_integer_aabb(points)
print(perm)