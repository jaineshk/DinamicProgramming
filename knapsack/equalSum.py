
# is subset Code
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
                
    #to print the values
    # for i in range(n + 1):
    #     for j in range(sum + 1):
    #         print (K[i][j], end =" ")
    #         print()


    return  K[n][sum]      

# check if sum is even or not 
def findPartition(arr,n):
    add = sum(arr)
    #if not even then equal sum not possible
    if add % 2 != 0:
        return False
    #if even the call the subsetSum method to check one of the sum is half the value or not
    #if it is then it is equal sum
    else:
        return isSubsetSum(arr,n,add)



arr = [3, 1, 1, 2, 2, 1]
n = len(arr)
 
# Function call
if findPartition(arr, n) == True:
    print("Can be divided into two",
          "subsets of equal sum")
else:
    print("Can not be divided into ",
          "two subsets of equal sum")