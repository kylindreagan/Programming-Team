EPSILON = 1e-9
def orientation(p, q, r):
    """
    Returns:
    0: collinear
    1: clockwise  
    2: counterclockwise
    """
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    
    if abs(val) < EPSILON: 
        return 0
    return 1 if val > 0 else 2

def on_segment(p, q, r):
    return (min(p[0], r[0]) - EPSILON <= q[0] <= max(p[0], r[0]) + EPSILON and
            min(p[1], r[1]) - EPSILON <= q[1] <= max(p[1], r[1]) + EPSILON)

def intersect(seg1, seg2):
    p1, p2 = seg1
    q1, q2 = seg2 
    
    def eq(a, b):
        return abs(a - b) < EPSILON
    
    # Check for identical endpoints
    if (eq(p1[0], q1[0]) and eq(p1[1], q1[1])) or \
       (eq(p1[0], q2[0]) and eq(p1[1], q2[1])) or \
       (eq(p2[0], q1[0]) and eq(p2[1], q1[1])) or \
       (eq(p2[0], q2[0]) and eq(p2[1], q2[1])):
        return True
    
    # Find the four orientations
    o1 = orientation(p1, p2, q1)
    o2 = orientation(p1, p2, q2)
    o3 = orientation(q1, q2, p1)
    o4 = orientation(q1, q2, p2)
    
    # General case: segments intersect if orientations differ
    if o1 != o2 and o3 != o4:
        return True
    
    # Special cases (collinear points)
    if o1 == 0 and on_segment(p1, q1, p2):
        return True
    if o2 == 0 and on_segment(p1, q2, p2):
        return True
    if o3 == 0 and on_segment(q1, p1, q2):
        return True
    if o4 == 0 and on_segment(q1, p2, q2):
        return True
    
    return False

def get_intersection(seg1, seg2, eps=1e-9):
    p1, p2 = seg1
    p3, p4 = seg2
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4
    
    dx1 = x2 - x1
    dy1 = y2 - y1
    dx2 = x4 - x3
    dy2 = y4 - y3
    
    cross = dx1 * dy2 - dy1 * dx2
    
    if abs(cross) < eps:
        return None
    
    # Using Cramer's rule
    det = cross 
    dx = x3 - x1
    dy = y3 - y1
    
    t = (dx * dy2 - dy * dx2) / cross
    u = (dx * dy1 - dy * dx1) / cross
    
    if -eps <= t <= 1 + eps and -eps <= u <= 1 + eps:
        ix = x1 + t * dx1
        iy = y1 + t * dy1
        return (ix, iy)
    
    return None

def count_triangles(segments):
    n = len(segments)
    intersections = [[] for _ in range(n)]
    
    for i in range(n):
        for j in range(i+1, n):
            if intersect(segments[i], segments[j]):
                intersections[i].append(j)
                intersections[j].append(i)
    
    count = 0
    for a in range(n):
        for b in intersections[a]:
            if b > a:
                for c in intersections[b]:
                    if c > b and c in intersections[a]:
                        p1 = get_intersection(segments[a], segments[b])
                        p2 = get_intersection(segments[b], segments[c])
                        p3 = get_intersection(segments[c], segments[a])
                        if distinct(p1, p2, p3):
                            count += 1
    
    return count

def distinct(p1, p2, p3, eps=1e-9):
    if p1 is None or p2 is None or p3 is None:
        return False
    
    if abs(p1[0] - p2[0]) < eps and abs(p1[1] - p2[1]) < eps:
        return False
    
    if abs(p2[0] - p3[0]) < eps and abs(p2[1] - p3[1]) < eps:
        return False
    
    if abs(p1[0] - p3[0]) < eps and abs(p1[1] - p3[1]) < eps:
        return False
    
    return True

while True:
    n = int(input())
    if n == 0:
        break
    segments = []
    for i in range(n):
        x1, y1, x2, y2 = map(float, input().split())
        segments.append(((x1, y1), (x2, y2)))
    print(count_triangles(segments))