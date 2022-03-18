# A dynamic programming based Python3 program print
# shortest supersequence of two strings

# returns shortest supersequence of X and Y
def printShortestSuperSeq(x, y):
	m = len(x)
	n = len(y)

	# dp[i][j] contains length of shortest
	# supersequence for X[0..i-1] and Y[0..j-1]
	dp = [[0 for i in range(n + 1)]
			for j in range(n + 1)]

	# Fill table in bottom up manner
	for i in range(m + 1):
		for j in range(n + 1):

			# Below steps follow recurrence relation
			if i == 0:
				dp[i][j] = j
			elif j == 0:
				dp[i][j] = i
			elif x[i - 1] == y[j - 1]:
				dp[i][j] = 1 + dp[i - 1][j - 1]
			else:
				dp[i][j] = 1 + min(dp[i - 1][j],
								dp[i][j - 1])

	# Following code is used to print
	# shortest supersequence
    
	# dp[m][n] stores the length of the
	# shortest supersequence of X and Y

	# string to store the shortest supersequence
	string = ""
    
	# Start from the bottom right corner and
	# one by one push characters in output string print(dp)
	i = m
	j = n
	while i > 0 and j > 0:

		# If current character in X and Y are same,
		# then current character is part of
		# shortest supersequence
		if x[i - 1] == y[j - 1]:

			# Put current character in result
			string += x[i - 1]

			# reduce values of i, j and index
			i -= 1
			j -= 1

		# If current character in X and Y are different
		elif dp[i - 1][j] > dp[i][j - 1]:

			# Put current character of Y in result
			string += y[j - 1]

			# reduce values of j and index
			j -= 1
		else:

			# Put current character of X in result
			string += x[i - 1]

			# reduce values of i and index
			i -= 1

	# If Y reaches its end, put remaining characters
	# of X in the result string
	while i > 0:
		string += x[i - 1]
		i -= 1

	# If X reaches its end, put remaining characters
	# of Y in the result string
	while j > 0:
		string += y[j - 1]
		j -= 1

	string = list(string)

	# reverse the string and return it
	string.reverse()
	return ''.join(string)

# Driver Code
if __name__ == "__main__":
	x = "AGGTAB"
	y = "GXTXAYB"

	print(printShortestSuperSeq(x, y))

# This code is contributed by
# sanjeev2552
