from math import sqrt, acos, sin, pi
from itertools import combinations

def calculate_net_area(circles, n):
    total_area = sum(circle_area(r) for _, _, r in circles)
    overlap_area = 0

    # Inclusion-Exclusion Principle
    for k in range(2, n + 1):
        for comb in combinations(range(n), k):
            inter_area = float('inf')
            for i in range(k):
                for j in range(i + 1, k):
                    inter_area = min(inter_area, intersectionArea(
                        circles[comb[i]][0], circles[comb[i]][1], circles[comb[i]][2],
                        circles[comb[j]][0], circles[comb[j]][1], circles[comb[j]][2]
                    ))
            if inter_area > 0:
                if k % 2 == 0:
                    overlap_area += inter_area
                else:
                    overlap_area -= inter_area
    
    net_area = total_area - abs(overlap_area)
    return net_area


def circle_area(radius):
    return radius ** 2 * pi

def intersectionArea(X1, Y1, R1, X2, Y2, R2) :
    # Calculate the euclidean distance
    # between the two points
    d = sqrt(((X2 - X1) * (X2 - X1)) + ((Y2 - Y1) * (Y2 - Y1)));
 
    if d > R1 + R2 or d == R1 + R2:
        ans = 0
    
    elif X1 == X2 and Y1 == Y2 and R1 == R2:
        ans = circle_area(R1) #Perfect overlap
    
    elif d <= abs(R1 - R2):
        return pi * min(R1, R2) ** 2  # One circle is completely inside the other
 
    else :
        alpha = acos(((R1 * R1) + (d * d) - (R2 * R2)) / (2 * R1 * d)) * 2;
        beta = acos(((R2 * R2) + (d * d) - (R1 * R1)) / (2 * R2 * d)) * 2;
         
        a1 = (0.5 * beta * R2 * R2 ) - (0.5 * R2 * R2 * sin(beta));
        a2 = (0.5 * alpha * R1 * R1) - (0.5 * R1 * R1 * sin(alpha));
        ans = a1 + a2
 
    return ans

ufos = int(input())
crop_circles = [tuple(map(int, input().split())) for _ in range(ufos)]
net_area = calculate_net_area(crop_circles, ufos)
print(net_area)