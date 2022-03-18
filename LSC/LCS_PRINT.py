#my method

# def lcs(a,b,x,y):
#     M = [[0 for i in range(y+1)] for j in range(x+1)]
#     #starting the loop
#        #base condition
#     for i in range(x+1):
#         M[i][0] = ""
#     for i in range(y+1):
#         M[0][i] = ""    
#     for i in range(1,x+1):
#         for j in range(1, y+1):     
#             if a[i-1]==b[j-1]:
#                 M[i][j] = M[i-1][j-1] + a[i-1]
#             else:
#                 if len(M[i-1][j])>len(M[i][j-1]):
#                     M[i][j] = M[i-1][j]
#                 else:
#                     M[i][j] = M[i][j-1] 
#     print(M)                              
#     return M[x][y]

# X = "AGGTAB"
# Y = "GXTXAYB"
# print ("Length of LCS is ", lcs(X , Y, len(X), len(Y)) )




#learned method
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
    i = x
    j = y
    result = ""
    while (i>0 and j>0):
        if a[i-1]==b[j-1]:
            result = a[i-1] + result
            i-=1 ; j-=1 
        else:
            if M[i-1][j]>M[i][j-1]:
                i-=1
            else:
                j-=1

    print(result)
    return M[x][y]

X = "AGGTAB"
Y = "GXTXAYB"
print ("Length of LCS is ", lcs(X , Y, len(X), len(Y)) )