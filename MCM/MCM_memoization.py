import sys
dp =[[-1 for i in range(1001)]for i in range(1001)]

def solve(arry,i,j):
    mn = sys.maxsize
    #base
    if  i>=j:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]  

    for k in range(i,j):
        value = solve(arry,i,k)+solve(arry,k+1,j)+arry[i-1]*arry[k]*arry[j]
        if value < mn:
            mn = value
    dp[i][j] = mn
    return mn         

def MCM(arry):
    i = 1
    j = len(arry)-1
    value = solve(arry,i,j)
    return value

arry = [10, 20, 30, 40, 30]
print("minimum materix mul is ",MCM(arry))