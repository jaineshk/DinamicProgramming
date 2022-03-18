def lcs(a,b,x,y):
    M = [[0 for i in range(y+1)] for j in range(x+1)]
    #starting the loop
    for i in range(x+1):
        for j in range(y+1):
            #base condition
            if(i==0 or j==0):
                M[i][j] = 0
            elif a[i-1]==b[j-1]:
                M[i][j] = 1 + M[i-1][j-1] 
            else:
                M[i][j] = max(M[i-1][j],M[i][j-1]) 
    print(M)
    return M[x][y]

X = "AGGTAB"
Y = "GXTXAYB"
print ("Length of LCS is ", lcs(X , Y, len(X), len(Y)) )