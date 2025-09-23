from collections import deque

#https://www.geeksforgeeks.org/flood-fill-algorithm/
def floodFill(img, x, y, newClr):
    coast = 0
    q = deque()

    # Rows and columns of the display
    m = len(img)
    n = len(img[0])

    prevClr = img[x][y]
    if prevClr == newClr:
        return

    # Append the position of the starting pixel 
    # of the component
    q.append((x, y))
    img[x][y] = newClr

    # While the queue is not empty, i.e., the whole 
    # component having prevClr color
    # is not colored with newClr color
    while q:
        # Dequeue the front node
        x, y = q.popleft()

        # Check if the adjacent pixels are valid and enqueue
        if x + 1 < m and img[x + 1][y] == prevClr:
            img[x + 1][y] = newClr
            q.append((x + 1, y))
        elif x + 1 < m and img[x + 1][y] == '1':
            coast += 1
        if x - 1 >= 0 and img[x - 1][y] == prevClr:
            img[x - 1][y] = newClr
            q.append((x - 1, y))
        elif x - 1 >= 0 and img[x - 1][y] == '1':
            coast += 1
        if y + 1 < n and img[x][y + 1] == prevClr:
            img[x][y + 1] = newClr
            q.append((x, y + 1))
        elif y + 1 < n and img[x][y + 1] == '1':
            coast += 1
        if y - 1 >= 0 and img[x][y - 1] == prevClr:
            img[x][y - 1] = newClr
            q.append((x, y - 1))
        elif y - 1 >= 0 and img[x][y - 1] == '1':
            coast += 1
    
    return coast

m,n = map(int, input().split())
image = [['0']*(n+2)]
for i in range(m):
    image.append(['0']+list(input())+['0'])
image.append(['0']*(n+2))

newPixel = "-1"
coast = floodFill(image,0,0,newPixel)
print(coast)