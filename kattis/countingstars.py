from collections import deque

cases = 1

#https://www.geeksforgeeks.org/flood-fill-algorithm/
def floodFill(img, x, y, newClr):
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
            if x - 1 >= 0 and img[x - 1][y] == prevClr:
                img[x - 1][y] = newClr
                q.append((x - 1, y))
            if y + 1 < n and img[x][y + 1] == prevClr:
                img[x][y + 1] = newClr
                q.append((x, y + 1))
            if y - 1 >= 0 and img[x][y - 1] == prevClr:
                img[x][y - 1] = newClr
                q.append((x, y - 1))

while True:
    try:
        m,n = map(int, input().split())
        image = []
        for i in range(m):
            image.append(list(input()))

        newStar = "V"
        x,y = 0,0
        totalStars = 0
        while True:
            if not any('-' in sublist for sublist in image):
                break
            elif y > n-1:
                y = 0
                x += 1
            elif image[x][y] == '-':
                floodFill(image, x, y, newStar)
                totalStars += 1
                y += 1
            else:
                y += 1

        print("Case",str(cases) + ":", totalStars)
        cases += 1
    except EOFError:
        quit()