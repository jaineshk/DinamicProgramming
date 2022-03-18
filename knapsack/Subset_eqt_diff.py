def Countsubset_eqltodiff(a,n):
    S1 = (n+(sum(a)))//2
    size = len(a)

    K =[[0 for x in range(S1+1)]for x in range(size+1)]

    for i in range(S1+1):
        K[0][i] = 0
    for i in range(size+1):
        K[i][0] = 1

    for i in range(1,size+1):
        for j in range(1,S1+1):
            if a[i-1] <= j:
                K[i][j] = K[i-1][j] + K[i-1][j - a[i-1]]
            else:
                K[i][j] = K[i-1][j]   

    return K[size][S1]

a = [1, 1, 2, 3]
diff = 1
 
print("The count is", Countsubset_eqltodiff(a, diff))