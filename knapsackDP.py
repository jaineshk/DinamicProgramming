#Dynamic program applied

def knapsack(weight,values,w,n):\
    #creating matrix with zero
    tp = [[0 for x in range(w+2)]for x in range(n+2)]
    #going through loops
    #storing values for sub condition the returning the last tp[n][w] as answer
    for i in range(0,n+1):
        for j in range(0,w+1):
            #base condition
            if( i==0 or j==0):
                tp[i][j]
            # if bag wieght is not enough to fill the value
            elif weight[i-1] > j:
                tp[i][j] = tp[i-1][j]   
            # bag wieght is enough we take max of two condition.
            # One to select the value and other not to.    
            else:
                tp[i][j] =  max(values[i-1] + tp[i-1][j-weight[i-1]], tp[i-1][j])

    return tp[n][w]   
        
# driver code
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(knapsack(wt,val,W,n))

