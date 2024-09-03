def grid_based_area(circles, gridsize=100):
    min_x = min(circle[0] - circle[2] for circle in circles)
    max_x = max(circle[0] + circle[2] for circle in circles)
    min_y = min(circle[1] - circle[2] for circle in circles)
    max_y = max(circle[1] + circle[2] for circle in circles)

    x_range = max_x - min_x
    y_range = max_y - min_y

    x_resolution = int(x_range * gridsize)
    y_resolution = int(y_range * gridsize)

    width = x_range / x_resolution
    height = y_range / y_resolution

    covered = [[False for _ in range(y_resolution)] for _ in range(x_resolution)]

    for xi, yi, ri in circles:
        for i in range(x_resolution):
            for j in range(y_resolution):
                x = min_x + i * width
                y = min_y + j * height
                if (x - xi)**2 + (y-yi)**2 <= ri**2:
                    covered[i][j] = True
    

    covered_total = sum(sum(row) for row in covered)
    return (covered_total * width * height)

ufos = int(input())
crop_circles = [tuple(map(int, input().split())) for _ in range(ufos)]
net_area = grid_based_area(crop_circles)
print(net_area)