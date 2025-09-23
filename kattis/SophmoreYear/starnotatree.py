from math import*
from decimal import Decimal, ROUND_HALF_UP

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
# Test points. These points are the left,
# up, right and down relative neighbours
# (arranged circularly) to the
# current_point at a distance of
# test_distance from current_point
#AKA- CIRCLE OF MAX DISTANCE
test_point = [Point(-10000, 0), 
              Point(0, 10000),
              Point( 10000, 0),
              Point(0, -10000)]
 
 
# Lowest Limit till which we are going
# to run the main while loop
# Lower the Limit higher the accuracy
lower_limit = 0.0000000000001
 
# Function to return the sum of Euclidean
# Distances
def distSum(p, arr, n):
    sum = 0
    for i in range(n):
        distx = abs(arr[i].x - p.x)
        disty = abs(arr[i].y - p.y)
        sum = sum + sqrt((distx * distx) + (disty * disty))
 
    # Return the sum of Euclidean Distances
    return sum
 
 
# Function to calculate the required
# geometric median
def geometricMedian(arr, n):
 
    # Current x coordinate and y coordinate
    current_point = Point(0, 0)
     
    for i in range(n):
        current_point.x = current_point.x + arr[i].x
        current_point.y = current_point.y + arr[i].y
 
         
    # Here current_point becomes the
    # Geographic MidPoint
    # Or Center of Gravity of equal
    # discrete mass distributions
    current_point.x = current_point.x / n
    current_point.y = current_point.y / n
 
    # minimum_distance becomes sum of
    # all distances from MidPoint to
    # all given points
    minimum_distance = distSum(current_point, arr, n)
 
    k = 0
    while (k < n):
        while(i < n and i != k):
            newpoint = Point(0, 0)
            newpoint.x = arr[i].x
            newpoint.y = arr[i].y
            newd = distSum(newpoint, arr, n)
            if newd < minimum_distance:
                minimum_distance = newd;
                current_point.x = newpoint.x
                current_point.y = newpoint.y
            i = i + 1
        k = k + 1
 
    # Assume test_distance to be 1000
    test_distance = 1000
    flag = 0
 
    # Test loop for approximation starts here
    while test_distance > lower_limit:
 
        flag = 0
 
        # Loop for iterating over all 4 neighbours
        for i in range(4):
 
            # Finding Neighbours done
            newpoint = Point(0,0)
            newpoint.x = current_point.x + test_distance * test_point[i].x
            newpoint.y = current_point.y + test_distance * test_point[i].y
 
            # New sum of Euclidean distances
            # from the neighbor to the given
            # data points
            newd = distSum(newpoint, arr, n)
 
            if newd < minimum_distance:
 
                # Approximating and changing
                # current_point
                minimum_distance = newd
                current_point.x = newpoint.x
                current_point.y = newpoint.y
                flag = 1
                break
 
        # This means none of the 4 neighbours
        # has the new minimum distance, hence
        # we divide by 2 and reiterate while
        # loop for better approximation
        if (flag == 0):
            test_distance = test_distance / 2
        
    return "{0:.6f}".format(minimum_distance)


N = int(input())
room = []
for i in range(N):
    cpuX, cpuY = map(int, input().split())
    room.append(Point(cpuX, cpuY))

print(geometricMedian(room, N))