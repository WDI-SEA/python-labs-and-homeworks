def letter_counter(word):
	result = {}
	for i in word:
		if i in result:
			result[i] += 1
		else:
			result[i] = 1
	print(result)

letter_counter('banana')