# same code as print LCS little change.
# get teh table and print it.

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
    i = x
    j = y
    result = ""
    while (i>0 and j>0):
        if a[i-1]==b[j-1]:
            result = a[i-1] + result
            i-=1 ; j-=1 
        else:
            if M[i-1][j]>M[i][j-1]:
                result = a[i-1] + result
                i-=1
            else:
                result = b[j-1] + result
                j-=1

    while(i>0):
        result = a[i-1] + result
        i-=1

    while(j>0):
        result = b[j-1] + result
        j-=1

    
    return result

X = "ACBCF"
Y = "ABCDAF"
print ("shortest common super sequence ", lcs(X , Y, len(X), len(Y)) )