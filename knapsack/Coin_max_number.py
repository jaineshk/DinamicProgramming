def subset_sum(arry:list, length: int, sum: int):
    K = [[0 for x in range(sum+1)]for x in range(n+1)]

    for i in range(sum+1):
        K[0][i] = 0

    for i in range(length+1):
        K[i][0] = 1


    for i in range(1, length+1):
        for j in range(1, sum+1):

            if (arry[i-1] <= j):
                K[i][j] = K[i-1][j]+ K[i][j-arry[i-1]]
            else:
                 K[i][j] = K[i-1][j] 

    return K[length][sum]

a = [1,2,3]
n = len(a)
sum = 5
print(subset_sum(a, n, sum))