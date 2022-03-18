import sys

def minCoins(c,m,v):
    K=[[0 for x in range(v+1)]for x in range(m+1)]
    #initializing the first column and row
    for i in range(m+1):
        K[i][0] = 0
    for i in range(v+1):
        K[0][i] = sys.maxsize-1

    #initalizing of 2 row
    for i in range(1,v+1):
        if i%c[0] != 0:
            K[1][i] = sys.maxsize-1
        else:
            K[1][i] = i%c[0]   

    for i in range(2,m+1):
        for j in range(1,v+1):
            if c[i-1]<=j:
                K[i][j] = min(K[i-1][j], K[i][j-c[i-1]]+1)
            else:
                K[i][j] = K[i-1][j]

    return K[m][v]



coins = [9, 6, 5, 1]
m = len(coins)
V = 11
print("Minimum coins required is",minCoins(coins, m, V))