#matrix chain multiplication
import sys
def MCM(arry,i,j):
    #max value
    mn = sys.maxsize
    #base condition
    if i>=j:
        return 0
    for k  in range(i,j):
        temp = MCM(arry,i,k)+ MCM(arry,k+1,j) + arry[i-1]* arry[k] * arry[j]
        if (temp < mn):
            mn = temp
    return mn        



arry = [10, 20, 30, 40, 30]
i = 1
j = len(arry)-1
print("minimum materix mul is ",MCM(arry,i,j))
