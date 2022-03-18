def SCS(a,b,x,y):
    k=[[0 for i in range(y+1)]for i in range(x+1)]

    #initailization include in main
    for i in range(x+1):
        for j in range(y+1):
            #base
            if i==0 or j==0:
                k[i][j] = 0
            elif a[i-1]==b[j-1]:
                k[i][j] = 1+k[i-1][j-1]
            else:
                k[i][j]= max(k[i-1][j],k[i][j-1])

    # for SCS we need to subtract the LCS 
    # from sum of length of both string.
    scs = (x+y) - k[x][y]
    return scs

a ='aggtab'
b='gxtxayb'
print("The shortest Common super Sequence of A and B is  "+ str(SCS(a,b,len(a),len(b))) )