#subset
def isSubsetSum(set,n,sum):
    K = [[False for x in range(sum+1) ]for x in range(n+1) ]
    #for 1 row all false 
    for i in range(0,sum+1):
        K[0][i] = False
    #for the first column True
    for i in range(0,n+1):
        K[i][0] = True
    #for fil in the conter part
    for i in range(1,n+1):
        for j in range(1, sum+1):
            if (set[i-1]<= j) :
                K[i][j] = (K[i-1][j-set[i-1]] or K[i-1][j])
            else:
                K[i][j] = K[i-1][j]  

    for i in range(n + 1):
        for j in range(sum + 1):
            print (K[i][j], end =" ")
            print()


    return  K[n][sum]                 


Set = [3, 34, 4, 12, 5, 2]
sum = 9
n = len(Set)
if (isSubsetSum(Set, n, sum) == True):
    print("Found a subset with given sum")
else:
    print("No subset with given sum")

