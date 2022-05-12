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
        temp = 1 + minPalPartion(str,i,k)+ minPalPartion(str,k+1,j) 
        if mn > temp:
            mn = temp
    dp[i][j] = mn        
    return mn

def main():
    string = "geek"
    print("Min cuts needed for Palindrome Partitioning is ",minPalPartion(string, 0, len(string) - 1),)
 
if __name__ == "__main__":
    main()