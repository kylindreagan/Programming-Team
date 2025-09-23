from decimal import Decimal, ROUND_HALF_UP
# Used to hold details of a point
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
# The objects that we want stored in the quadtree
class Node:
    def __init__(self, pos, shape_type, color, size):
        self.pos = pos           # Position (center for circles, top-left for squares)
        self.shape_type = shape_type  # "circle" or "square"
        self.color = color       # Color of the shape
        self.size = size         # Radius for circles, side length for squares

    # Check if a point is inside this shape
    def contains_point(self, p):
        if self.shape_type == "CIRCLE":
            return ((p.x - self.pos.x) ** 2 + (p.y - self.pos.y) ** 2) <= self.size ** 2
        elif self.shape_type == "SQUARE":
            return (self.pos.x <= p.x <= self.pos.x + self.size and 
                    self.pos.y <= p.y <= self.pos.y + self.size)
        return False
   
    # Check if a point is on the boundary of this shape
    def on_boundary(self, p):
        if self.shape_type == "CIRCLE":
            # Point is on boundary if distance from center is exactly equal to the radius
            distance_to_center = ((p.x - self.pos.x) ** 2 + (p.y - self.pos.y) ** 2) ** 0.5
            return abs(distance_to_center - self.size) < 1e-6  # Tolerance for floating-point precision

        elif self.shape_type == "SQUARE":
            # Point is on boundary if it lies on any of the square's edges
            on_left_or_right_edge = (self.pos.x == p.x or self.pos.x + self.size == p.x) and (self.pos.y <= p.y <= self.pos.y + self.size)
            on_top_or_bottom_edge = (self.pos.y == p.y or self.pos.y + self.size == p.y) and (self.pos.x <= p.x <= self.pos.x + self.size)
            return on_left_or_right_edge or on_top_or_bottom_edge
 
# The main quadtree class
class Quad:
    def __init__(self, topL, botR):
        self.topLeft = topL
        self.botRight = botR
        self.nodes = []
        self.topLeftTree = None
        self.topRightTree = None
        self.botLeftTree = None
        self.botRightTree = None
        self.capacity = 4   # Max nodes per quad before subdivision
 
    # Insert a node into the quadtree
    def insert(self, node):
        if node is None or not self.inBoundary(node.pos):
            return

        # If capacity is not reached, add node here
        self.nodes.append(node)

    def subdivide(self):
        x_mid = (self.topLeft.x + self.botRight.x) / 2
        y_mid = (self.topLeft.y + self.botRight.y) / 2

        self.topLeftTree = Quad(self.topLeft, Point(x_mid, y_mid))
        self.topRightTree = Quad(Point(x_mid, self.topLeft.y), Point(self.botRight.x, y_mid))
        self.botLeftTree = Quad(Point(self.topLeft.x, y_mid), Point(x_mid, self.botRight.y))
        self.botRightTree = Quad(Point(x_mid, y_mid), self.botRight)
    
    def search(self, p):
        if not self.inBoundary(p):
            return []  # No shapes if point is outside the boundary

        found_nodes = []
        for node in self.nodes:
            if node.contains_point(p):
                found_nodes.append(node)

        return found_nodes

    # Check if point p is within the boundaries of this quad
    def inBoundary(self, p):
        return (self.topLeft.x <= p.x <= self.botRight.x and
                self.topLeft.y <= p.y <= self.botRight.y)

def average_rgb(shapes):
    # Initialize cumulative sums for red, green, and blue components
    total_r, total_g, total_b = 0, 0, 0
    num_shapes = 0

    for s in shapes:
        # Skip processing if shape is on boundary or black (0, 0, 0)
        if s.on_boundary(p):
            return (0, 0, 0)  # Return black immediately if condition is met

        # Add the color values to the cumulative sum
        total_r += s.color[0]
        total_g += s.color[1]
        total_b += s.color[2]
        num_shapes += 1

    if num_shapes == 0:
        return (255, 255, 255)  # If no shapes were found, return white

    # Calculate the average color
    avg_r = int(Decimal(total_r / num_shapes).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
    avg_g = int(Decimal(total_g / num_shapes).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
    avg_b = int(Decimal(total_b / num_shapes).quantize(Decimal('1'), rounding=ROUND_HALF_UP))


    # Clamp the result to the 0-255 range (if needed)
    avg_r = min(max(avg_r, 0), 255)
    avg_g = min(max(avg_g, 0), 255)
    avg_b = min(max(avg_b, 0), 255)

    return (avg_r, avg_g, avg_b)

N = int(input())
for n in range(N):
    QT = Quad(Point(-1000, -1000), Point(1000, 1000))
    objects, points = map(int, input().split())
    for i in range(objects):
        #px, py = point of center for circle and of lower left corner for square
        name, px, py, length, r, g, b = input().split()
        px, py = float(px), float(py)
        color = (int(r), int(g), int(b))
        shape = Node(Point(px,py), name, color, float(length))
        QT.insert(shape)
        
    print(f"Case {n+1}:")
    for j in range(points):
        x, y = map(int, input().split())
        p = Point(x,y)
        shapes = QT.search(p)
        point_rgb = average_rgb(shapes)
        print(f"({point_rgb[0]}, {point_rgb[1]}, {point_rgb[2]})")
    if n != N - 1:
        print()