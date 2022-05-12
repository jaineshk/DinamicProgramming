import sys

dp =[[-1 for i in range(1001)]for i in range(1001)]
def ispalindrome(x):
    return x == x[::-1]
 
def minPalPartion(str, i, j):
    if dp[i][j] != -1:
        return dp[i][j]  
    mn = sys.maxsize
    if ispalindrome(str[i:j+1]):
        return 0
    if i>=j:
        return 0 
    for k in range(i,j):
        # +1 because we do one in middlep partition and 2 with the code 
        # optimizing ti check that each of the subcalls are present in materix ofr not
        left,right = 0,0
        if dp[i][k] != -1:
            left = dp[i][k]
        else:
            left = minPalPartion(str,i,k)
            dp[i][k] = left

        if dp[k+1][j] != -1:
            right = dp[k+1][j]
        else:
            left = minPalPartion(str,k+1,j)
            dp[k+1][j] = right

        temp = 1 + left + right
        if mn > temp:
            mn = temp
    dp[i][j] = mn        
    return mn

def main():
    string = "geek"
    print("Min cuts needed for Palindrome Partitioning is ",minPalPartion(string, 0, len(string) - 1),)
 
if __name__ == "__main__":
    main()