def countoccur(data):
	str1 = data.split()
	count = dict()
	for i in str1:
		if i in count:
			count[i] += 1
		else:
			count[i] = 1

	return count

print(countoccur('the best there is the best there will be'))

