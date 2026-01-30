from dataclasses import dataclass
import heapq
from math import isclose
from collections import defaultdict

EPS = 1e-9

@dataclass(frozen=True, order=True)
class Point:
    x: float
    y: float

@dataclass
class Segment:
    p: Point
    q: Point
    id: int

def normalize(seg):
    if (seg.p.x, seg.p.y) <= (seg.q.x, seg.q.y):
        return seg
    return Segment(seg.q, seg.p, seg.id)

def orient(a, b, c):
    return (b.x - a.x)*(c.y - a.y) - (b.y - a.y)*(c.x - a.x)

def on_segment(a, b, c):
    return (min(a.x, b.x) - EPS <= c.x <= max(a.x, b.x) + EPS and
            min(a.y, b.y) - EPS <= c.y <= max(a.y, b.y) + EPS)

def segments_intersect(s1, s2):
    a, b = s1.p, s1.q
    c, d = s2.p, s2.q

    o1 = orient(a, b, c)
    o2 = orient(a, b, d)
    o3 = orient(c, d, a)
    o4 = orient(c, d, b)

    if o1*o2 < 0 and o3*o4 < 0:
        return True

    if isclose(o1, 0) and on_segment(a, b, c): return True
    if isclose(o2, 0) and on_segment(a, b, d): return True
    if isclose(o3, 0) and on_segment(c, d, a): return True
    if isclose(o4, 0) and on_segment(c, d, b): return True

    return False

def intersection_point(s1, s2):
    x1, y1 = s1.p.x, s1.p.y
    x2, y2 = s1.q.x, s1.q.y
    x3, y3 = s2.p.x, s2.p.y
    x4, y4 = s2.q.x, s2.q.y

    den = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)
    if isclose(den, 0):
        return None  # parallel or collinear

    px = ((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4)) / den
    py = ((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4)) / den
    return Point(px, py)

LEFT, RIGHT, INTER = 0, 1, 2

@dataclass(order=True)
class Event:
    x: float
    kind: int
    y: float
    seg1: Segment
    seg2: Segment = None

class SweepStatus:
    def __init__(self):
        self.segs = []

    def y_at(self, seg, x):
        if isclose(seg.p.x, seg.q.x):
            return seg.p.y
        t = (x - seg.p.x) / (seg.q.x - seg.p.x)
        return seg.p.y + t*(seg.q.y - seg.p.y)

    def insert(self, seg, x):
        y = self.y_at(seg, x)
        i = 0
        while i < len(self.segs) and self.y_at(self.segs[i], x) < y:
            i += 1
        self.segs.insert(i, seg)
        return i

    def remove(self, seg):
        self.segs.remove(seg)

    def neighbors(self, i):
        below = self.segs[i-1] if i > 0 else None
        above = self.segs[i+1] if i+1 < len(self.segs) else None
        return below, above

def bentley_ottmann(segments):
    segments = [normalize(s) for s in segments]
    events = []
    intersections = set()

    for s in segments:
        events.append(Event(s.p.x, LEFT, s.p, s))
        events.append(Event(s.q.x, RIGHT, s.q, s))

    heapq.heapify(events)
    status = SweepStatus()
    seen = set()

    while events:
        e = heapq.heappop(events)
        x = e.x

        if e.kind == LEFT:
            i = status.insert(e.seg1, x)
            for nb in status.neighbors(i):
                if nb and segments_intersect(e.seg1, nb):
                    p = intersection_point(e.seg1, nb)
                    if p and (p.x, p.y) not in seen and p.x >= x - EPS:
                        seen.add((p.x, p.y))
                        intersections.add(p)
                        heapq.heappush(events,
                            Event(p.x, INTER, p, e.seg1, nb))

        elif e.kind == RIGHT:
            i = status.segs.index(e.seg1)
            below, above = status.neighbors(i)
            status.remove(e.seg1)
            if below and above and segments_intersect(below, above):
                p = intersection_point(below, above)
                if p and (p.x, p.y) not in seen and p.x >= x - EPS:
                    seen.add((p.x, p.y))
                    intersections.add(p)
                    heapq.heappush(events,
                        Event(p.x, INTER, p, below, above))

        else:  # INTERSECTION
            s1, s2 = e.seg1, e.seg2
            i1 = status.segs.index(s1)
            i2 = status.segs.index(s2)
            if i1 > i2:
                i1, i2 = i2, i1

            status.segs[i1], status.segs[i2] = status.segs[i2], status.segs[i1]

            for seg, nb in [(s1, status.neighbors(i2)[1]),
                            (s2, status.neighbors(i1)[0])]:
                if nb and segments_intersect(seg, nb):
                    p = intersection_point(seg, nb)
                    if p and (p.x, p.y) not in seen and p.x >= x - EPS:
                        seen.add((p.x, p.y))
                        intersections.add(p)
                        heapq.heappush(events,
                            Event(p.x, INTER, p, seg, nb))

    return intersections

def split_segments(segments, intersections):
    points_on = defaultdict(list)

    for s in segments:
        points_on[s.id].extend([s.p, s.q])

    for p in intersections:
        for s in segments:
            if on_segment(s.p, s.q, p):
                points_on[s.id].append(p)

    edges = set()

    for s in segments:
        pts = points_on[s.id]

        def param(p):
            if abs(s.p.x - s.q.x) >= abs(s.p.y - s.q.y):
                return (p.x - s.p.x) / (s.q.x - s.p.x + EPS)
            else:
                return (p.y - s.p.y) / (s.q.y - s.p.y + EPS)

        pts = sorted(set(pts), key=param)

        for i in range(len(pts)-1):
            if pts[i] != pts[i+1]:
                edges.add((pts[i], pts[i+1]))

    return edges

def build_graph(edges):
    adj = defaultdict(set)
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    return adj

def area2(a, b, c):
    return abs((b.x-a.x)*(c.y-a.y) - (b.y-a.y)*(c.x-a.x))

def find_triangles(adj):
    triangles = set()
    vertices = list(adj.keys())

    for u in vertices:
        for v in adj[u]:
            if u >= v:
                continue
            common = adj[u] & adj[v]
            for w in common:
                if v >= w:
                    continue
                if area2(u, v, w) > EPS:
                    triangles.add(tuple(sorted([u, v, w])))
    return triangles

while True:
    n = int(input())
    if n == 0:
        break
    segments = []
    for i in range(n):
        x1, y1, x2, y2 = map(float, input().split())
        p = Point(x1, y1)
        q = Point(x2, y2)
        segments.append(Segment(p, q, i))
    intersections = bentley_ottmann(segments)
    edges = split_segments(segments, intersections)
    adj = build_graph(edges)
    triangles = find_triangles(adj)
    print(len(triangles))