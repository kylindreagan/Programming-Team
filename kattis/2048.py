#n for columns; m for rows.
def duplicateCheckH(game, n):
    if game[n][0] == game[n][1] and game[n][2] == game[n][3] and game[n][0] == game[n][2]:
        return True
    else:
        return False
def duplicateCheckV(game,m):
    if game[0][m] == game[1][m] and game[2][m] == game[3][m] and game[0][m] == game[2][m]:
        return True
    else:
        return False
def rightMove(game):
    n = 0
    b = 0
    for i in range(4):
        m = 0
        if duplicateCheckH(game, n) == True:
            game[n][0] = 0
            game[n][1] = 0
            game[n][2] *= 2
            game[n][3] *= 2
            n += 1
        else:
            recentlyadded = False
            for j in range(3):
                if recentlyadded == True:
                    m += 1
                    recentlyadded = False
                else:
                    if game[n][m] == game[n][m+1]:
                        #DISTANCEEE CHECK!!
                        if m == 0 and game[n][m+2] == 0 and game[n][3] == game[n][1] and game[n][1] != 0:
                                game[n][3] *= 2
                                game[n][1] = game[n][0]
                                game[n][0] = 0
                                m += 1
                        elif m <= 1 and game[n][m+1] == game[n][m+2] and game[n][m+2] != 0:
                            game[n][m+1] *= 2
                            game[n][m+2] = 0
                            recentlyadded = True
                            m += 1
                        else:
                            game[n][m+1] *= 2
                            game[n][m] = 0
                            recentlyadded = True
                            m += 1
                    elif game[n][m+1] == 0:
                        #Proximity check!!
                        if (m == 0) and game[n][2] == game[n][3] and game[n][3] != 0:
                            game[n][3] *= 2
                            game[n][2] = 0
                            m += 1 
                        else:  
                            game[n][m+1]= game[n][m]
                            game[n][m] = 0
                            m += 1
                    else:
                        m += 1
            n += 1
def zeroRemoveR(game):
    n = 0
    for i in range(4):
        m = 0
        for i in range(3):
            if game[n][m+1] == 0:
                game[n][m+1]= game[n][m]
                game[n][m] = 0
                m += 1
            else:
                m += 1
        n += 1
def leftMove(game):
    n = 0
    for i in range(4):
        m = 0
        if duplicateCheckH(game, n) == True and game[m]!=[0, 0, 0, 0]:
            game[n][3] = 0
            game[n][2] = 0
            game[n][1] *= 2
            game[n][0] *= 2
            n += 1
        else:
            m = -1
            recentlyadded = False
            for j in range(3):
                if recentlyadded == True:
                    m -= 1
                    recentlyadded = False
                else:
                    if game[n][m] == game[n][m-1]:
                        if m == -1 and game[n][1] == 0 and game[n][0] == game[n][2] and game[n][0] != 0:
                            game[n][0] *= 2
                            game[n][-2] = game[n][-1]
                            game[n][-1] = 0
                            m -= 1
                        elif m >= -2 and game[n][m-1] == game[n][m-2] and game[n][m-1] != 0:
                            game[n][m-1] *= 2
                            game[n][m-2] = 0 
                            recentlyadded = True
                            m -= 1
                        else:
                            game[n][m-1] *= 2
                            game[n][m] = 0 
                            recentlyadded = True
                            m -= 1
                    elif game[n][m-1] == 0:
                        #PROXIMITY CHECK!!
                        if (m == -1) and game[n][0] == game[n][1] and game[n][0] != 0:
                            game[n][0] *= 2
                            game[n][1] = 0
                            m -= 1 
                        else: 
                            game[n][m-1]= game[n][m]
                            game[n][m] = 0
                            m -= 1
                    else:
                        m -= 1
            n += 1
def zeroRemoverL(game):
    n = 0
    for i in range(4):
        m = -1
        for i in range(3):
            if game[n][m-1] == 0:
                game[n][m-1]= game[n][m]
                game[n][m] = 0
                m -= 1
            else:
                m -= 1
        n += 1
