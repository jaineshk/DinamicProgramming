def findMin(array:list, lenght:list):
    A,N = array,lenght

    add = sum(A)

    #find that which sum is possible with this arry using subset problem
    #only the last row is usefull
    #DP table
    DP = [[False for x in range(add+1)]for x in range(N+1)]

    #assigning the answers to zero values
    for i in range(add+1):
        DP[0][i] = False
    for i in range(N+1):
        DP[i][0] = True

    for i in range(1,N+1):
        for j in range(1,add+1):
            if A[i-1] <= j:
                DP[i][j] = DP[i-1][j] or DP[i-1][j -A[i-1]]
            else:
                DP[i][j] = DP[i-1][j]   
   
    #checking the minimun difference
    mini = add//2
    for j in range(add//2+1):
        if  DP[N][j] == True:
            print(j)
            mini = min(mini, add-(2*j))

    return mini        


a = [3, 1, 4, 2, 2, 1]
n = len(a)
 
print("The minimum difference between "
      "2 sets is ", findMin(a, n))