# memoization applied

def knapsack(weight,values,w,n):
    #base condition selected at lowest value
    if( n==0 or w==0):
        return 0
    if tp[n][w] != -1:
        return tp[n][w]

    # if bag wieght is not enough to fill the value
    if weight[n-1] > w:
        tp[n][w] = knapsack(weight,values,w,n-1)
        return tp[n][w]
    # bag wieght is enough we take max of two condition.
    # One to select the value and other not to.    
    else:
        tp[n][w] =  max (values[n-1] + knapsack(weight,values,w-weight[n-1],n-1), knapsack(weight,values,w,n-1)) 
        return tp[n][w] 

# driver code
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
tp = [[-1 for x in range(W+2)]for x in range(n+2)]
print(knapsack(wt,val,W,n))
print(tp)
