def optValue(arrayValues, arrayWeights, maxWeight):
	# A compact algorithm to compute the optimal sum value in a problem of N points
	# having a value and a wight, that does not exceeds a certain maximum weight W. Executes in O(N*W) time.
	# Imput: arrayValues[N] which holds the values of each point and arrayWeights[N] which holds their weights,
	# and int mawWeight the largest sum of weigths allowed.
	# Output: Biggest sum of values.

	progress = [[0]*(maxWeight + 1) for i in range(len(arrayValues) + 1)]
	for i in range(1, len(arrayValues) + 1):
		for j in range(0, maxWeight + 1 ):
			if (j - arrayWeights[i - 1] >= 0):
				if progress[i-1][j] < progress[i-1][j - arrayWeights[i - 1]] + arrayValues[i - 1]:
					progress[i][j] = progress[i-1][j - arrayWeights[i - 1]] + arrayValues[i - 1]
					continue
			progress[i][j] = progress[i-1][j]
	return progress[len(arrayValues)][maxWeight]