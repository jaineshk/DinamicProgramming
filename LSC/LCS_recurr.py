def lcs(a,b,x,y):
    #base
    if(x==0 or y ==0):
        return 0
    #if the last digit at the string matches
    elif(a[x-1]==b[y-1]):
        return 1+lcs(a,b,x-1,y-1) 
    #if last digit of the string doesn't match
    # remove either one of the last charater    
    else: 
        return max(lcs(a,b,x-1,y),lcs(a,b,x,y-1))       


X = "AGGTAB"
Y = "GXTXAYB"
print ("Length of LCS is ", lcs(X , Y, len(X), len(Y)) )

