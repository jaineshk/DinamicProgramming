def cutRod(a,s):
    K=[[0 for x in range(s+1)]for x in range(s+1)]

    for i in range(s+1):
        for j in range(s+1):
            if (i == 0 or j == 0):
                K[i][j] = 0

            elif i <= j:
                K[i][j] = max (a[i-1] +  K[i][j-i] ,K[i-1][j] )

            else:
                  K[i][j] = K[i-1][j]  

    return K[s][s]

arr = [1, 5, 8, 9, 10, 17, 17, 20]
size = len(arr)
print("Maximum Obtainable Value is " + str(cutRod(arr, size)))