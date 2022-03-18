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
    return M[x][y]

def LPS(a):
    b = a[::-1]
    value = lcs(a,b,len(a),len(b))
    return value    
# driver code
X = "AGBCBA"
ans = LPS(X)
print ("longest palindromic seq is ", LPS(X) )

# to find minimum number of Deletion and insertion
print("Mini no of insertion to make this a palindrome ", len(X)-ans)
print("Mini no of deletion to make this a palindrome ", len(X)-ans)
