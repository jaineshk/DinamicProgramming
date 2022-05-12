def LSB(arry,n):
    lis = [0]*n
    

    for i in range(0,n):
        for j in range(i+1,n):

            if (arry[j-1] & arry[j])*2 < (arry[j-1] | arry[j]) and (arry[j-1] < arry[j]):
                lis[i] +=1
            else:
                break    
    print(lis)
    return max(lis)            

arry = [6,9,17,2,15,5,2]
n =len(arry)
print(LSB(arry,n))





 
# def lis(arr):
#     n = len(arr)
 
#     # Declare the list (array) for LIS and
#     # initialize LIS values for all indexes
#     lis = [1]*n
 
#     # Compute optimized LIS values in bottom up manner
#     for i in range(1, n):
#         for j in range(0, i):
#             if arr[i] > arr[j] and lis[i] < lis[j] + 1:
#                 lis[i] = lis[j]+1
 
#     # Initialize maximum to 0 to get
#     # the maximum of all LIS
#     maximum = 0
#     print(lis)
 
#     # Pick maximum of all LIS values
#     for i in range(n):
#         maximum = max(maximum, lis[i])
 
#     return maximum
# # end of lis function
 
 
# # Driver program to test above function
# arr = [10, 22, 9, 33, 21, 50, 41, 60]
# print ("Length of lis is", lis(arr))