def downMove(game):
    m = 0
    for i in range(4):
        recentlyadded = False
        n = 0
        if duplicateCheckV(game,m) == True:
            game[0][m] = 0
            game[1][m] = 0
            game[2][m] *= 2
            game[3][m] *= 2
            m += 1
        else:
            for j in range(3):
                if recentlyadded == True:
                    n += 1
                    recentlyadded = False
                else:    
                    if game[n][m] == game[n+1][m]:
                        #DISTANCE CHECK
                        if n == 0 and game[n+2][m] == 0 and game[3][m] == game[1][m] and game[3][m] != 0:
                            game[3][m] *= 2
                            game[1][m] = game[0][m]
                            game[0][m] = 0
                            n += 1
                        elif n <= 1 and game[n+1][m] == game[n+2][m] and game[n+1][m] != 0:
                            game[n+1][m] *= 2
                            game[n+2][m] = 0 
                            n += 1
                            recentlyadded = True
                        else:
                            game[n+1][m] *= 2
                            game[n][m] = 0 
                            n += 1
                            recentlyadded = True
                    elif game[n+1][m] == 0:
                        #PROXIMITY CHECK!!
                        if (n == 0) and game[2][m] == game[3][m] and game[3][m] != 0:
                            game[3][m] *= 2
                            game[2][m] = 0
                            n += 1 
                        else: 
                            game[n+1][m]= game[n][m]
                            game[n][m] = 0
                            n += 1
                    else:
                        n += 1
            m += 1
def zeroRemoverD(game):
    m = 0
    for i in range(4):
        n = 0
        for i in range(3):   
            if game[n+1][m] == 0:
                game[n+1][m]= game[n][m]
                game[n][m] = 0
                n += 1
            else:
                n += 1
        m += 1
def upMove(game):
    m = 0
    for i in range(4):
        recentlyadded = False
        n = 0
        if (duplicateCheckV(game, m)) == True:
            game[0][m] = 0
            game[1][m] = 0
            game[2][m] *= 2
            game[3][m] *= 2
            m += 1
        else:
            n = -1
            for j in range(3):
                if recentlyadded == True:
                    n -= 1
                    recentlyadded = False
                else:    
                    if game[n][m] == game[n-1][m] and game[n][m] != 0:
                        if n == -1 and game[1][m] == 0 and game[0][m] == game[2][m] and game[0][m] != 0:
                            game[0][m] *= 2
                            game[-2][m] = game[-1][m]
                            game[-1][m] = 0
                            n -= 1
                        elif n>=-2 and game[n-1][m] == game[n-2][m] and game[n-1][m] != 0:
                            game[n-1][m] *= 2
                            game[n-2][m] = 0 
                            n -= 1
                            recentlyadded = True
                        else:
                            game[n-1][m] *= 2
                            game[n][m] = 0 
                            n -= 1
                            recentlyadded = True
                    elif game[n-1][m] == 0:
                        #PROXIMITY CHECK!!
                        if (n == -1) and game[0][m] == game[1][m] and game[0][m] != 0:
                            game[0][m] *= 2
                            game[1][m] = 0
                            n -= 1 
                        else: 
                            game[n-1][m]= game[n][m]
                            game[n][m] = 0
                            n -= 1
                    else:
                        n -= 1
            m += 1  
def zeroRemoverU(game):
    m = 0
    for i in range(4):
        n = -1
        for i in range(3):
                if game[n-1][m] == 0:
                    game[n-1][m]= game[n][m]
                    game[n][m] = 0
                    n -= 1
                else:
                    n -= 1
        m += 1  
game = [
    [int(x) for x in input().split()],
    [int(x) for x in input().split()],
    [int(x) for x in input().split()],
    [int(x) for x in input().split()],
    ]
movement = int(input())
if movement == 0:
    leftMove(game)
    zeroRemoverL(game)
    zeroRemoverL(game)
    zeroRemoverL(game)
elif movement == 2:
    rightMove(game)
    zeroRemoveR(game)
    zeroRemoveR(game)
    zeroRemoveR(game)
elif movement == 3:
    downMove(game)
    zeroRemoverD(game)
    zeroRemoverD(game)
    zeroRemoverD(game)
elif movement == 1:
    upMove(game)
    zeroRemoverU(game)
    zeroRemoverU(game)
    zeroRemoverU(game)
for i in range(4):
    for j in range(4):
        print(game[i][j], end=" ")
    print()