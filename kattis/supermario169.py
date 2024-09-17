import math
import heapq

class Node:
    def  __init__(self,x=0,y=0,z=0):
        self._x = x
        self._y = y
        self._z = z
        self._locked = False
        
    def __eq__(self, other):
        return isinstance(other, Node) and self._x == other._x and self._y == other._y and self._z == other._z

    def __hash__(self):
        return hash((self._x, self._y, self._z))
    
    def __repr__(self):
        return f"({self._x}, {self._y}, {self._z})"
    
    def __getitem__(self, index):
        if index == 0:
            return self._x
        elif index == 1:
            return self._y
        elif index == 2:
            return self._z
        else:
            raise IndexError("Index out of range")
    
    def is_key(self):
        return False

class KeyNode(Node):
    def __init__(self, x=0,y=0,z=0, vals=set()):
        super().__init__(x,y,z)
        self._vals = vals
    
    def add(self, newVal):
        self._vals.add(newVal)
    
    def is_key(self):
        return True

class LockNode(Node):
    def __init__(self, x=0,y=0,z=0, key=KeyNode()):
        super().__init__(x,y,z)
        self._locked = True
    
    def unlock(self):
        self._locked = False
    
    def lock(self):
        self._locked = True

#Helper function to compute the Euclidean distance between two points in 3D space
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)

# Nearest Neighbor TSP function
def nearest_neighbor_tsp(points, start_index, n):
    visited = [False] * n
    visited[start_index] = True
    path = [start_index]  # Start the path with the start node
    total_distance = 0
    current_index = start_index

    for _ in range(n - 1):  # We need to visit all nodes
        nearest_distance = float('inf')
        nearest_index = None

        # Find the nearest unvisited node
        for neighbor_index in range(n):
            if not visited[neighbor_index]:
                neighbor = points[neighbor_index]
                distance = euclidean_distance(points[current_index], neighbor)
                if distance < nearest_distance and not neighbor._locked:
                    nearest_distance = distance
                    nearest_index = neighbor_index
        
        
        if nearest_index is None:
            break  # No valid nearest neighbor, exit the loop

        # Visit the nearest node
        visited[nearest_index] = True
        path.append(nearest_index)
        near_node = points[nearest_index]
        if near_node.is_key():
            for lock_node in near_node._vals:
                lock_node.unlock()
                
        total_distance += nearest_distance
        current_index = nearest_index

    # Return to the starting node to complete the cycle
    total_distance += euclidean_distance(points[current_index], points[start_index])
    path.append(start_index)

    return path, total_distance


switches, mx, my, mz = map(int, input().split())

start = Node(mx,my,mz)
total_nodes = [start]
running_total = switches

for _ in range(switches):
    coins, sx, sy, sz = map(int, input().split())
    if coins == 0:
        continue
    running_total += coins
    coin_set = set()
    for _ in range(coins):
        cx,cy,cz = map(int, input().split())
        temp_coin = LockNode(cx,cy,cz)
        coin_set.add(temp_coin)
        total_nodes.append(temp_coin)
    temp_switch = KeyNode(sx,sy,sz,coin_set)
    total_nodes.append(temp_switch)

path, traveled = nearest_neighbor_tsp(total_nodes, 0, running_total)

print(traveled)