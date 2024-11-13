def Golomb_precomp(n): 
 
    dp = [1,2,2]
    # Finding and print first 
    # n terms of Golomb Sequence.
    for i in range(3,n+1):
        dp.extend([i]*dp[i-1]) 
    return dp

print(x:=Golomb_precomp(438744))
while True:
    positionF = int(input())
    if positionF == 0:
        break
    print(x[positionF])