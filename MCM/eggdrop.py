import sys
dp = [[-1 for i in range(100)]for i in range(100)]
def eggdrop(e,f):
    #base
    if f==0 or f==1:
        return f
    if e == 1:
        return f
    if dp[e][f]!= -1:  
        return dp[e][f]  
    mn = sys.maxsize
    for k in range(1,f):
        if dp[e-1][k-1] != -1:
            broken =  dp[e-1][k-1]
        else:
            broken = eggdrop(e-1,k-1)  
            dp[e-1][k-1] = broken 

        if dp[e][f-k] != -1:
            unbroken =  dp[e][f-k]
        else:
            unbroken = eggdrop(e,f-k)  
            dp[e][f-k] = unbroken

        temp = 1+max(broken,unbroken)
        mn = min(mn,temp)
    dp[e][f] =mn
    return mn

e = 3
f = 5
print("mini attempt in worst case ",eggdrop(e,f))
