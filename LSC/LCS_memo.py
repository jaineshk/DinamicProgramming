
def lcs(a,b,x,y):
    #memo
    if M[x][y] != -1:
        return M[x][y]
    #base
    if(x==0 or y ==0):
        return 0 
    elif a[x-1]==b[y-1]:
        M[x][y] = 1+lcs(a,b,x-1,y-1)# never forget the 1
        return M[x][y]
    else:
        M[x][y] = max(lcs(a,b,x-1,y),lcs(a,b,x,y-1))
        return M[x][y]



X = "AGGTAB"
Y = "GXTXAYB"
M = [[-1 for i in range(1001)] for j in range(1002)]
print ("Length of LCS is ", lcs(X , Y, len(X), len(Y)) )